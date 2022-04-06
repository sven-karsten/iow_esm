# Create forcings for the CCLM model with int2lm

The int2lm tool enables creating regional forcings for the Cosmo-CLM model from coarse global model data or reanalysis data.
See https://www.cosmo-model.org/content/model/documentation/core/int2lm_2.08.pdf for more information and/or ask the CLM community.


## Prerequisites

Set up a destiantion (e.g. on the HLRN in Göttingen) as described in [](getting_started:first_use).

Note that you might only clone and build the `tools/I2LM` component for this use case.
As a starting point you can take the example setup `I2LM_example` from the file `SETUPS.example` (or the corresponding example on your favorite target machine).

This example can be used to create CCLM forcings over the Eurocordex domain on an 0.22°x0.22° grid using the ERA-Interim reanalysis data.
If you want to do something else, you have to make some adaptions in the setup.


## Make your adaptions

### Global settings

Once you set up your destination, go there and change to the `input` directory.
Here you find the file `global_settings.py` it has the same format as for other use cases.
How to set it up can be found in [](usage:setting_up_global_settings).


### Jobscript

Follow the steps described in [](usage:setting_up_jobscript).


### Local settings


In the folder `input/I2LM_Eurocordex` the file `local_settings.py` can be found (note that the input folder might be renamed as `I2LM_<your_domain>` according to the domain you want to process).
Here you have to modify the database from where the coarse data is taken for the interpolation.
First, choose a file with the external fields for the CCLM run you want to perform. 
In the example setup this looks like:

``` python
####################################################
#        Local settings for the int2lm run         #
####################################################

###################################
#         Data base               #
###################################
# name of the used climatology file
climatology_file = "climatology_cD3_0220.nc"

# path to the climatology file, if empty it is assumed relative to this directory
climatology_dir = ""
```

TODO: Explain where or how to get the climatology files.

Second, specify where to find coarse data that will be interpolated, e.g.
``` python
# path to the coarse grid data, if empty it is assumed relative to this directory
# in this directory the data should be in subdirectories called yearYYYY (e.g. year1980)
coarse_data_dir = "/scratch/usr/mviowmod/DATABASE/CCLM_FORCING/ERAI"

# prefix of the coarse data files, this might be either "cas" or "caf"
coarse_data_pref = "caf"

```

These so-called `caf` or `cas` files can be found at the DKRZ servers for a few global models and reanalysis data, see https://redc.clm-community.eu/projects/data/wiki/Initial_and_Boundary_Data and/or ask the CLM community.


### Input of the int2lm tool

The main input of the int2lm tool is the file `INPUT` in `input/I2LM_Eurocordex`.
How to set it up correctly can be found in the original documentation https://www.cosmo-model.org/content/model/documentation/core/int2lm_2.08.pdf.
Importantly, variables that have the value `*auto*` in the example setup will be overwritten when the job is running and you do not have to set them manually.


## Start the run

The int2lm tool is started as any other model within the IOW ESM.
So either you use the command line interface, i.e. the `run.sh` script or you can start it with the GUI by hitting `Run`.
See also [](getting_started:first_use) for how to run a model.