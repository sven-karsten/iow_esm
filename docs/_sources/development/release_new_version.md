# Release of a new version

## Release of the subcomponents

### Test your changes

As soon as you have changed something be sure that these changes are working correctly.
In the best case your changes are backward compatible and still work with older setups.
If you introduce breaking changes it should be clearly noted in the Readme of the subcomponent and of the main repository.


### Update the Readme

Go to each sub compoment that has changed since the last version. 
Let's say for subcomponent `componentA` we want to release a new version `X.XX.XX`. 
Then update the corresponding `Readme.md` by adding a block (on top of the last version) like

``` markdown
## X.XX.XX (latest release)

| date        | author(s)   | link      |
|---          |---          |---        |
| YYYY-MM-DD  | AB          | [X.XX.XX](https://git.io-warnemuende.de/iow_esm/componentA/branch/X.XX.XX)     | 

<details>

### changes
* changed something
* fixed this
* added that
    
### dependencies
* depends on something 
  
### known issues
* shows some strange behavior in case X

### tested with
* intensively tested on some machine with some setup

</details>
``` 

Here `YYYY-MM-DD` should be the current date and `AB` should be your initials. 
The link to the git repository should be pointing to the specific branch of this release.
This branch is created in the next step.


### Create a release branch

After you are sure that all your changes are in their final state, commit them (the updated `Readme.md` as well) and create a branch named `X.XX.XX` on this commit.
After you have pushed that branch to the repository it should be reachable via the link you have put into the Readme.


## Update the main repository

### Update the Readme

Update the `Readme.md` file of the main repository in the same fashion as it is described for the subcomponents.
Note briefly the biggest changes of the subcomponents and also changes of the main repository's scripts, if available.

The next step is to commit your changes and create a branch for the new version of the main repository.
Importantly, the creation of the branch is not done manually but rather by editing and subsequently executing the shell script `release.sh`, as described in the next section.


### Update the script release.sh

In the main repository there is the shell script `release.sh`.
Here you can specify the `new_version` number of the IOW ESM, a specific `commit_message` and the `origins` with the corresponding version numbers of the subcomponents.
After you have made your changes commit them into the master branch.
Subsequently execute the shell script via

``` bash
./release.sh
```

This creates a branch named as the new version and an updated `ORIGINS` file is committed into that branch.
After you are sure that everything is correct, push this branch to the remote repository and the new version is released.