# Automatic synchronization to another target

## The main principle

The _target_, where the data should be synchronized to, executes a periodic `rsync` command
to copy the data from the _source_ machine, where the data is/has been produced.
Thus it is necessary that you can log from the target machine (e.g. IOW server) to the source machine (e.g. HLRN super computer).
The synchronisation target must be one of the keywords in your `DESTINATION` file.

In order to avoid frequent password requests it is beneficial to set up the target machine properly, as it is described in the following section.


## Set up the target machine

Add the following line to `~/.bashrc`
```bash
export SSH_AUTH_SOCK=~/.ssh/ssh-agent.$HOSTNAME.sock
``` 

and then update your session via executing
```bash
source ~/.bashrc
``` 

Create a screen on the target with
``` bash
screen -S ssh-agent
```

Now you are attached to that screen and you can run an SSH agent inside via
``` bash
ssh-add -l 2>/dev/null >/dev/null
if [ $? -ge 2 ]; then
  ssh-agent -a "$SSH_AUTH_SOCK" >/dev/null
fi
```

Then detach from that screen via 
``` bash
screen -d ssh-agent
```

Subsequently add the private key of your source machine to the agent, e.g.
``` bash
ssh-add ~/.ssh/id_rsa_hlrn
```
where the `id_rsa_hlrn` should be replaced by your chosen key.

Now you have to enter the password once and as long as the `ssh-agent` screen is running
there is no need to enter the password again.


## Activate the synchronization

### Command-line interface

Run the model in the root directory e.g. via
``` bash
./run.sh hlrng sync_to=phy-10
``` 

or if the model should be prepared before running 
``` bash
./run.sh hlrng prepare-before-run sync_to=phy-10
``` 
where this order of arguments is mandatory.

The synchronisation target, in this case `phy-10`, must be one of the keywords in your `DESTINATION` file.

In order to start the synchronization manually after the model run already started, you can execute e.g.
``` bash
./sync_from_one_target_to_another.sh hlrng phy-10
```


### GUI

With the graphical user interface you can choose via a dropdown menu in the "Run the model" frame to which target the synchronization should happen.
As soon as you run the model the synchronization is started and repeated every hour.
If the field is empty, no synchronization is performed.


## Stop synchronization

Currently you have to stop the synchronization manually by executing on the synchronization target
``` bash
screen -r rsync-hlrnb_CCLM-phy-10_CCLM
```
and a subsequent canceling via hitting `Ctrl + C` on the keyboard.

