(usage:setting_up_jobscript)=
# Setting up your jobscript template

The jobscript template is a template for the script that is submitted/executed to run your job.
In order to adapt it to your needs you will most probably modify the example templates in the example setups.
However, certain lines should not be changed.

Which template file you use is specified in the file `global_settings.py`, see [](usage:setting_up_global_settings).

## Jobscript templates for the slurm queuing system

### Personal adaptions

``` bash
#SBATCH --job-name=<your_favorite_name>
#SBATCH -t dd-hh:mm:ss
#SBATCH --account=<project/user> 
#SBATCH -p <partition>
```

Here you may enter whatever is needed by you.
These settings are in general completely machine specific and therefore please refer to the corresponding documentation, e.g. for the HLRN this is https://www.hlrn.de/doc/display/PUB/Compute+node+partitions.

### Leave unchanged

#### Automatically replaced 

``` bash
#SBATCH --nodes=_NODES_
#SBATCH --ntasks=_CORES_
#SBATCH --tasks-per-node _CORESPERNODE_
```

These lines will be replaced when the actual jobscript is created.

#### Necessary

``` bash
#SBATCH --distribution=block,Pack

export SLURM_CPU_BIND=none
module load <...>

python3 run.py
```

These lines are required that the model runs efficiently and that all necessary modules are loaded.
The last line is actually start of the run.


## Jobscript templates without a queuing system

### Leave unchanged

#### Necessary

``` bash
module load <...>

python3 run.py
```

These lines are required that the model runs efficiently and that all necessary modules are loaded.
The last line is actually start of the run.