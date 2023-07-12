(usage:prepare_input_folders)=
# Preparing the input folders for individual model runs

The IOW ESM is able to run a single atmospheric model and several ocean or land models at the same time. 
For each of these sub-models, a sub-folder in the input directory has to be prepared. 
It shall be named `MODELNAME_GRIDNAME` where `MODELNAME` is the name of the model (as it is called in the components folder) and `GRIDNAME` is the name of the model grid.
To start, it makes most sense to look into the input folders that come with the example configuration. 
When you create your own model configurations, you can start by modifying those.

## General remarks

The input folders can contain files and arbitrarily named sub-directories which will simply be copied (or dynamically linked) to create a work directory for the model. 
An exception are subfolders named `from`. 
These should themselves contain subfolders named after years or dates as `YYYYMMDD` (e.g. `1950` or `19501201`). 
In case that the starting date of a model run is equal to or larger than a subfolder’s date, the files inside this folder will be copied to the directory containing the folder `from`. 
For example, if there are files
```
input/MOM5_maingrid/OBC/from/1950/obc_sealevel.nc
input/MOM5_maingrid/OBC/from/1951/obc_sealevel.nc
input/MOM5_maingrid/OBC/from/1952/obc_sealevel.nc
```
and the starting date of a model run is `1951-06-01`, the file
```
input/MOM5_maingrid/OBC/from/1951/obc_sealevel.nc
```
will be copied (or linked) to
```
work/MOM5_maingrid/OBC/obc_sealevel.nc
```

## Expected contents of the COSMO-CLM input directory

TODO what is expected here???

The following settings are required in `INPUT_PHY`:
```
llake = FALSE
lseaice = FALSE
```

## Expected contents of a MOM5 input directory

TODO what is expected here

