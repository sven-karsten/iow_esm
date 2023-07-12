(background:details_on_fluxes)=
# Details on individial fluxes

This section contains physical details about the fluxes that can be calculated in the flux calculator executable.
All fluxes are calculated positive upward, such that e.g. precipitation is always negative.

## List of variables that determine the fluxes

Fluxes may depend on the following variables:
| code | symbol         | description                                                 | provided by      | unit    |
| ---- | -------------- | ----------------------------------------------------------- | ---------------- | ------- |
| ALBE | $\alpha$       | surface albedo                                              | ocean/land model | 1       |
| AMOI | $a_{moisture}$ | turbulent diffusion coefficient for moisture                | atmos model      | 1       |
| AMOM | $a_{momentum}$ | turbulent diffusion coefficient for momentum                | atmos model      | 1       |
|      | $c_d$          | specific heat capacity of dry air at constant pressure      | 1005.0           | J/kg/K  |
|      | $\Delta H_v$   | latent heat of vaporization                                 | 2.501e6          | J/kg    |
|      | $\Delta H_f$   | latent heat of freezing                                     | 0.334e6          | J/kg    |
|      | $\Delta H_s$   | latent heat of sublimation                                  | 2.835e6          | J/kg    |
| FARE | $f_{area}$     | area fraction of this bottom type (between 0 and 1)         | ocean/land model | 1       |
| FICE | $f_{ice}$      | ice area fraction (between 0 and 1)                         | ocean/land model | 1       |
|      | $g$            | graviational acceleration                                   | 9.81             | m/s     |
| PATM | $p_a$          | pressure at lowest atmospheric level                        | atmos model      | Pa      |
| PSUR | $p_s$          | surface pressure                                            | atmos model      | Pa      |
| QATM | $q_{v,a}$      | specific water vapor content (lowest atmospheric grid cell) | atmos model      | kg/kg   |
|      | $q_{v,s}$      | specific water vapor content (at sea / soil surface)        | aux. variable    | kg/kg   |
|      | $R_d$          | dry air gas constant                                        | 287.05           | J/kg/K  |
|      | $R_v$          | water vapor gas constant                                    | 461.51           | J/kg/K  |
|      | $\sigma$       | Stefan-Boltzmann constant                                   | 5.67e-8          | W m$^{-2}$ K$^{-4}$ |
| TATM | $T_a$          | air temperature (lowest atmospheric grid cell)              | atmos model      | K       |
| TSUR | $T_s$          | surface temperature                                         | ocean/land model | K       |
| UATM | $u_a$          | zonal velocity (lowest atmospheric grid cell)               | atmos model      | m/s     |
|      | $u_{min,evap}$ | minimum velocity for CCLM evaporation calculation           | 0.01             | m/s     |
| VATM | $v_a$          | meridional velocity (lowest atmospheric grid cell)          | atmos model      | m/s     |

## Auxiliary variables for fluxes

### Specific water vapor content (at sea/soil surface)

This auxiliary variable ($q_{v,s}$, in kg/kg) describes the specific water vapor content in the air immediately above the surface, i.e. in the logarithmic boundary layer. 

It is used further in the following routines:
|                 | file                               | routine               | variable                         |
| --------------- | ---------------------------------- | --------------------- | -------------------------------- | 
| flux calculator | `flux_lib/mass/flux_mass_evap.F90` | `flux_mass_evap_cclm` | `specific_vapor_content_surface` |

Here is how it is calculated:

#### COSMO-CLM routine for specific water vapor content at sea/ice surface

|                 |                                                                               |               |
| --------------- | ----------------------------------------------------------------------------- | ------------- |
| **requires**    | $f_{ice}$, $p_s$, $R_d$, $R_v$, $T_s$                                         |               |
| **source**      | COSMO-CLM subroutine `initialize_loop`                                        | (`lmorg.f90`) |
| **references**  | \cite{Lowe1977}, \cite{Murray1967}                                            |               |
| **calculation** | over water / over ice:                                                        |               |
|                 | $\: \alpha = 17.2693882 \, / \, \alpha = 21.8745584$                          | 1             |
|                 | $\: T_2 = 35.86 \, / \, T_2 = 7.66$                                           | K             |
|                 | always:                                                                       |               |
|                 | $T_1 = 273.16$                                                                | K             |
|                 | $p_0 = 610.78$                                                                | Pa            |
|                 | $p_{sat} = p_0 \, \exp \left( \alpha \frac{T_s - T_1}{T_s - T_2} \right)    $ | Pa            |
|                 | $\mathbf{q_{v,s}} = \frac{ \frac{R_d}{R_v} p_{sat}}{p_s - \left(1-\frac{R_d}{R_v}\right) p_{sat}}$ | kg/kg |

## Mass fluxes

### Evaporation/condensation mass flux of water

The surface moisture flux (kg/m$^2$/s) is used further in the following routines:

|                 | file                               | routine                  | variable                         |
| --------------- | ---------------------------------- | ------------------------ | -------------------------------- | 
| COSMO-CLM       | `src_conv_tiedtke.f90`             | `organize_conv_tiedtke`  | `-qvsflx`                        |
| COSMO-CLM       | `src_diagbudget.f90`               | `organize_diagbudget`    | `-qvsflx`                        |
| COSMO-CLM       | `src_integrals.f90`                | `check_qx_conservation`  | `-qvsflx`                        |
| flux calculator | `flux_heat_latent.f90`             | `flux_heat_latent_water` | `flux_mass_evap`                 |
| flux calculator | `flux_heat_latent.f90`             | `flux_heat_latent_ice`   | `flux_mass_evap`                 |
  
Here is how it is calculated:

#### COSMO-CLM routine for evaporation/condensation mass flux
|                 |                                                                                                |                         |
| --------------- | ---------------------------------------------------------------------------------------------- | ----------------------- |
| **requires**    | $a_{moisture}$, $p_s$, $q_{v,a}$, $q_{v,s}$, $R_d$, $R_v$, $T_s$, $u_a$, $u_{min,evap}$, $v_a$ |                         |
| **source**      | COSMO-CLM subroutine `slow_tendencies`                                                         | (`slow_tendencies.f90`) |
| **calculation** | $\tilde{T} = T_s \left(1 + \left(\frac{R_v}{R_d}-1\right) q_{v,s} \right)$                     | K                       |
|                 | $\mathrm{abs}(\vec{u}) = \sqrt{u_a^2+v_a^2}$                                                   | m/s                     |
|                 | $flux_{air} = a_{moisture} \max(\mathrm{abs}(\vec{u}),u_{min,evap}) \frac{p_s}{R_d \tilde{T}}$ | kg m$^{-2}$ s$^{-1}$    |
|                 | $\mathbf{flux\_mass\_evap} = flux_{air} \cdot (q_{v,s} - q_{v,a})$                             | kg m$^{-2}$ s$^{-1}$    |
| **explanation** | First we calculate the temperature $\tilde{T}$ at which dry air at the surface would show the same energy $p\cdot V$ as the moist air which is there now. | |
|                 | We then calculate a mass flux of air coming into contact with the surface. Evaporation is then calculated assuming that this air adjusts its water vapor content to the one at the surface.  | |

## Heat fluxes

### Latent heat flux

The latent heat flux (W/m$^2$) is used further in the following routines:

|                 | file                               | routine                  | variable                         |
| --------------- | ---------------------------------- | ------------------------ | -------------------------------- | 
| COSMO-CLM       | `near_surface.f90`                 | `near_surface`           | `-lhfl_s`                        |
| COSMO-CLM       | `send_fld.f90`                     | `send_fld`               | `-lhfl_s`                        |
| COSMO-CLM       | `src_conv_ifs.f90`                 | `organize_conv_ifs`      | `-lhfl_s`                        |

Here is how the fluxes can be calculated:

#### COSMO-CLM routine for latent heat flux over water

|                 |                                                                                                |                         |
| --------------- | ---------------------------------------------------------------------------------------------- | ----------------------- |
| **requires**    | $\Delta H_v$, `flux_mass_evap`                                                                 |                         |
| **source**      | COSMO-CLM subroutine `slow_tendencies`                                                         | (`slow_tendencies.f90`) |
| **calculation** | $\mathbf{flux\_heat\_latent} = \Delta H_v \cdot \mathtt{flux\_mass\_evap}$                     | J m$^{-2}$ s$^{-1}$     |

#### COSMO-CLM routine for latent heat flux over ice

|                 |                                                                                                |                         |
| --------------- | ---------------------------------------------------------------------------------------------- | ----------------------- |
| **requires**    | $\Delta H_v$, `flux_mass_evap`                                                                 |                         |
| **source**      | COSMO-CLM subroutine `slow_tendencies`                                                         | (`slow_tendencies.f90`) |
| **calculation** | $\mathbf{flux\_heat\_latent} = \Delta H_s \cdot \mathtt{flux\_mass\_evap}$                     | J m$^{-2}$ s$^{-1}$     |

### Sensible heat flux

The sensible heat flux (W/m$^2$) is used further in the following routines:

|                 | file                               | routine                  | variable                         |
| --------------- | ---------------------------------- | ------------------------ | -------------------------------- | 
| COSMO-CLM       | `near_surface.f90`                 | `near_surface`           | `-shfl_s`                        |
| COSMO-CLM       | `send_fld.f90`                     | `send_fld`               | `-shfl_s`                        |
| COSMO-CLM       | `src_conv_ifs.f90`                 | `organize_conv_ifs`      | `-shfl_s`                        |

Here is how the fluxes can be calculated:

#### COSMO-CLM routine for sensible heat flux

|                 |                                                                                                |                         |
| --------------- | ---------------------------------------------------------------------------------------------- | ----------------------- |
| **requires**    | $a_{moisture}$, $p_a$, $p_s$, $q_{v,s}$, $R_d$, $R_v$, $T_s$, $u_a$, $u_{min,evap}$, $v_a$     |                         |
| **source**      | COSMO-CLM subroutine `slow_tendencies`                                                         | (`slow_tendencies.f90`) |
| **calculation** | $\tilde{T} = T_s \left(1 + \left(\frac{R_v}{R_d}-1\right) q_{v,s} \right)$                     | K                       |
|                 | $\mathrm{abs}(\vec{u}) = \sqrt{u_a^2+v_a^2}$                                                   | m/s                     |
|                 | $flux_{air} = a_{moisture} \max(\mathrm{abs}(\vec{u}),u_{min,evap}) \frac{p_s}{R_d \tilde{T}}$ | kg m$^{-2}$ s$^{-1}$    |
|                 | $ EF = \left(\frac{p_s}{p_a}\right)^\frac{R_d}{cp_d}$                                          | 1                       |
|                 | $\mathbf{flux\_heat\_sensible} = flux_{air} \cdot cp_d \cdot \left(T_g - T_a \cdot EF \right)$ | kg m$^{-2}$ s$^{-1}$    |
| **explanation** | The first part until $flux_{air}$ is identical to the CCLM mass flux of evaporation.           |                         |
|                 | $EF$ is the Exner function which calculates the ratio $T/\theta$ between local temperature at local pressure and potential temperature at a reference pressure. In the original routine two Exner factors were calculated for pressure in the lowest atmospheric level and surface pressure, each with a reference pressure of 1e5~Pa, and divided by each other, here the procedure is simplified. The Exner factor $EF$ converts the temperature of the lowest atmospheric level $T_a$ to temperature at the surface.  | |

## Momentum fluxes

### Upward flux of horizontal momentum

The upward flux of horizontal momentum (=shear stress, N/m$^2$) is used further in the following routines:

|                 | file                               | routine                  | variable                         |
| --------------- | ---------------------------------- | ------------------------ | -------------------------------- | 
| COSMO-CLM       | `near_surface.f90`                 | `near_surface`           | `-umfl_s`, `-vmfl_s`             |
| COSMO-CLM       | `send_fld.f90`                     | `send_fld`               | `-umfl_s`, `-vmfl_s`             |

Here is how it is calculated:

#### COSMO-CLM routine for eastward momentum flux

|                 |                                                                                                |                         |
| --------------- | ---------------------------------------------------------------------------------------------- | ----------------------- |
| **requires**    | $a_{momentum}$, $p_s$, $q_{v,s}$, $R_d$, $R_v$, $T_s$, $u_a$, $v_a$                            |                         |
| **source**      | COSMO-CLM subroutine `slow_tendencies`                                                         | (`slow_tendencies.f90`) |
| **calculation** | $\tilde{T} = T_s \left(1 + \left(\frac{R_v}{R_d}-1\right) q_{v,s} \right)$                     | K                       |
|                 | $\mathrm{abs}(\vec{u}) = \sqrt{u_a^2+v_a^2}$                                                   | m/s                     |
|                 | $flux_{air} = a_{momentum} \mathrm{abs}(\vec{u}) \frac{p_s}{R_d \tilde{T}}$ | kg m$^{-2}$ s$^{-1}$    |
|                 | $ EF = \left(\frac{p_s}{p_a}\right)^\frac{R_d}{cp_d}$                                          | 1                       |
|                 | $\mathbf{flux\_momentum\_east} = - flux_{air} \cdot u_a$                                       | kg m$^{-1}$ s$^{-2}$=N/m$^2$ |
| **explanation** | First we calculate the temperature $\tilde{T}$ at which dry air at the surface would show the same energy $p\cdot V$ as the moist air which is there now. |  |
|                 | We then calculate a mass flux of air coming into contact with the surface.                     |                         |
|                 | Momentum transfer is then calculated assuming that this air passes all its horizontal momentum to the surface. |         |
|                 | Horizontal movement of the surface (water currents) is neglected.                              |                         |

#### COSMO-CLM routine for eastward momentum flux
Calculation is completely analog to the previous one.

## Radiation fluxes

Just like precipitation fluxes, radiation fluxes are calculated by the atmospheric model on the atmospheric grid. Unlike precipitation, they do however vary between different bottom model cells with a different temperature and albedo. 
We will outline here how this redistribution works.

Two types of radiation are distinguished by their wavelength, which are shortwave and longwave radiation. 
For each of these types, each bottom grid cell can have one albedo value, or possibly several different ones e.g. for different ice classes which share the area of the ocean grid cell. 
The average albedo for the atmospheric grid cell $i$, $\alpha^a_i$, can therefore be calculated as follows:

$
\begin{aligned}
  \alpha^a_{i,shortwave} &= \sum\limits_{m=1}^M \sum\limits_{j=1}^{B_m} \frac{\left| g^a_i \tilde{\cap} g^{b,m}_j \right|}{\left| g^a_i \right|} \sum\limits_{c=1}^{C_m} \alpha^{b,m}_{c,shortwave} \cdot f^{b,m}_c(j) \\
	\alpha^a_{i,longwave} &= \sum\limits_{m=1}^M \sum\limits_{j=1}^{B_m} \frac{\left| g^a_i \tilde{\cap} g^{b,m}_j \right|}{\left| g^a_i \right|} \sum\limits_{c=1}^{C_m} \alpha^{b,m}_{c,longwave} \cdot f^{b,m}_c(j)
\end{aligned}
$

Here, $m$ is the index of the bottom model chosen, 
$j$ is its grid cell index, 
the numerator in the fraction gives the area of intersection between atmospheric and bottom model grid cells where they are bidirectionally coupled, 
the denominator normalizes this area to the full area of the atmospheric grid cell, 
$c$ is the class index (=ice class, soil type) used in bottom model $m$, 
$\alpha^{b,m}_{c}$ is the albedo defined for this class in the bottom model, and  
$f^{b,m}_c(j)$ is the area fraction of the bottom grid cell covered by this class.

Black-body radiation is emitted from the surface according to its temperature and longwave albedo and can be calculated with the help of the Stefan-Boltzmann constant $\sigma$:

$bbr = (1-\alpha_{longwave}) \sigma T^4$

A similar horizontal averaging gives an average value for the atmospheric grid cell:

$
bbr^a_{i,longwave} = \sum\limits_{m=1}^M \sum\limits_{j=1}^{B_m} \frac{\left| g^a_i \tilde{\cap} g^{b,m}_j \right|}{\left| g^a_i \right|} \sum\limits_{c=1}^{C_m} \left(1-\alpha^{b,m}_{c,longwave} \right) f^{b,m}_c(j) \sigma \left(T^{b,m}(j)\right)^4 
$

From this value, we can calculate an effective radiative bottom temperature for the atmospheric grid cell:

$
T^a_{i,longwave} = \sqrt[4]{\frac{bbr^a_{i,longwave}}{(1-\alpha^a_{i,longwave}) \sigma}}
$

We use this temperature for the radiative flux calculation to make sure the emitted black-body radiation is exact.

After calculating the downward radiative fluxes (both shortwave and longwave) by the atmospheric model, we pass these to the flux calculator. The flux calculator will then calculate the upward radiative fluxes on the exchange grid, using the spatially detailed information on albedo and surface temperature. This procedure ensures that also the average upward fluxes over the atmospheric grid cell are exactly identical between (a) the flux calculator and (b) the atmospheric model which calculate them independently.
In practice, it works like this:
* Bottom models send surface temperature.
* flux calculator calculates and sends blackbody radiation.
* CCLM receives surface temperature and blackbody radiation in <br>
        `lmorg -> initialize_loop -> receive_fld`
* CCLM calculates all radiation components in <br>
        `lmorg -> organize_physics('compute',...) -> organize_radiation`
* CCLM sends radiation fluxes and other variables in <br>
	      `lmorg -> organize_physics('compute',...) -> communicate_with_flux_calculator`
* flux calculator calculates and sends all other fluxes.
* CCLM receives these fluxes in the same routine.
* Bottom models receive all fluxes.

