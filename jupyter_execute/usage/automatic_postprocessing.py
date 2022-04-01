#!/usr/bin/env python
# coding: utf-8

# # Automatic postprocessing
# 
# ## Default processing of raw output
# 
# 
# If all of your models provide a postprocess task called `process_raw_output` and these tasks should be performed after a run has successfully finished you can add to `input/global_settings.py` the following lines
# 
# ``` python
# 
# ################################################
# # STEP 8 (optional): Start postprocessing after run has finished #
# ################################################
# process_raw_output = True
# 
# ```
# 
# This will call the script `postprocess.sh` of the task for each model in the following way
# ``` bash
# ./postprocess.sh  <model-output-dir> <current-start-date> <current-end-date>
# ```
# 
# where 
# * model-output-dir = "IOW_ESM_ROOT/output/run_name/model"
# * current-start-date = the start date of the _current_ run
# * current-end-date = the end date of the _current_ run
# 
# ## Perform specific tasks automatically
# 
# 
# ``` python
# 
# ################################################
# # STEP 8 (optional): Start postprocessing after run has finished #
# ################################################
# process_raw_output = False
# postprocess_tasks = {   
#     "MOM5_Baltic" : ["process_raw_output", "prepare_for_validator"],
#     "CCLM_Eurocordex" : ["process_raw_output"]
# }
# 
# ```
# 
# Note that the tasks are preformed in the order they appear in the lists given in the dictionary.
# 
# ## Perform specific tasks with specific arguments automatically
# 
# ``` python
# 
# ################################################
# # STEP 8 (optional): Start postprocessing after run has finished #
# ################################################
# process_raw_output = False
# postprocess_tasks = {   
#     "MOM5_Baltic" : { "process_raw_output" : {},
#                       "prepare_for_validator" : {"run_name" : "some_other_name",
#                                                  "init_date" : "19790101",
#                                                  "end_date" : end_date
#                                                 }
#                     },
#     "CCLM_Eurocordex" : ["process_raw_output"]
# }
# 
# ```
# 
# An empty dict means to use the defaults, i.e.
# * "run_name" = run name as specified in `input/global_settings.py`
# * "init_date" = start date of _the current_ run
# * "end_date" = end date of _the current_ run
# 
