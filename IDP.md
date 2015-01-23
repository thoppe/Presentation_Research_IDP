## Multiscale protein modeling 
### Disorder & aggregation

----------

*[Travis Hoppe](http://thoppe.github.io/)*, [(deck source)](https://github.com/thoppe/Presentation_Research_IDP)

National Institutes of Health (NIH)
National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)
Laboratory of Chemical Physics (LCP), Theoretical Biophysical Chemistry

====
## Biophysical question #1

How do we make predictions about intrinsically disordered proteins 
_without sampling the entire conformational landscape_?

====+
<br>

## Biophysical question #2

How can we predict phase-separations of protein solutions?
====*

## People involved
### Robert Best, Wenwei Zheng
!(images/people/robert.jpg) <<height:250>>
!(images/people/wenwei.jpg) <<height:250>>
### Allen Minton, Di Wu
!(images/people/minton.jpg) <<height:250>>
!(images/people/di.jpg)     <<height:250>>
====

# Protein Structure
### Levels of complexity:

|### Primary structure    (sequence)
|### Secondary structure  (helices, sheets)
|### Tertiary structure   (3D structure)
|### Quaternary structure (protein complex)
|### Higher-order structure (aggregation)

====*

## Primary Structure
Twenty residue "alphabet" forms polypeptide chain
!(images/common_aa_chart.png) <<width:1200>>

&& Chemical Structure of the Twenty Common Amino Acids, [Compound Interest](http://www.compoundchem.com/2014/09/16/aminoacids/)

====*

## Secondary & Tertiary Structure
!(images/1ova/1ova_lines.png)   <<width:380>>
!(images/1ova/1ova_spheres.png) <<width:380>>
!(images/1ova/1ova_cartoon.png) <<width:380>>

From sequence to structure
    GSIGAASMEF CFDVFKELKV HHANENIFYC PIAIMSALAM VYLGAKDSTR TQINKVVRFD KLPGFGDEIE AQCGTSVNVH 
    SSLRDILNQI TKPNDVYSFS LASRLYAEER YPILPEYLQC VKELYRGGLE PINFQTAADQ ARELINSWVE SQTNGIIRNV 
    LQPSSVDSQT AMVLVNAIVF KGLWEKAFKD EDTQAMPFRV TEQESKPVQM MYQIGLFRVA SMASEKMKIL ELPFASGTMS 
    MLVLLPDEVS GLEQLESIIN FEKLTEWTSS NVMEERKIKV YLPRMKMEEK YNLTSVLMAM GITDVFSSSA NLSGISSAES 
    LKISQAVHAA HAEINEAGRE VVGGAEAGVD AASVSEEFRA DHPFLFCIKH IATNAVLFFG RCVSP

&& Ovalbumin, Egg white protein [PDB 1OVA](http://www.rcsb.org/pdb/explore.do?structureId=1ova), Crystal Structure resolved by [Carrell](http://www.ncbi.nlm.nih.gov/pubmed/1942038?dopt=Abstract)


====
## Protein folding problem

Predict structure from sequence
### Sequence $\rightarrow$ Structure $\rightarrow$ Function

!(images/energy_landscape.jpg)  <<height:300; transparent>>
!(images/ww_fold.m4v) <<height:300>>

Native structure, folding pathways, ...

&& Energy Landscape by [Wolynes](http://rsta.royalsocietypublishing.org/content/363/1827/453), Folding Example of WW-domain by [Best](http://pubs.acs.org/doi/abs/10.1021/jp102575b), 2010.

====*

## Protein Modeling
Coarse-grained depictions of proteins and their interactions

====+

!(images/not_a_protein/the-treachery-of-images.jpg) <<height:375>>
!(images/not_a_protein/Not_A_protein.png)           <<height:375>>

&& _The Treachery of Images_ by [René Magritte](http://en.wikipedia.org/wiki/The_Treachery_of_Images)

====*

Traditional computational techniques, molecular dynamics
work when you have a well-defined native structure.

Sample conformational space around the native structure, or along a pathway.

====+
<br>
<br>

IDPs (**intrinsically disordered proteins**) lack a folding pathway and native state!

## Folding $\Rightarrow$ Sampling

====

## Intrinsically disordered proteins
|### Structure
+ Lacks *tertiary structure* (disorder!)
+ Still may form secondary structure
+ Different *primary structure* (residue propensity)
+ More charged, less hydrophobic and aromatic residues
|### Function
+ Often found in signaling pathways, centers of protein hubs
+ *Specificity*, with *low affinity*
|### Modeling
+ Traditional methods are problematic (no funnel, no pathway!)

====

## Statistical Potentials
Residue-residue interactions, quasi-chemical lattice-gas

## $U_{a,b} = -kT \ln \frac{p_{\text{obs}}(a,b)}{p_\text{exp}(a,b)} \approx -kT \ln \frac{N_\text{obs}(a,b)}{N_\text{exp}(a,b)}$

!(images/1pcy/1pcy_cartoon.png) <<height:300>>
!(images/1pcy/1pcy_sticks.png) <<height:300>>
!(images/1pcy/1pcy_ultra_sidechain.png) <<height:300>>
!(images/1pcy/1pcy_res_res.png) <<height:300>>

&& [Protein database: Top 8000](http://kinemage.biochem.duke.edu/databases/top8000.php), Richardson

====*<<transistion:none>>

### Residue-residue interaction matrix, MJ
!(images/mj_potential/MJ_matrix.png)  <<transparent; height:700>>

&& Other statistical potentials: [Tanaka and Scheraga](http://pubs.acs.org/doi/abs/10.1021/ma60054a013) (1976), [Spil](http://www.ncbi.nlm.nih.gov/pubmed/2359125) (1990), [Miyaza and Jernigan](http://www.ncbi.nlm.nih.gov/pubmed/8604144) (1996),<br>[Betancourt and Thirumalai](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2144252/) (1999), [Skolnick, Kolinski and Ortiz](http://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0134%2820000101%2938:1%3C3::AID-PROT2%3E3.0.CO;2-S/abstract) (2000)

====*<<transistion:none>>
### MJ matrix reveals biophysical structure
!(images/mj_potential/MJ_matrix_remapped.png)  <<transparent; height:700>>
====

### MJ Contact energy, from structure
# $U_\text{MJ} = \sum_{i=1}^N \sum_{j>i}^N E_{ij}  \quad \quad \quad \quad E_{ij} = \mathbf{M}_{\text{res}(i), \text{res}(j)}$
====+
<br>
<br>
### Mean-field (MF) energy, from sequence
# $U_{\text{MF}} = \sum_{\alpha=1}^{20} \sum_{\beta=\alpha}^{20} n_{\text{contact}}(\alpha, \beta) E_{\alpha \beta}$
### $n_{\text{contact}}(\alpha, \beta) = X_{\alpha} X_{\beta} e^{-\mathbf{M}_{\alpha \beta}/kT} $

====*<<transistion:none>>
MJ contact energy reproduces MF energy
!(images/estimation_MF_MJ.png)       <<transparent; height:700>> 

====*<<transistion:none>>
Energy per residue still shows good correlation
!(images/estimation_MF_MJ_per_N.png) <<transparent; height:700>> 

====*<<transistion:none>>
MF Energy distributions: Physically reasonable
!(images/mean_field_calc/average_self_energy.png)  <<transparent; height:325>>
!(images/mean_field_calc/residue_propensity.png)   <<transparent; height:325>>
!(images/mean_field_calc/MF_vs_hydrophilicity.png) <<transparent; height:325>>
!(images/mean_field_calc/MF_vs_Garbuzynskiy.png)   <<transparent; height:325>>

&& [IDP Propensity](http://www.ncbi.nlm.nih.gov/pubmed/15657106), [Kyte-Doolittle](http://www.ncbi.nlm.nih.gov/pubmed/7108955), [Garbuzynskiy index](http://www.ncbi.nlm.nih.gov/pubmed/20019059)

====<<transistion:default>>

## Protein Networks

+ Target protein (native-like or IDP) interacts with a range of possible surfaces
+ Measure average binding *affinity* of protein to surfaces
+ Measure binding *specificity* of protein to surfaces

====*

## Protein-Protein interactions

Pairwise decomposition of energetic terms of protein complex, A--B
### $U_{AB,\text{complex}} = U_A + U_B + U_{AB}$

Contact matrix is not symmetric
### $n_{AB, \text{contact}}(\alpha, \beta) = X_{A_\alpha} X_{B_\beta} e^{-\mathbf{M}_{\alpha \beta}/kT} $

====
## Binding affinity
!(images/binding_affinity.png) <<transparent; height:700>> 

====*
## Binding specificity

Define "decoys" as weakly bound structures in protein network.
### $Z_{E} = \left ( \left< E_{\text{decoy}} \right > - E_{\text{target}} \right ) / \sigma(E_\text{decoy})$

====*
## Binding specificity
!(images/binding_specificity_1.png) <<transparent; height:700>> 
====
## MF IDP Summary:
+ MF models reproduce MJ contact energies. MF IDP's bound to native structures show increased _specificity_ with lower _affinity_.

====+

!(images/small_lattice/1.png) <<height:150; transparent>>
!(images/small_lattice/2.png) <<height:150; transparent>>
!(images/small_lattice/3.png) <<height:150; transparent>>
!(images/small_lattice/4.png) <<height:150; transparent>>
!(images/small_lattice/5.png) <<height:150; transparent>>
!(images/small_lattice/6.png) <<height:150; transparent>>

!(images/small_lattice/7.png) <<height:150; transparent>>
!(images/small_lattice/8.png) <<height:150; transparent>>
!(images/small_lattice/9.png) <<height:150; transparent>>
!(images/small_lattice/10.png) <<height:150; transparent>>
!(images/small_lattice/11.png) <<height:150; transparent>>
!(images/small_lattice/12.png) <<height:150; transparent>>

_What's next?_ Add structure to mean field calculations. 
Lattices may be optimal for IDP's, they can reproduce native-energies but quickly sample extended conformational space.












