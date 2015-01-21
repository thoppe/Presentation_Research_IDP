## Multiscale protein modeling 
### Disorder & aggregation

----------

*[Travis Hoppe](http://thoppe.github.io/)*, [(deck source)](https://github.com/thoppe/Presentation_Research_IDP)

National Institutes of Health (NIH)
National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)
Laboratory of Chemical Physics (LCP), Theoretical Biophysical Chemistry

====*

## People involved
### Allen Minton, Di Wu
!(images/people/minton.jpg) <<height:250>>
!(images/people/di.jpg)     <<height:250>>
### Robert Best, Wenwei Zheng
!(images/people/robert.jpg) <<height:250>>
!(images/people/wenwei.jpg) <<height:250>>

====

## BIO*PHYSICS*
### Multiscale modeling

### Length

### Time

====

## Biological question

How do we make predictions about intrinsically disordered proteins when traditional methods fail?

====

# Protein Structure
### Four levels of complexity:

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

&& Ovalbumin, Egg white protein [PDB 1OVA](http://www.rcsb.org/pdb/explore.do?structureId=1ova), Crystal Structure, [Carrell](http://www.ncbi.nlm.nih.gov/pubmed/1942038?dopt=Abstract)


====
## Protein folding problem

Predict structure from sequence
### Sequence $\rightarrow$ Structure $\rightarrow$ Function

!(images/energy_landscape.jpg)  <<height:300>>
!(images/T42morphs.gif)  <<height:300>>

Native structure, folding pathways, ...

&& Energy Landscape by [Wolynes](http://rsta.royalsocietypublishing.org/content/363/1827/453), Folding Example of NK-lysin by [Jones](http://www.ncbi.nlm.nih.gov/pubmed/9485510).

TO DO: UPDATE PICTURE TO: http://pubs.acs.org/doi/abs/10.1021/ct500569b

====
Only works when you have a well-defined structure...

IDP (intrinsically disordered proteins) do not!

====

## Intrinsically disordered proteins

### Structure
+ Lacks *tertiary structure* (disorder!)
+ Still may form secondary structure
+ Different *primary structure* (residue propensity)
+ More charged, less hydrophobic and aromatic residues

### Function
+ Often found in signaling pathways, centers of protein hubs
+ *Specificity*, with *low affinity*

### Modeling
+ Traditional methods are problematic (no funnel, no pathway!)

====

## Statistical Potentials
Residue-residue interactions, quasi-chemical lattice-gas

## $U_{a,b} = -kT \ln \frac{p_{\text{obs}}(a,b)}{p_\text{exp}(a,b)} \approx -kT \ln \frac{N_\text{obs}(a,b)}{N_\text{exp}(a,b)}$

!(images/1pcy/1pcy_cartoon.png) <<height:300>>
!(images/1pcy/1pcy_sticks.png) <<height:300>>
!(images/1pcy/1pcy_ultra_sidechain.png) <<height:300>>
!(images/1pcy/1pcy_res_res.png) <<height:300>>

&& Protein database, Top 8000 REFERENCE HERE

====*

### Residue-residue interaction matrix, MJ
!(images/mj_potential/MJ_matrix.png)  <<transparent>> <<height:500>>

&& Other statistical potentials: [Tanaka and Scheraga](http://pubs.acs.org/doi/abs/10.1021/ma60054a013) (1976), [Spil](http://www.ncbi.nlm.nih.gov/pubmed/2359125) (1990), [Miyaza and Jernigan](http://www.ncbi.nlm.nih.gov/pubmed/8604144) (1996), <br> [Betancourt and Thirumalai](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2144252/) (1999), [Skolnick, Kolinski and Ortiz](http://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0134%2820000101%2938:1%3C3::AID-PROT2%3E3.0.CO;2-S/abstract) (2000)

====*

### MJ matrix reveals biophysical structure

DIAGONALIZED MJ MATRIX HERE

====

### MJ Contact energy, from structure

# $U_\text{MJ} = \sum_{i=1}^N \sum_{j>i}^N E_{ij}  \quad \quad E_{ij} = \mathbf{M}_{\text{res}(i), \text{res}(j)}$

### Mean-field (MF) energy, from sequence

# $U_{\text{MF}} = \sum_{\alpha=1}^{20} \sum_{\beta=\alpha}^{20} E_{\alpha \beta} \cdot n_{\text{contact}}(\alpha, \beta)$
### $n_{\text{contact}}(\alpha, \beta) = X_{\alpha} X_{\beta} e^{-\mathbf{M}_{\alpha \beta}/kT} $

====*

MF Energy distributions

INSERT: AA propensities
INSERT Kyle-Doolittle plot

!(images/mean_field_calc/average_self_energy.png)


====*

MJ contact energy can reproduce MF energy!
UPDATE TO MORE ACCURATE PICTURE
!(images/MJ_MF_energy_cmp.png)

====

## Protein-Protein interactions

Pairwise decomposition of energetic terms of protein complex, A--B
## $U_{AB,\text{complex}} = U_A + U_B + U_{AB}$

Contact matrix is now not symmetric (UPDATE THIS):
### $n_{AB \text{contact}}(\alpha, \beta) = X_{\alpha} X_{\beta} e^{-\mathbf{M}_{\alpha \beta}/kT} $

====
## Binding affinity

Native-Native interactions and Native-IDP interactions

INSERT: affinity plot

====*

## Binding specificity

UPDATE: correct z-score
# $z = \left ( \left< E_{\text{bound}} \right > - E_{\text{unbound}} \right ) / \text{VAR}[E_\text{all}] $

INSERT: specificity plot

UPDATE: plot E min?

====*

## MF energy correlates to structure

INSERT: MF energy vs radius of gyration

====

## MF IDP Summary:

+ MF models can reproduce MJ contact energies
+ MF IDP's bound to native structures show increased _specificity_ with lower _affinity_.












