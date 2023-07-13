(usage:new-target-machines)=
# Add new target machines

In order to add a new target machine the following steps have to be performed:

1. Add a new keyword and the corresponding remote directory to your `DESTINATIONS` file.
Let's call the new target keyword in this example `new-target`.
Then the new line in your `DESTINATIONS` file could look like `new-target user@new-target:/data/user/IOW_ESM`.
Add `new_target` to the `AVAILABLE_TARGETS` file in the root directory.

2. Add a build script for each component that should be build on the new target. 
For the example this must be called `build_new-target.sh`.
In general the name has to be `build_` followed by the keyword and `.sh`.
In most cases you can probably copy the build script from another target and simply adapt the loaded modules or paths.
You have to find out on your own which modification are to be done here.

3. Add a script that starts the build script on the target. 
For the example this must be called `start_build_new-target.sh`.
In general the name has to be `start_build_` followed by the keyword and `.sh`.
On some targets the build is performed using the queuing system on others it can be performed on directly the login node.
Find out which is true for your new target.
The existing `start_build_haumea.sh` is an example for using the queue, whereas `start_build_hlrng.sh` is an example for direct compilation on the login node.

4. Add a machine settings python module `machine_settings_new_target.py` to the directory `scripts/run`.
Here you have to specify how MPI and the queueing system are used on the new target.
As a template you can use the examples `machine_settings_hlrn.py` (Intel-MPI + SLURM) and `machine_settings_haumea.py` (OpenMPI+SLURM).