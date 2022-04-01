(usage:setting_up_global_settings)=
# Setting up the global_settings.py

The file `global_settings.py` is the central configuration file of the IOW ESM.
This file has to keep its name and its location, which is the folder `input` in the root directory
on your target machine.

It consists of the following sections.


## Modeller's information

The modeller's section contains your personal information.
Some of these information can be found later on in some output files, such that your work can be related to you.

This section might look like:

``` python

####################################################
# Global settings for the IOW-ESM model run        #
####################################################

###################################
# STEP 1: Info about the modeller #
###################################
modeller        = "Your Name"                                                   # string, name of the modeller who is responsible
email           = "your.name@io-warnemuende.de"                                 # string, contact of the responsible modeller
institution     = "Leibniz Institute for Baltic Sea Research Warnemunde (IOW)"  # string, name of the institute

```


## Run information

The next sections determines the run you want to perform.
Especially important is the `run_name` variable. 
This determines the folder, where you will find your results in the `output` folder in the root directory
on your target machine.
The hotstart files of your run are also stored folder named `run_name` in the `hotstart` folder in the root directory
on your target machine.

Another important configuration are the `init_date` and `final_date` variables.
They determine the running period and they must be in the "YYYYMMDD" format, e.g. "20220324" for the 24th of March in 2022.
The model will be cold-started at the `init_date` if there are no hotstart files present.
(If there are hotstart files, the model will start from the last common hotstart date for all models.)
The model will then run until it reaches the `final_date` unless it crashes in the meantime.

The `debug_mode` determines which executables are used. 
For each model there is a debug and a production (or release) version available.
Usually you use here `False` which refers to the production executables.

This section in the `global_settings.py` might look like:

``` python
###############################
# STEP 2: Info about the run  #
###############################
run_name        = "TEST_RUN"                # string without space, name of the current run
run_description = "run for a first test"    # string, description: what is this run good for?
init_date       = "19800101"                # string, date when model is/was cold-started (YYYYMMDD) 
final_date      = "20100101"                # string, when will the model run finally end? (YYYYMMDD) 
debug_mode      = False                     # boolean, whether or not to use executables compiled with debugging options (slow)
```


## Time step information

TODO: Add further description here...

``` python
#################################################
# STEP 3: Time stepping info                    #
#################################################
coupling_time_step = 600               # integer, time step when fluxes are calculated and exchanged (s)
run_duration = "1 month"               # string, duration of one model run (day/days, month/months, year/years)
runs_per_job = 1                       # how many runs will be done in one job script
```


## Optional settings