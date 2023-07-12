# Advanced use


## Advanced destination keywords

It is possible to use not only the destination keywords given in [Configure your destinations (targets)](#configure-your-destinations-(targets)).
You can also use something like e.g. `hlrng_XXX` and `hlrng_YYY` if you want to run two independent instances on the target `hlrng`.
However, the string before the *first* underscore *must* be one of the keywords given above.

## Building during development


### Build single components in a different modes and configurations

If you are developing only one component at a time, it is not necessary to call the global build script from the root directory.
There are also build scripts in each components subdirectory which can be called directly, e.g.

``` bash
cd components/flux_calculator
./build.sh hlrng debug rebuild 
``` 

This would rebuild the flux_calculator on the `hlrng` in debug mode.
The defaults for the second and third argument are `release` and `fast` (which is the opposite of `rebuild`).
The same applies likewise to the other components.


### Build tagging

Once you execute a build command, e.g. 

``` bash
./build.sh hlrng
``` 

a file `LAST_BUILD_hlrng_release` is created, 
where the strings `hlrng` and `release` depend on the arguments, you give to the build script.
This file contains information on the state the source code of the components is in.
In particular, it contains the unique commit ID, the build mode (fast/rebuild) and a time stamp of the build.
Moreover, if the source code exhibits uncommited changes when the build script was executed,
these diffrences are logged within that file.
By executing the run script later on, the same tagging will be done for the main repository and this file is transferred to the destination.
That way, you can always identify with which version of the code your working on the target. 

(usage:advanced_use:running_during_development)=
## Running during development

TODO: change this section to use of several input folders.

### Update the setup before running

During development it usual to modify the setup, i.e. parameters in input files.
It is not intended to do this directly on the target, 
because then it is hard to keep track of the changes (still it is possible of course).
However, the run script in the root directory offers the possibility to update the setup directly before running the model.
Before running, you have to prepare a setup used for updating.
The idea is, that you create a local folder where you put the input files that you want to modify.
This folder, e.g. `./local_setup`, must have the same directory structure as a normal setup folder.
For instance, if you want to have a modified `input/global_settings.py` at your destination, 
you create `./local_setup/input/global_settings.py`, make your changes in the file and then register this folder in the `SETUPS` file, 
e.g. by adding the line `update ./local_setup`.
Then you can run the model by calling

``` bash
./run.sh hlrng update
```

This will start the model on the `hlrng` but beforehand it will synchronize the contents of the `./local_setup` to the destination.
Moreover, in `./local_setup` there is file `UPDATE_SETUP_INFO` created, which is also transferred to the target 
and contains information and time stamp of the updating.

In general the run script can be called like

``` bash
./run.sh hlrng [prepare-before-run] update1 update2 update3...
```

where `prepare-before-run` is optional and can be omitted, which is usually the case if it is not the very first run on a target.

The second argument `prepare-before-run` is obligatory for the very first run if the necessary mapping files are not part of the setup yet.
Putting this argument will create necessary mapping files in the destination directories.
However, for all following runs *this is an optional argument and should be omitted*, unless you really want to re-create the mapping files.

The setup updates are transferred in the order they appear, where the last one can, in principle, overwrite the ones before.
*Note that you should not use the keyword `prepare-before-run` for a setup, otherwise the script will be confused.*


## Archiving


### Archiving the employed setup

Imagine you have started your development on `hlrng` from the setup with the keyword `testing`, this can be viewed as the base of your current setup.
Now you made changes to some input files and you want to conserve the current state.
This can be done by using the script

``` bash
./archive_setup.sh hlrng testing archive
```

First, this would produce a copy of the base setup corresponding to the keyword `testing` in the very same destination (you need write permissions there).
The new folder has the same name as `testing` supplemented by `_archive` and it contains only symbolic links to the base setup.
Second, it is checked where the base setup and the one residing on the `hlrng` differ.
Third, only files that are different will be updated from the `hlrng` and put into the created archive folder.
If you want to create your archive in a different directory then your base, you can specifiy a keyword and the corresponding destination in the `SETUPS` file.
You can then call the setup archiving script with that keyword as the third argument.
Note that the base setup and the archive must be available via the same machine since we are using symbolic links here. 

Once you have archived your setup, the `SETUP_INFO` file on your target server will be updated as well.