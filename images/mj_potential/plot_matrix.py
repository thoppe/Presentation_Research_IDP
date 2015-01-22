import numpy as np
import pandas as pd
import scipy.cluster.vq
import scipy.cluster.hierarchy
import json
from Bio.PDB.Polypeptide import three_to_one
import pylab as plt
#import seaborn as sns

import matplotlib as mpl
mpl.rcParams['ytick.major.pad'] = 14

with open("model_system.json") as FIN:
    js = json.load(FIN)

A = np.array(js["interaction_matrix"])
cols = js["interaction_matrix_labels"]
cols = [three_to_one(x) for x in cols]
#clusters = "ADEGKNPQRST CFHILMVWY"
#clusters = "ADEGKNPST CFHMWY ILQRV"
clusters = "AG CFHMWY DEKNPQRST ILV"
#clusters = "AG CW DEKPS FHMY ILV NQRT"

clusters = list(clusters.replace(' ',''))

MJ = pd.DataFrame(A, columns=cols, index=cols)
MJ2 = MJ.reindex(columns=clusters, index=clusters, copy=True)

r0,r1 = MJ.min().min(), MJ.max().max()
r = max(abs(r0),abs(r1))
m,n = 20,20

hydrophobic_res = "AILFVPG"
polar_res       = "QNHSTYCMW"
charged_res     = "RKDE"

def plot_residue_matrix(A, rename=False):
    fig = plt.figure(figsize=(15,15))
    #fig = plt.figure(figsize=(12,12))

    ax=plt.imshow(A, 
              interpolation='nearest', 
              cmap='bwr',vmin=-r,vmax=r).get_axes()

    cols = list(A.index)
    cols = [x if x not in hydrophobic_res else 
            r"${}^h$".format(x)
            for x in cols]
    cols = [x if x not in charged_res else 
            r"${}^c$".format(x)
            for x in cols]
    cols = [x if x not in polar_res else 
            r"${}^p$".format(x)
            for x in cols]
    if not rename: 
        cols = list(A.index)
        cols = [r"${}$".format(x) for x in cols]     

    ax.set_xticks(np.linspace(0, n-1, n))
    ax.set_xticklabels(cols)
    ax.set_yticks(np.linspace(0, m-1, m))
    ax.set_yticklabels(cols)
    ax.grid('off')
    ax.xaxis.tick_top()

    ax.tick_params(axis='both', 
                   which='major', labelsize=20)
    cbar = plt.colorbar(fraction=.046, pad=0.04)
    cbar.ax.tick_params(labelsize=20) 

    for tick in ax.yaxis.get_major_ticks():
        tick.tick1line.set_markersize(0)
        tick.tick2line.set_markersize(0)
        tick.label1.set_horizontalalignment('center')

    return fig

plot_residue_matrix(MJ)
plt.savefig("MJ_matrix.png",
            bbox_inches='tight',transparent=True)


plot_residue_matrix(MJ2,rename=True)
plt.savefig("MJ_matrix_remapped.png",
            bbox_inches='tight',transparent=True)

#plt.show()
