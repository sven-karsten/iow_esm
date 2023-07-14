# Advanced use

(usage:advanced_use:advanced_destination_keywords)=
## Advanced destination keywords

It is possible to use not only the destination keywords given in [](getting_started:first_use:configure-destinations).
You can also use something like e.g. `hlrng_XXX` and `hlrng_YYY` if you want to run two independent instances on the target `hlrng`.
However, the string before the *first* underscore *must* be one of the keywords given above.


## Building during development

(usage:advanced_use:build-single-components-in-a-different-modes-and-configurations)=
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


(usage:advanced_use:prepare_before_run)=
### Prepare mappings before the run starts

If you want to create new mappings between the model grids (becaus you updated the setups or the paralleization layout) you can put an additional argument (literaly `prepare-before-run`) to the run command, e.g.

``` bash
./run.sh prepare-before-run hlrng
``` 


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