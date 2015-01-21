from __future__ import division
import json, os, sys
import pylab as plt
import numpy as np
import pandas as pd
import mean_field_estimation as MF
import multiprocessing as mp

IDP_propensities = pd.Series(MF.propensities["IDP"], 
                             index = MF.aa_index)
PDB_propensities = pd.Series(MF.propensities["PDB"], 
                             index = MF.aa_index)

df = pd.DataFrame(index = MF.aa_index)
df["Native-like"] = PDB_propensities
df["IDP"] = IDP_propensities


fixed_indexing = pd.Index(np.sort(df.index))
df.index = fixed_indexing
 
import seaborn as sns
sns.set_context("talk")

df.plot(kind="bar",width=.9)

plt.ylabel("Propensity")
plt.xlabel("Residue")

plt.savefig("residue_propensity.png",
            bbox_inches='tight',transparent=True)

plt.show()
