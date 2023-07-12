# Coupling concept


One basic problem when dealing with regional climate models system is that the individual components (atmosphere, ocean, land etc.) 
are described by different models (realized as computer programs) that act on different grids, see  {numref}`Fig. {number} <fig-grids>` and {numref}`Fig. {number} <fig-grids1D>`.

Still, the components have to be coupled in order communicate their state to each other and exchange fluxes as given by nature itself.


```{figure} ../figures/grids.png
---
height: 300px
name: fig-grids
---
Overlaying grids of atmospheric and ocean model for the Baltic Sea
```

```{figure} ../figures/grids1D.png
---
height: 150px
name: fig-grids1D
---
Abstraction of figure {numref}`Fig. {number} <fig-grids>` in one spatial horizontal dimension. Bottom model can support different surface types as water (blue) and ice (white).
```

To exemplify this problem let us consider the calculation of a flux of something from the atmosphere to the bottom.
Usually, if the flux depends on the state of the ocean, some state variables have to be communicated first to the atmosphere.
Since the atmospheric grids are normally larger, the information has to be averaged (weighted by areas) over several bottom cells, 
over different surface types, see {numref}`Fig. {number} <fig-conservative_mapping1>`.


With this averaged state information and its own internal state, the atmospheric model can now calculate the flux as a field on the atmospheric grid.
It is noteworthy that the flux cannot be calculated for the different surface types differently, since the atmospheric model does not know about that (at least not without changing the code significantly).
Finally, the flux field then has to be redistributed on the bottom cells (again in a area-weighted manner such that flux variable is overall conserved), 
see {numref}`Fig. {number} <fig-conservative_mapping2>`.
Since the flux is only calculated from averaged information and not surface-type-dependent, this approach locally not consistent and can become inaccurate. 
This is especially true if many bottom grid cells are covered by one atmospheric grid cell.


```{figure} ../figures/conservative_mapping1.png
---
height: 150px
name: fig-conservative_mapping1
---
Average of ocean's state variables communicated to the atmosphere.
```

```{figure} ../figures/conservative_mapping2.png
---
height: 150px
name: fig-conservative_mapping2
---
Calculation of fluxes in the atmospheric model and remapping on to the ocean's grid.
```


## Current implementation

### Available models

At present, the following components can be coupled in the IOW ESM:
* COSMO-CLM atmospheric model
* MOM5.1 ocean model (including (a) the ERGOM ecosystem model and (b) a dynamic ice model, coupled internally via the FMS coupler)

By its design it is modular, so more models will follow in future that can be interactively coupled together.
