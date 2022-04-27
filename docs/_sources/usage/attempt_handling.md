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

class MyAttemptHandler():
    """Class that handles your attempts.
    
    The name of the class is arbitrary

    Mandatory attributes: `next_attempt` which represents your next attempt, type must be convertable by str() function to string, typically a string or an integer, if all attempts are exhausted and you want to stop this must be set to None.
                                    
    Class can have arbitrarily more optional attributes. 
    However, all attributes must be serializable by the pickle library, see https://docs.python.org/3/library/pickle.html.
    The serialization into a file is necessary to store the state of the attempt handler over several jobs.
    IMPORTANT: If you want to start from scratch, you have to remove such files, which are sored as <run_name>_attempt_handler.obj in the root directory.

    Parameters can be arbitrary. In this example:

    :param root:        Path to the root directory
    :type root:         str     
        
    """
    
    def __init__(self, root = "."):  
    
        # initialize mandatory attribute self.next_attempt
        self.next_attempt = 1
    
        
        # optional arguments and members
        
        # it makes sense to memorize the root directory
        self.root = root     
        
        # our maximal number of attempts
        self.max_attempts = 4
        
    def prepare_attempt(self, **kwargs):
        r"""
        Mandatory method to prepare the attempt.
        
        Do whatever is necessary to set up the next attempt, e.g. manipulating input files.

        :Keyword Arguments:

        * **start_date** (*int*) --
          Start date of the current job in format YYYMMDD
        * **end_date** (*int*) --
          End date of the current job in format YYYMMDD  
                
        """     

        # you can use the keyword arguments
        start_date = kwargs["start_date"]
        end_date = kwargs["end_date"]
        print("Peparing " + str(self.next_attempt) + " for start date " +  str(start_date) + " and end date " + str(end_date))
        
        # copy some prepared files to the actual input file
        input_nml = self.root + "/input/MOM5_Baltic/input.nml"
        os.system("cp " + input_nml + "." + str(self.next_attempt) + " " + input_nml)
        
        return

    def evaluate_attempt(self, crashed, **kwargs):
        r"""
        Mandatory method to evaluate the attempt.
        
        In this method the setting of the next_attempt should typically happen, e.g. incrementation.
        Important: If all attempts are exhausted, next_attempt must be set tot `None`.
        Important: If model has crashed, this function should return False otherwise following steps are ill-defined.

        :param crashed:         `True`, if the model has crashed, `False`, otherwise
        :type crashed:          bool   

        :Keyword Arguments:
        
        * **start_date** (*int*) --
          Start date of the current job in format YYYMMDD
        * **end_date** (*int*) --
          End date of the current job in format YYYMMDD          

        :return:                `True`, if attempt is accepted (work will be copied to output, hotstart folder is created), `False`, if attempt is not accepted (work will not be copied to output, no hotstart folder is created)      
        :rtype:                 bool
        """ 

        # you can use the keyword arguments
        start_date = kwargs["start_date"]
        end_date = kwargs["end_date"]
        print("Evaluating " + str(self.next_attempt) + " for start date " +  str(start_date) + " and end date " + str(end_date))

        # if the model has crashed, react here
        if crashed:
            
            # we have no attempts left, we should stop here
            if self.next_attempt == self.max_attempts:
                self.next_attempt = None
                return False
            
            # there are attempts left, go to the next set of input files 
            self.next_attempt += 1
            # throw away work of failed attempt (you might also store it somewhere for debugging)
            return False
            
        # if the model did succeed, we can go back to the previous input files
        if self.next_attempt > 1:
            self.next_attempt -= 1                
            
        return True
```

Read the comments in this code and understand what is happening.
This MOM5-specific example handles 4 attempts related to some prepared input files `input/MOM5_Baltic/input.nml.1` to `input/MOM5_Baltic/input.nml.4`.
While creation, the object gets an additional member for memorizing the root path of the project. 
However you can pass arbitrary arguments to the constructor.
For the first attempt, the example class copies the prepared input file `input/MOM5_Baltic/input.nml.1` to the actually used input file `input/MOM5_Baltic/input.nml`, see the `prepare_attempt` method.
If the run fails (`crashed = True` in the `evaluate_attempt` method) with this input file, we will go to the next attempt (`self.next_attempt += 1`) and the next time `prepare_attempt`is called we will use the input file `input/MOM5_Baltic/input.nml.2`.
If this attempt succeeds we will go back to the previous attempt (`self.next_attempt -= 1`), i.e. to the input file `input/MOM5_Baltic/input.nml.1`.
If a run failed 4 time in a row (`self.next_attempt == self.max_attempts`) all attempts are exhasuted and we stop (`self.next_attempt = None`).

Of course for your application you have to implement your own functionality according to your needs.


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

**Important**
* the preparation takes place _before_ the input files are copied to the local work directories
* the evaluation takes place _after_ the output is copied to the global `work` directory but _before_ it is stored in the `output` directory
* if the evaluation returns `True` the content of `work` is copied to `output` and hotstart files are also copied to the `hotstart` directory, thus the run is assumed to be valid and the next run starts from these hotstart files
* if the evaluation return `False` nor output neither hotstart files are copied and thus this run is assumed to be invalid and the next run will start from the last available hotstart files
* evaluating with `True` while `crashed = True` will yield an error and the model is aborted (a crashed run cannot be successful!)

In other words you best prepare your attempt in the `input` directory and evaluate it in the global `work` directory.

Note that preparation and evaluation are intended to be rather small and fast tasks since these steps consume walltime of your job. 

### The default case

The default for the variable `attempt_handler` would be `None` or it can be left out.
In both cases there will be a single attempt for each run without preparation and always positive evaluation (however a run can of cource  still fail if the model crashes)