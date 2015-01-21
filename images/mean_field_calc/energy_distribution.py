import numpy as np
import mean_field_estimation as MF
import multiprocessing as mp

samples = 10**4
#samples = 300

# Optimal set of paramers for "unfoldedness"
gar_org = {"G":-7.73,                "P":-8.27,                "A":-2.37,
           "D":-12.55,                "E":-8.96,                "K":-4.63,
           "S":-5.03,                "N":0.18,                "Q":1.85,
           "T":-8.15,                "R":-7.36,                "H":-8.13,
           "C":-9.20,                "V":11.49,                "M":3.66,
           "L":6.50,                "I":10.46,                "Y":9.05,
           "F":19.46,                "W":23.43}
garbuzynskiy = np.zeros(20,dtype=float)
for aa in gar_org:
    idx = np.where(np.array(MF.aa_index)==aa)[0][0]
    garbuzynskiy[idx] = gar_org[aa]

def calc_garbuzynskiy(seq):
    return sum([garbuzynskiy[a] for a in seq])



surf_n = 5
seq_n  = 50
P = mp.Pool()

#sIDP_SEQS = (MF.sIDP_random_sequence(seq_n) for _ in xrange(samples))
IDP_SEQS = (MF.IDP_random_sequence(seq_n) for _ in xrange(samples))
PDB_SEQS = (MF.PDB_random_sequence(seq_n) for _ in xrange(samples))

import pandas as pd
df = pd.DataFrame()

func = MF.protein_self_energy
df["IDP_U"] = [U for U in P.imap(func, IDP_SEQS,chunksize=100)]
#df["sIDP_U"] = [U for U in P.imap(func, sIDP_SEQS,chunksize=100)]
df["PDB_U"] = [U for U in P.imap(func, PDB_SEQS,chunksize=100)]

#func = calc_garbuzynskiy
#df["IDP_G"] = [U for U in P.imap(func, IDP_SEQS,chunksize=100)]
#df["PDB_G"] = [U for U in P.imap(func, PDB_SEQS,chunksize=100)]

import pylab as plt
import seaborn as sns
sns.set(style="white")

'''
f, axes = plt.subplots(2, 1, figsize=(7, 7), sharex=True)

sns.kdeplot(df["IDP_U"],df["IDP_G"],shade=False,ax=axes[0])
axes[0].scatter(df["IDP_U"],df["IDP_G"],alpha=.2,color='k')
axes[0].set_xlim(-30,10)
axes[0].set_ylim(-175,100)
axes[0].set_title("IDP",fontsize=20)

sns.kdeplot(df["PDB_U"],df["PDB_G"],shade=False,ax=axes[1])
axes[1].scatter(df["PDB_U"],df["PDB_G"],alpha=.2,color='k')
axes[1].set_xlim(-30,10)
axes[1].set_ylim(-175,100)
axes[1].set_title("PDB",fontsize=20)
'''
#sns.jointplot("IDP_U","IDP_G",df,kind="kde",
#sns.jointplot("PDB_U","PDB_G",df,kind="kde",xlim=(-50,10),ylim=(-150,100))

#plt.scatter(IDP_U,IDP_G,color='k',alpha=.5)
#plt.scatter(PDB_U,PDB_G,color='r',alpha=.5)

sns.distplot(df["IDP_U"],norm_hist=True,label="IDP")
sns.distplot(df["PDB_U"],norm_hist=True,label="PDB")
#sns.distplot(df["sIDP_U"],norm_hist=True,label="sIDP")
plt.legend(loc=2)
plt.xlabel("Mean field energy")
plt.title("Distribution of energy sampled from different propensities, N={}".format(seq_n))
plt.xlim(-40,20)
plt.savefig("average_self_energy.png")
plt.show()
