(usage:directory_structure)=
# Directory Structure of the IOW ESM

Under a base directory which the user can select, there is the following directory structure, which will be explained in the following subsections:

```
components
   OASIS3-MCT
   COSMO-CLM
   MOM5
   flux_calculator
input
   CCLM_MAINGRID
   MOM5_MAINGRID
   GETM_SUBGRID
scripts
   prepare
   run
   post
work
   CCLM_MAINGRID
   MOM5_MAINGRID
   GETM_SUBGRID
output
   RUN01
      CCLM_MAINGRID
         19500101
         19510101
         ...
      MOM5_MAINGRID
         ...
      GETM_SUBGRID
         ...
   RUN02
      ...
hotstart
   RUN01
      CCLM_MAINGRID
         19510101
         19520101
         ...
   RUN02
   ...
```

## The components directory

This directory contains the components of the IOW-ESM, which are
* **COSMO-CLM**, a regional atmospheric model,
* **MOM5**, a hydrodynamic ocean model,
* the **OASIS3-MCT** library for coupling the components via MPI,
* the **flux calculator**, a separate executable to calculate fluxes between atmosphere and ocean/land on an exchange grid.

Each component’s directory contains subdirectories for
* the source code,
* the compile scripts,
* the compiled libraries and/or executables.
In some cases, the directory contains a GIT repository of source code, such that the changes
to the ocial GIT release of that model component can be easily seen.

## The input directory

The user of the model system has to create a directory called input. i
It contains subdirectories for the individual model instances which shall be coupled. 
For each model instance, the subdirectory shall be named `MODELNAME_GRIDNAME` where `MODELNAME` is the name of the model (as it is called in the components folder) and `GRIDNAME` is the name of the model grid, since more than one instance of a model can run at the same time but with different grids. 
Read [here](usage:prepare_input_folders) how to store model input in these folders.

In addition, there are three files directly in the input directory:
* `global_settings.py` contains settings for the entire model system, such as name and duration of the present run, coupling timestep, or whether the work directory in which the coupled model runs should be global or node-local.
* `flux_calculator.nml` is a configuration file for the `flux_calculator` executable which defines how fluxes between atmosphere and land/sea shall be calculated, i.e. which bulk formulae are used.
* `namcouple` is the OASIS3-MCT coupling configuration file and describes how data are exchanged between the model subcomponents. It needs to match the configuration in `flux_calculator.nml`.

## The scripts directory

This directory contains scripts (bash or python3 scripts) which perform tasks in preparing model runs, running the model system, or postprocessing of data.

## The work directory (automatically created during model start)

This is the directory in which the models are actually executed. It can also be located in another place, such as a RAM drive. 
If the model run fails, you can check for errors here.

## The output directory (automatically created during model run)

For each run of the model system, there will be a separate directory which contains the model results. 
These are sorted by sub-model and by starting time.

## The hotstart directory (automatically created during model run)

This contains hotstart files to restart the model from a specific date. 
The directory is sorted like the `output` folder.
