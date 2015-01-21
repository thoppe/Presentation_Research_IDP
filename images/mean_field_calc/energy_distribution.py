import numpy as np
import mean_field_estimation as MF
import multiprocessing as mp

samples = 10**5
#samples = 300

# Optimal set of paramers for "unfoldedness"
gar_org = {"G":-7.73, "P":-8.27,       
           "A":-2.37, "D":-12.55,     
           "E":-8.96, "K":-4.63,
           "S":-5.03, "N":0.18,     
           "Q":1.85,  "T":-8.15,          
           "R":-7.36, "H":-8.13,
           "C":-9.20, "V":11.49,      
           "M":3.66,  "L":6.50,        
           "I":10.46, "Y":9.05,
           "F":19.46, "W":23.43}

hydrophilicity = {
    'A':1.8,    'C':2.5,
    'D':-3.5,   'E':-3.5,
    'F':2.8,    'G':-0.4,
    'H':-3.2,   'I':4.5,
    'K':-3.9,   'L':3.8,
    'M':1.9,    'N':-3.5,
    'P':-1.6,   'Q':-3.5,
    'R':-4.5,   'S':-0.8,
    'T':-0.7,   'V':4.2,
    'W':-0.9,   'Y':-1.3,
}

seq_n  = 50

def calc_hydrophilicity(AA):
    hydro = [hydrophilicity[MF.aa_index[x]] for x in AA]
    return sum(hydro)

def calc_gar(AA):
    return sum([gar_org[MF.aa_index[x]] for x in AA])

P = mp.Pool()

#sIDP_SEQS = (MF.sIDP_random_sequence(seq_n) for _ in xrange(samples))
IDP_SEQS = [MF.IDP_random_sequence(seq_n) for _ in xrange(samples)]
PDB_SEQS = [MF.PDB_random_sequence(seq_n) for _ in xrange(samples)]

import pandas as pd
df = pd.DataFrame()

func = MF.protein_self_energy
df["IDP_U"] = [U for U in P.imap(func, IDP_SEQS,chunksize=100)]
df["PDB_U"] = [U for U in P.imap(func, PDB_SEQS,chunksize=100)]

func = calc_hydrophilicity
df["IDP_HYDRO"] = [U for U in P.imap(func, IDP_SEQS,chunksize=100)]
df["PDB_HYDRO"] = [U for U in P.imap(func, PDB_SEQS,chunksize=100)]

func = calc_gar
df["IDP_GAR"] = [U for U in P.imap(func, IDP_SEQS,chunksize=100)]
df["PDB_GAR"] = [U for U in P.imap(func, PDB_SEQS,chunksize=100)]

import pylab as plt
import seaborn as sns
sns.set_context("talk")

sns.distplot(df["PDB_U"],norm_hist=True,label="Native-like")
sns.distplot(df["IDP_U"],norm_hist=True,label="IDP")

plt.legend(loc=2)
plt.xlabel("Mean field energy")

plt.xlim(-40,20)
#plt.savefig("average_self_energy.png",
#            bbox_inches='tight',transparent=True)
print "Skipping the save of the distribution"

plt.figure()
plt.scatter(df["IDP_U"], df["IDP_HYDRO"],alpha=.5,s=1,edgecolor='b')
plt.scatter(df["PDB_U"], df["PDB_HYDRO"],alpha=.5,s=1,edgecolor='b')
plt.ylabel("Kyte-Doolittle Hydrophilicity")
plt.xlabel("Mean field energy")
plt.savefig("MF_vs_hydrophilicity.png",
            bbox_inches='tight',transparent=True)


plt.figure()
plt.scatter(df["IDP_U"], df["IDP_GAR"],alpha=.5,s=1,edgecolor='b')
plt.scatter(df["PDB_U"], df["PDB_GAR"],alpha=.5,s=1,edgecolor='b')
plt.ylabel("Garbuzynskiy index")
plt.xlabel("Mean field energy")
plt.savefig("MF_vs_Garbuzynskiy.png",
            bbox_inches='tight',transparent=True)

plt.show()
