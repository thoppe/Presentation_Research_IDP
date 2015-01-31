### Paradigm shift
Proteins were thought to adopt stable, folded conformations.
Solving the structure was paramount for understanding the function.
====+

<br>
### Unexpected: disorder is abundant!
!(images/yeast_grouping_gsponer-2008.jpg)<<height:500;transparent>>  Grouping proteins in the yeast proteome, Gsponer, [Science (2008)](http://www.ncbi.nlm.nih.gov/pubmed/19039133)

====*

## Intrinsically disordered proteins
|### Structure
+ Lack *tertiary structure* (disorder!)
+ Still may form secondary structure
+ Different *primary structure* (residue propensity)
+ More charged, less hydrophobic and aromatic residues
|### Binding
!(images/1BRS_barnase_barstar/1BRS_complex.png)  <<height:300;transparent>> Not disordered, Lock and Key<br>Barnase-Barstar complex
!(images/1L8C_HIF1_CBP/1L8C.png) <<height:300;transparent>> Disorder-to-order<br>Hif-1 α/CBP
!(images/SIC1_disordered_protein_mittag.png) <<height:300;transparent>> Always disordered<br>SIC1 binding to CDC4
====*

|### Theory
+ What advantages do IDPs have over traditional proteins?
+ Recognition that the cellular environment is a crowded place.


|### Function
+ Often found in signaling pathways, centers of protein hubs
+ Linkers (entropic chains), Chaperones, HIV transcription [(TAT)](http://www.ncbi.nlm.nih.gov/pubmed/16423825)
+ Binding *specificity*, with *lower affinity*


|### Modeling
## IDPs: Folding $\Rightarrow$ Sampling

_Goal: Develop a model for IDP interactions._

====

## Statistical Potentials
Residue-residue interactions, quasi-chemical lattice-gas

## $U_{a,b} = -kT \ln \frac{p_{\text{obs}}(a,b)}{p_\text{expt}(a,b)} \approx -kT \ln \frac{N_\text{obs}(a,b)}{N_\text{expt}(a,b)}$

!(images/1pcy/1pcy_cartoon.png) <<height:300>>
!(images/1pcy/1pcy_sticks.png) <<height:300>>
!(images/1pcy/1pcy_ultra_sidechain.png) <<height:300>>
!(images/1pcy/1pcy_res_res.png) <<height:300>>

&& Potentials constructed from Top 8000 Protein Database, [Richardson Group](http://kinemage.biochem.duke.edu/databases/top8000.php)


====*<<transition:fade>>

### Residue-residue interaction matrix, MJ
!(images/mj_potential/MJ_matrix.png)  <<transparent; height:700>>

&& Other statistical potentials: [Tanaka and Scheraga](http://pubs.acs.org/doi/abs/10.1021/ma60054a013) (1976), [Spil](http://www.ncbi.nlm.nih.gov/pubmed/2359125) (1990), [Miyaza and Jernigan](http://www.ncbi.nlm.nih.gov/pubmed/8604144) (1996),<br>[Betancourt and Thirumalai](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2144252/) (1999), [Skolnick, Kolinski and Ortiz](http://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0134%2820000101%2938:1%3C3::AID-PROT2%3E3.0.CO;2-S/abstract) (2000)

====*<<transition:fade>>
### MJ matrix reveals biophysical structure
!(images/mj_potential/MJ_matrix_remapped.png)  <<transparent; height:700>>
&& H (hydrophobic), P (polar), C (charged)
%Analysis of Statistical Potentials by [Li](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.79.765).
====

### MJ Contact energy, from structure
# $U_\text{MJ} = \underset{r_i, r_j \text{in contact}}{\sum_{i=1}^N \sum_{j>i}^N E_{ij}} \quad \quad \quad \quad E_{ij} = \mathbf{M}_{\text{res}(i), \text{res}(j)}$
====+
<br>
<br>
### Mean-field (MF) energy, from sequence
# $U_{\text{MF}} = \sum_{\alpha=1}^{20} \sum_{\beta=\alpha}^{20} n_{\text{contact}}(\alpha, \beta) E_{\alpha \beta}$
### $n_{\text{contact}}(\alpha, \beta) = X_{\alpha} X_{\beta} e^{-\mathbf{M}_{\alpha \beta}/kT} $

====*
MJ contact energy reproduces MF energy
!(images/estimation_MF_MJ.png)       <<transparent; height:700>> 

&& <a href="images/estimationMFMJperN.png">Energy per residue</a> shows good correlation as well.

====
MF Energy distributions: Physically reasonable
!(images/mean_field_calc/residue_propensity.png)   <<transparent; height:320>>
!(images/mean_field_calc/average_self_energy.png)  <<transparent; height:320>>
!(images/mean_field_calc/MF_vs_hydrophilicity.png) <<transparent; height:320>>
!(images/mean_field_calc/MF_vs_Garbuzynskiy.png)   <<transparent; height:320>>


&& IDP Propensity, Coeytaux & Poupon, [Bioinformatics (2005)](http://www.ncbi.nlm.nih.gov/pubmed/15657106)<br>Hydrophilicity index, Kyte & Doolittle, [J. Mol. Biol. (1982)](http://www.ncbi.nlm.nih.gov/pubmed/7108955)<br>Amyloidogenic regions, Garbuzynskiy et. al. [Bioinformatics (2010)](http://www.ncbi.nlm.nih.gov/pubmed/20019059)

====<<transition:default>>

## Protein Networks
+ Target protein interacts with a range of possible surfaces.
+ Measure average binding *affinity* of protein to surfaces.
+ Measure binding *specificity* of protein to surfaces.


!(images/yeast_network_interaction.jpg) Example network: Protein-protein interactions in yeast, _S. cerevisiae_<br>Schwikowski & Fields et al., [Nature 2000](http://www.ncbi.nlm.nih.gov/pubmed/11101803).

====*

## Protein-complex energy

Pairwise decomposition of protein complex energy; Binding affinity $U_{AB}$
#### $U_{AB,\text{complex}} = U_A + U_B + U_{AB}$

Contact matrix is not symmetric
### $n_{AB, \text{contact}}(\alpha, \beta) = X_{A_\alpha} X_{B_\beta} e^{-\mathbf{M}_{\alpha \beta}/kT} $

Specificity score: Define "decoys" as weakly bound 
structures in protein network.
### $Z_{E} = \left ( \left< E_{\text{decoy}} \right > - E_{\text{target}} \right ) / \sigma(E_\text{decoy})$

%&& Z-scores of native protein structures, [Zhang and Skolnick](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2144000/)

====
## Binding affinity
!(images/binding_affinity.png) <<transparent; height:700>> 

====*
## Binding specificity
!(images/binding_specificity_1.png) <<transparent; height:700>> 
====*
## MF IDP Summary:
+ MF models reproduce MJ contact energies. MF IDP's bound to native structures show increased _specificity_ with lower _affinity_.

====+

!(images/small_lattice/7.png) <<height:150; transparent>> PDB:1B8A
!(images/small_lattice/2.png) <<height:150; transparent>> 1B0B
!(images/small_lattice/3.png) <<height:150; transparent>> 1BQ8
!(images/small_lattice/4.png) <<height:150; transparent>> 1DQP
!(images/small_lattice/5.png) <<height:150; transparent>> 1DOI
!(images/small_lattice/6.png) <<height:150; transparent>> 1C4Q


!(images/small_lattice/1.png) <<height:150; transparent>> 1ARB
!(images/small_lattice/8.png) <<height:150; transparent>> 1BXU
!(images/small_lattice/9.png) <<height:150; transparent>> 1CC8
!(images/small_lattice/10.png) <<height:150; transparent>> 1CCJ
!(images/small_lattice/11.png) <<height:150; transparent>> 1DFU
!(images/small_lattice/12.png) <<height:150; transparent>> 1DMG

_What's next?_ Add structure to mean field calculations. 
Lattices may be optimal for IDP's, they can reproduce native-energies but quickly sample extended conformational space.