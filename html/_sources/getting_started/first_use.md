(getting_started:first_use)=
# First use

First be sure that you have read the `Readme` at https://git.io-warnemuende.de/iow_esm/main and that you fulfill all the prerequisites.


## Key agent recommended

Note that it is strongly recommended to use a [key agent](https://www.ssh.com/academy/ssh/agent) for connecting to the target servers.
Otherwise you will have to type in your account password very often.
Assuming you have generated RSA key pairs for the target machines as described in the [phywiki](http://phywiki.io-warnemuende.de/do/view/Server/GenerateRsakeys) or as required for the HLRN, you can start a key agent via

``` bash
eval `ssh-agent`
ssh-add ~/.ssh/<private-key>
```

where the `<private-key>` should be the private key generated for the desired target.


## Working with the GUI

If you would like to work with graphical user interface you have to start corresponding python script from a shell
(`MSYS2` on Windows or `bash` on Linux) by executing the following in the root directory (where this `Readme.md` is located)

``` bash
/path/to/python iow_esm.py
```

The shell where this is executed should be the same as where the key agent is running.

If you use the GUI, it will guide you step by step throught the first steps that are described in the following for the command line application.
However, you can and should still use this description as a roadmap.


## First steps with the command line interface


### Get the component sources

After cloning this repository to your local machine you have to get the component repositories as well.
For this purpose there is the bash script `clone_origins.sh` which uses the file `ORIGINS`. 
The one you have cloned right now contains all available components.
**This file should not be edited and commited unless you really know what you are doing.**
By executing in the root directory (where this `Readme.md` is located)

``` bash
./clone_origins.sh
```

you clone all individual components which have their own repositories to your local machine.
If there will be some you don't need you can later remove them. 
However, be sure that you can still build and run the model properly.
For instance, if you want to run the models uncoupled from the other you still have to build the OASIS coupler first, 
see `documentation/developers_documentation.pdf` for details.

Note that depending on your choice from above, i.e. you cloned the main project as a user or as a developer, 
you will clone the latest release branches or the master (development) branches, respectively.
However, if you started as user but decide later to develop you can always check out the individual master branches manually.


### Configure your destinations (targets)

You will not build (or run) the model on your local computer.
Instead you have to specify a destination or a target, where your sources are copied and compiled.
This is done a file `DESTINATIONS` (this name is obligatory). 
Since this file very user-specific it is not part of the repository and *you have to create one.*
However, there is an example `DESTINATIONS.example`, please have a look.
You see that each line consists of two elements.
The first is the *keyword for the target*. This keyword has to match one of the following

* `hlrng`
* `hlrnb`
* `haumea`
* `phy-2`

where 

* `hlrng` refers to the HLRN IV cluster located in Göttingen
* `hlrnb` refers to the HLRN IV cluster located in Berlin
* `haumea` is the cluster of the of the Rostock University
* `phy-2` is one of the IOW's physics department computing servers (**ATTENTION: currently the model is not running here**)

At the moment there are running build scripts only for these targets, which can be found the file `AVAILABLE_TARGETS` as well.
Do not edit or commit this file unless you really know what you are doing.
If you want to add more targets, it will be explained in [Register new destinations](#register-new-destinations).

The second element in a line of `DESTINATIONS.example` corresponds to the *root directory on the target*, the path, where the whole model will be deployed, built and run.
If the path on the target does not exist, it will be created.
Be sure that you have write permissions.
Importantly, the location _must_ have the following format `user@host:/path/to/rootdirectory`.
Both user and host name are use in the script and cannot be omitted although you might have some shortcuts and aliases for your accounts.
**Now it is up to you, to create your own file `DESTINATIONS` in your local root directory, but do not commit it!**
Note that there is also the possibility to give more advanced keywords to run several instances on the same target, see [Advanced destination keywords](#advanced-destination-keywords)


### Build the coupled model for the first time

Each component can be built individually by executing the build scripts in the component's directory, see [Build single components in a different modes and configurations](#build-single-components-in-a-different-modes-and-configurations).
However, for the first build the order is important, since some components of the coupled model depend on each other.
Therefore, you should use the `build.sh` script in the root directory.
If you want to build the model e.g. on the HLRN cluster located in Berlin, you can run, e.g.

``` bash
./build.sh hlrng
``` 

This will build the model on `hlrng` in release mode.
Note that we will stick to this specific target throughout this Readme.
Nevertheless, if you want to work with another target for your first tests, just replace `hlrng` with another valid keyword.
Note further that the first argument is non-optional, whereas there are two others which can be omitted, 
see [Build single components in a different modes and configurations](#build-single-components-in-a-different-modes-and-configurations).


### Deploy dependencies for running (setups)


#### Configure your setups

In order to run the model, you need input files which define a certain setup.
What exactly a setup consits of, you can find out by looking at [Available setups](#available-setups).
The setups you want to use can be registered in a special file named `SETUPS` (this name is obligatory), 
which is in the root directory.
Since this file specific for certain users and individual runs of the model it is not part of the repository and *you have to create one.*
However, there is an example `SETUPS.example`, please have a look.
You see that each line consists of two elements.
The first is the *keyword for the setup*. 
This keyword can be chosen by you almost freely.
It should be unique and a single word without spaces.
In order to update from one or several setups you can call the run script `run.sh` with a second, third, etc. argument representing your setup keys in the `SETUP`.
The files from these setups are then synchronized to the target in the order they appear as arguments.
That is, the last setup will overwrite the ones before if files are overlapping.

The second element of a line in `SETUPS` represents the location of this setup. 
This can be local on your machine or on a remote computer.
Be sure that the remote computer knows your targets and can copy files to them. 


#### Available setups

##### HLRN in Göttingen
You can find an example setup for a MOM5 for the Baltic sea coupled to a CCLM model for the Eurocordex domain under `/scratch/usr/mviowmod/IOW_ESM/setups/MOM5_Baltic-CCLM_Eurocordex/example_8nm_0.22deg/1.00.00`.
The corresponding line in the `SETUPS` file could then look like
`coupled_example user@glogin:/scratch/usr/mviowmod/IOW_ESM/setups/MOM5_Baltic-CCLM_Eurocordex/example_8nm_0.22deg/1.00.00`,
where `user` should be replaced by your user name on the HLRN in Göttingen.
It might be also necessary to add the full domain to the hostname, depending on your ssh configuration.
Other example setups (also for uncoupled runs) can be found in `SETUPS.example` in this directory.

**TODO:** Explain strucutre of the setup folder (= root directoy)


#### Copy setup files to target

After creating the file `SETUPS` you can run in the root directory

``` bash
./deploy_setup.sh hlrng coupled_example
``` 

Before running the model you should have a look at the deployed folders on your target.
Especially you should go to the `input` folder and open the file `global_settings.py`.
Please enter your name and email here.
Moreover you should have a look at the file `jobscript_*`. 
Here you may adjust the account which you will use for running the model.
More details on the preparation of the `input` folder is given in the file `documentation/developers_documentation.pdf`.  
 

### Run the coupled model for the first time

If everything is set up on your remote computer of choice, you can run the model for the first time by executing this in the root directory:

``` bash
./run.sh hlrng
``` 

The first argument of the run script is always the target keyword as specified in your `DESTINATIONS` file.
By executing the run script all files from `scripts` directory will be transferred to the target.

After the scripts are transferred the model is started on the target.

If you use one of the setups from the `SETUPS.example` file, there is no need for further preparation of the coupled model.
However for the general case there is the possibility to run preparation scripts that set up the exchange grid 
and remapping files for the coupler, see `documentation/developers_documentation.pdf`. 
Note that for an uncoupled run there is no need for the preparation.

