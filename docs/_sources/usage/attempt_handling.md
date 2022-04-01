# Attempt handling

## 1. Set up the IOW ESM framework

Follow the steps described in the Readme you can find at the project's [main site](https://git.io-warnemuende.de/iow_esm/main).

After you have set up everything go to the target machine. 



## 2. Create your own attempt handler

Once you are on the target you have to create a python module, let's call it `my_attempt_handling.py`.
You can create it anywhere you like but let's assume for this example that you create it in the path to the root directory of the IOW ESM, say `"/path/to/IOW_ESM"`.

This module has to contain a class with some mandatory members and methods as illustrated in the following example:

``` python
# imports for this example, you can import arbitrary modules here
import os
import glob

# class name is arbitrary
class MyAttemptHandler():
    
        # constructor can have arbitrary arguments
        def __init__(self, root = "."):
                # !!! mandatory member attempts must be a list of strings
                self.attempts = ["1", "2"]
                # !!! mandatory member last_attempt_file must be a name of a file (can be a path, absolute or relative to "/path/to/IOW_ESM/scripts/run") that can be created and read
                self.last_attempt_file = "my_last_attempt.txt"

                # optional arguments and members
                # it makes sense to memorize the root directory
                self.root = root

        # !!! mandatory method for preparing an attempt, signature is obligatory
        def prepare_attempt(self, attempt):

                if attempt == self.attempts[0]:
                        # do nothing for the first attempt
                        return

                if attempt == self.attempts[1]:
                        # do something with input files for second attempt
                        os.system("touch " + self.root + "/attempt2.txt")
                        return

                return

        # !!! mandatory method for evaluating an attempt, signature is obligatory, must return True or False
        def evaluate_attempt(self, attempt):

                # in this example let's provoke that the first attempt fails
                if attempt == self.attempts[0]:
                        return False

                # let the second attempt succeed if file from preparation has been created
                if attempt == self.attempts[1]:
                        if glob.glob(self.root + "/attempt2.txt") != []:
                                return True

                return True
```

Read the comments in this code and understand what is happening.
This dummy example handles two attempts called `"1"` and `"2"`, see member `attempts`.
While creation, the object gets an additional member for memorizing the root path of the project. 
However you can pass arbitrary arguments to the constructor.
The example class does nothing to prepare the first attempt but creates an empty file for the second attempt, see the `prepare_attempt` method.
It is further constructed such that the first attempt will always fail and the second succeeds only if the empty file has been created, `evaluate_attempt` method.

Of course for your application you have to implement your own functionality according to your needs.

## 2a. Extension

The `evaluate_attempt` method may also have two arguments. The `crashed` argument will be `True` or `False` if the model has technically crashed or not, respectively. 

```python
        def evaluate_attempt(self, attempt, crashed):
        
                # recognize crash (and possibly react) but allow model to rerun within the same attempt
                if crashed:
                        os.system("touch " + self.root + "/attempt_" + attempt + "_crashed.txt")
                        return True
                    
                # in this example let's provoke that the first attempt fails
                if attempt == self.attempts[0]:
                        return False

                # let the second attempt succeed if file from preparation has been created
                if attempt == self.attempts[1]:
                        if glob.glob(self.root + "/attempt2.txt") != []:
                                return True

                return True
```

This allows you to react to crashes very individually.

## 3. Register your attempt handler

In order to register your attempt handler you have to pass an instance via the `global_settings.py` in the `input` folder within your `"/path/to/IOW_ESM"`.
For the example given above you would have to add the following lines to the `global_settings.py` file.

``` python
#################################################
# STEP 3a: Attempt handling                     #
#################################################

# import own module 
import sys
sys.path.append("/path/to/IOW_ESM") # you can put absolute paths here, if not this path is interpreted relative to scripts/run 
import my_attempt_handling

# create instance of the attempt handler
attempt_handler = my_attempt_handling.MyAttemptHandler("/path/to/IOW_ESM")                      # if a run fails, you can have new attempts with modified settings

```

Again the name `my_attempt_handling`, `MyAttemptHandler` as well as the path `"/path/to/IOW_ESM"` might be different for you.

## 4. How the IOW ESM calls the attempt handler 

The IOW ESM will call the attempt handler such that it iterates over the entries in `attempt_handler.attempts`. It will stay within an attempt until the  `evaluate_attempt` method returns `False`. Then it will go to the next attempt until the last attempt is exhausted. If the `evaluate_attempt` method takes only one argument, a crash of the model will also lead to the next attempt.

The corresponding code from `scripts/run/run.py` looks like:

``` python
for run in range(runs_per_job):
        
    # get next attempt from the file specified in member last_attempt_file (done by an attempt_iterator object)
    attempt = attempt_iterator.get_next_attempt()

    # PREPARATION
    # prepare the attempt
    attempt_handler.prepare_attempt(attempt)

    # perform attempt
    # ...
    # set crashed = True if the model crashed

    # EVALUATION
    # either:
    # if the evaluate_attempt method takes one arguments, the call looks like
    if not crashed:
        # if the run did not crash, still check for evaluation
        run_failed = not attempt_handler.evaluate_attempt(attempt)
    else:
        run_failed = True
    
    # or:
    # if the evaluate_attempt method takes two arguments, the call looks like
    run_failed = not attempt_handler.evaluate_attempt(attempt, crashed)
    
    # something went wrong: either model has crashed or the attempt has not passed the criterion 
    if run_failed:
        # if this was the final attempt, we stop here
        if attempt == attempt_handler.attempts[-1]:
            print('IOW_ESM job finally failed integration from '+str(start_date)+' to '+str(end_date))
            sys.exit()

        # if it was not the final attempt, memorize this attempt (done by an attempt_iterator object)
        attempt_iterator.store_last_attempt(attempt)
        
        # go on with next attempt in a new job
        print('  attempt '+str(attempt)+' failed. Go on with next attempt.', flush=True)
        os.system("cd " + IOW_ESM_ROOT + "/scripts/run; " + resubmit_command)
        sys.exit()

```

**Important**
* the preparation takes place _before_ the input files are copied to the local work directories
* the evaluation takes place _after_ the output is copied to the global `work` directory but _before_ it is stored in the `output` directory

In other words you best prepare your attempt in the `input` directory and evaluate it in the global `work` directory.

Note that preparation and evaluation are intended to be rather small and fast tasks since these steps consume walltime of your job. 

### The default case

The default for the variable `attempt_handler` would be `None` or it can be left out.
In both cases there will be a single attempt for each run without preparation and always positive evaluation (however a run can of cource  still fail if the model crashes)