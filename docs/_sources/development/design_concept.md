# Design and concept

## Source-code managment

```{figure} ../figures/project_structure.png
---
height: 400px
name: project_structure
---
Visualization of the individual repositories within the IOW ESM package.
```


## Versioning scheme

```{figure} ../figures/version_management.png
---
height: 500px
name: version_management
---
Visualization of the relation between diffferent versions of the individual components and the whole package (connected via `main` repository).
```

Relation of individual versions and the version of the whole package is stored in the `ORIGINS` file, e.g. for the IOW ESM 1.03.00 this looks like:

``` bash
components/OASIS3-MCT       https://git.io-warnemuende.de/iow_esm/components.oasis3-mct.git         1.00.01
components/flux_calculator  https://git.io-warnemuende.de/iow_esm/components.flux_calculator.git    1.02.00
components/MOM5             https://git.io-warnemuende.de/iow_esm/components.mom5.git               1.01.00
components/CCLM             https://git.io-warnemuende.de/iow_esm/components.cclm.git               1.00.03
tools/I2LM                  https://git.io-warnemuende.de/iow_esm/tools.i2lm.git                    1.00.01
postprocess                 https://git.io-warnemuende.de/iow_esm/postprocess.git                   1.02.00
```

For the development branch (i.e. the master branch) the version numbers are omitted and all components are taken from the head of their corresponding master branches.