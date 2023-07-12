(usage:define_parallelization_layout)=
# Defining the parallelization layout

Parallelization is defined for each individual model, as described in the following subsections.
The parallelization of the entire model system will then be automatically derived from these individual settings.

To get a parallelization that fits yourmachine and model system, please take the following
steps:
1. Specify the parallelization layout of individual models as described in the component-specific subsections.
2. Go to the folder scripts/run where you will find job script templates `jobscript_???` for dierent supercomputers and their job submission systems. Find an appropriate one for your supercomputer (or [create it](usage:setting_up_jobscript)), adjust the runtime.
3. Go to the file `input/global_settings.py` and specify the filename of your template there (`jobscript_template = '???'`)
4. Also in `input/global_settings.py`, fill in the number of cores per node to use.
5. Go to the folder scripts/prepare and run `python3 create_jobscript.py`, which will take the supercomputer-specific job script defined in `input/global_settings.py` and produce a file `scripts/run/jobscript` by filling in in the required number of cores and nodes for the full coupled model.
6. Later you may want to check whether the parallelization is ecient, i.e. whether none of the components has too much idle time waiting for the others. Then you may increase or decrease the parallelization of individual subcomponents.

## Defining CCLM parallelization

CCLM uses a rectangular parallelization in X and Y direction, where X and Y are the zonal and meridional direction on the rotated lat-lon grid. 
The number of rectangles in each direction can be specified in the file `input/CCLM_???/INPUT_ORG`

## Defining MOM5 parallelization

MOM5 uses a rectangular decomposition defined in `input/MOM5_???/input.nml`. 
A file named `input/MOM5_???/mask_table` can be used to define which of the rectangles contain land points only and therefore require no MPI task to be allocated for them. 
MOM5 comes with a tool to find out parallelization layouts which optimize the relative fraction of these land domains.

