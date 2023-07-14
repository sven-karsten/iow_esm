# IOW Earth system model documentation

This is the main documentation for the IOW earth system model (ESM) project. 

In the following the intended concept of  working with IOW ESM software package is described.
Subsequently, the reader is lead to a step-by-step description of how to start using the package.

For the scientific background of this model please read {cite}`karsten2023` and [](background:coupling-concept).

**Note that the documentation is work in progress and by far not complete yet (see {ref}`todos`)!**


## Working concept

Before working with the IOW ESM it is important to understand the intended working concept.
The basic idea for the workflow is that you clearly can separate the place where you store and/or develop the source code and where the model is running.
The model will potentially run on many different machines such as supercomputers.
However, the development should take place only in one central place to avoid the mess of having locally different and incompatible versions at different places.

This philosophy leads to a one-to-many relation as depicted in {numref}`Fig. {number} <working_concept>`.

```{figure} ./figures/working_concept.png
---
height: 500px
name: working_concept
---
Visualization of the intended working concept
```

In other words there is one place where you as a developer work, this might be your personal computer or an IOW server.
From this place, which can be thought of as a _control center_ you can develop the code, start a built and start simulations with subsequent post-processing.
On the hand there are many places where the model can work which might be any server suitable to handle the planned simulations.
These servers are refered to as _targets_ or _destinations_ in the following.
The great advantage is, that you can always keep the sources on _all_ targets in sync with your single personal working place.


## Getting started

Be sure you have read the `Readme` at https://git.io-warnemuende.de/iow_esm/main and fulfill all the prerequisites.
You might then go to [](getting_started:first_use) to set up everything and perform your first run.


```{bibliography}
:style: unsrt
```

## Documentation history 

### Authors

* SK      (sven.karsten@io-warnemuende.de)
* HR      (hagen.radtke@io-warnemuende.de)


### Versions

#### 0.01.00 (in preparation)

| date        | author(s)   | 
|---          |---          |
| 2023-07-14  | SK, HR          |

<details>

##### changes
* initial version of jupyter-book documentation
* not complete yet

##### compatibility
* to iow_esm/main version [1.04.00](https://git.io-warnemuende.de/iow_esm/main/src/branch/1.04.00)
  
</details>