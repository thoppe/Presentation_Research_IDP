### Higher order structure
Phase separations lead to sudden changes in liquid structure.
!(images/macrocharge/example_phase_sep.jpg) <<height:225px;transparent>> Leibler, [Nature 2004](http://www.nature.com/nature/journal/v430/n6999/abs/nature02758.html)
!(images/macrocharge/phase_sep2.jpg) <<height:225px;transparent>> Tanaka, [Phys. Rev. E 2005](http://journals.aps.org/pre/abstract/10.1103/PhysRevE.72.041509)

How do we model _many_ protein-protein interactions? 
Can we *predict* aggregates from experimental structure? 
!(images/macrocharge/1AO6_cartoon.png) <<height:225px;transparent>> Human serum albumin<br>[PDB:1AO6](http://www.rcsb.org/pdb/explore/explore.do?structureId=1ao6)
!(images/macrocharge/1OVA_cartoon.png) <<height:225px;transparent>> Ovalbumin<br>[PDB:1OVA](http://www.rcsb.org/pdb/explore.do?structureId=1ova)
!(images/macrocharge/1W6Z_cartoon.png) <<height:225px;transparent>> Lysozyme<br>[PDB:1W6Z](http://www.rcsb.org/pdb/explore/explore.do?structureId=1w6z)
!(images/macrocharge/3V03_cartoon.png) <<height:225px;transparent>> Bovine Serum Albumin<br>[PDB:3V03](http://www.rcsb.org/pdb/explore/explore.do?structureId=3v03)

====*

## Protein-Protein interactions 

|### Important terms:
Volume exclusion, *Electrostatics*, solvent effects,
Non-specific interactions (London/dispersion forces)

|### Second-order effects?
Non spherical geometries, polarization,
internal conformational energies, ...


_Need a way of validating model._

====*

### Experimental Measurements
Second virial coefficient, $B_{2}$, measurement 
using light scattering at different pH.
!(images/macrocharge/exp_B22_1OVA.png) <<height:550px;>>  Dotted-line: Hard sphere potential.

=====*

### Virial Coefficients

An equation of state expanded in powers of density $\rho$
## $\frac{P}{k_B T} = \rho + B_2(T) \rho^2 + B_3(T) \rho^3 + \ldots$
$B_2$ is the pairwise interaction of _two_ molecules
$B_3$ is the interaction of _three_ molecules, ...
Negative values of $B_2$ often correlate with aggregation.

For rotationally invariant molecules*
##$B_2 = -\frac{1}{2} \int_0^\infty (e^{-U(r)/k_B T} - 1) 4\pi r^2 d r$
_Goal: Develop a realistic pair potential for virial calculation._
&& *Rotationally dependent [calculation](http://thoppe.github.io/Presentation_Research_Macrocharge/#/2/1) integrates over all orientations. For [hard spheres](http://thoppe.github.io/Presentation_Research_Macrocharge/#/5) $B_2 = (2/3)\pi \sigma^3$.

====

# The Process
!(images/macrocharge/human_serum_albumin_1e7h.png) <<transparent>>

Start with the crystallized PDB Structure
_e.g._ Human Serum Albumin [PDB:1A06](http://www.rcsb.org/pdb/explore/explore.do?structureId=1ao6")
====*

### Electrostatics: [Poisson-Boltzmann](http://thoppe.github.io/Presentation_Research_Macrocharge/#/6/2)
## $\nabla^2 \phi = -\rho/\epsilon, \quad \quad \quad U(r)/kT = Z^2 \lambda_B \, \left(\frac{\exp(\kappa a)}{1 + \kappa a}\right)^2 \, \frac{\exp(-\kappa r)}{r}$

Solve for $\phi$ with the Adaptive Poisson-Boltzmann Solver (APBS), 
!(images/macrocharge/human_serum_albumin_1e7h_ALPHA.png) <<transparent;height:300>>
!(images/macrocharge/human_serum_albumin_1e7h_pH_4.01886800_field.png) <<height:300>>

Typically (in the absence of ions), $\epsilon_{\text{water}} = 80$ and $\epsilon_{\text{protein}} = 4$.

&& APBS by Baker et al. [Proc. Natl. Acad. Sci. 2001](http://www.pnas.org/content/98/18/10037), Bjerrum length $\lambda_B = {e^2}/{4\pi \varepsilon_0 \varepsilon_r \  k_B T}$

====*
## Macrocharge fitting
Best fit macrocharges to approximate the field.
!(images/macrocharge/HSA_real.png) <<transparent;height:200>>
!(images/macrocharge/HSA_fit.png)  <<transparent;height:200>>
====+
------
!(images/macrocharge/HSA_1E7H_spheres.png) <<transparent;height:250>>
!(images/macrocharge/superposition_SPH.png) <<transparent;height:250>>
Decompose the field, determine a region of excluded volume +
spherical harmonic decomposition for large distances.
   
====<<transition:none>>

## Matching experiments
Theoretical predictions of the second virial coefficient $B_{2}$
considering only excluded volume and reduced electrostatics.
!(images/macrocharge/exp_B22_1OVA.png) <<height:550px;>>

====*<<transition:none>>
## Matching experiments
Theoretical predictions of the second virial coefficient $B_{2}$
considering only excluded volume and reduced electrostatics.
!(images/macrocharge/fit_B22_1OVA.png) <<height:550px;>>

&& _A Simplified Representation of Anisotropic Charge Distributions within Proteins_, Hoppe,  [J. Chem. Phys. (2013)](http://scitation.aip.org/content/aip/journal/jcp/138/17/10.1063/1.4803099)

====*<<transition:default>>
### Phase separations summary

Calculate the _non-ideality_ of a protein molecule after including 
both the excluded volume and electrostatics.

Predict the second-virial coefficient as a function of pH values, protein concentrations, binary mixtures, and salt concentrations.

*Ongoing research:* Use the model in higher-order simulations 
to predict phase behavior via Gibb's ensembles.
