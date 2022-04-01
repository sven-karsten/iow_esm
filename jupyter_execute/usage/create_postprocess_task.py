#!/usr/bin/env python
# coding: utf-8

# # Create a new postprocess task
# 
# ## Folder and postprocess.sh
# 
# Go to the folder `postprocess` in your root directory and subsequently to the directory of the model you want to create a task for.
# Here you have to create a folder with the name of the task, e.g. `new_task` (no spaces).
# In this new folder you have to create a script called `postprocess.sh` taking the following arguments
# 
# ``` bash
# out_dir=$1
# from=$2
# to=$3
# ```
# 
# * `out_dir` will be the path to your model's output, e.g. "/path/to/iow_esm/output/MOM5_Baltic".
# * `from` and `to` will be the start and end date, respectively, of the time period your task will process. Both are given in the format YYYYMMDD.
# 
# What the script is then doing is completely up to you.
# It can call bash or python scripts etc.
# There are some auxiliary modules provided in the [auxiliary](https://git.io-warnemuende.de/iow_esm/postprocess/src/branch/master/auxiliary) folder of the [postprocess](https://git.io-warnemuende.de/iow_esm/postprocess) repository. You might use them.
# 
# ## Dependencies (optional but useful)
# 
# In order to keep an overview of the dependencies among the postprocess tasks it is useful to create a file `config.py` that contains list variable `dependencies`, e.g
# 
# ``` python
# dependencies = ["process_raw_output"]
# ```
# 
# Entries in the list are the names of tasks that your new task _directly_ depdends on.
# These dependencies are used by the GUI to list your tasks such that you can execute them in the correct order.
# 
# You can also use this `config.py` file for configuring your task if it is a python script.
# 
