(usage:setting_up_jobscript)=
# Setting up your jobscript template

The jobscript template is a template for the slurm script that is submitted to run your job.
In order to adapt it to your needs you will most probably modify the example templates in the example setups.
However, certain lines should not be changed.


## Personal adaptions

``` bash
#SBATCH --job-name=<your_favorite_name>
#SBATCH -t dd-hh:mm:ss
#SBATCH --account=<project/user> 
#SBATCH -p <partition>
```

Here you may enter whatever is needed by you.

## Leave unchanged

### Automatically replaced 

``` bash
#SBATCH --nodes=_NODES_
#SBATCH --ntasks=_CORES_
#SBATCH --tasks-per-node _CORESPERNODE_
```

These lines will be replaced when the actual jobscript is created.

### Necessary

``` bash
#SBATCH --distribution=block,Pack

export SLURM_CPU_BIND=none

python3 run.py
```

These lines are required that the model runs efficiently.
The last line is actually start of the run.