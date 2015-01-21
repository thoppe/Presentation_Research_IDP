{"theme":"md2reveal/css/one_moz.css"}

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

# Multiscale

## Length

## Time

====

# Protein Structure
### Four levels of complexity:

|### Primary structure    (sequence)
|### Secondary structure  (helices, sheets)
|### Tertiary structure   (3D structure)
|### Quaternary structure (protein complex)

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

&& Energy Landscape by [Wolynes](http://rsta.royalsocietypublishing.org/content/363/1827/453), Folding Example by of NK-lysin [Jones](http://www.ncbi.nlm.nih.gov/pubmed/9485510).

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
+ Specificity, low affinity

### Modeling
+ Tradiational methods are problematic (no funnel!)

====

## Statistical Potentials
Residue-residue interactions, quasi-chemical lattice-gas

## $U_{a,b} = -kT \ln \frac{p_{\text{obs}}(a,b)}{p_\text{exp}(a,b)} \approx -kT \ln \frac{N_\text{obs}(a,b)}{N_\text{exp}(a,b)}$

!(images/1pcy/1pcy_cartoon.png) <<height:300>>
!(images/1pcy/1pcy_sticks.png) <<height:300>>
!(images/1pcy/1pcy_ultra_sidechain.png) <<height:300>>
!(images/1pcy/1pcy_res_res.png) <<height:300>>

====*

### Residue-residue interaction matrix

Most famous, Miyaza and Jernigan (MJ) matrix*.
!(images/mj_potential/MJ_matrix.png) <<height:500>>

&& *Other statisitical potentials: [Tanaka and Scheraga](http://pubs.acs.org/doi/abs/10.1021/ma60054a013) (1976), [Spil](http://www.ncbi.nlm.nih.gov/pubmed/2359125) (1990), [Miyaza and Jernigan](http://www.ncbi.nlm.nih.gov/pubmed/8604144) (1996), <br> [Betancourt and Thirumalai](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2144252/) (1999), [Skolnick, Kolinski and Ortiz](http://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291097-0134%2820000101%2938:1%3C3::AID-PROT2%3E3.0.CO;2-S/abstract) (2000)






