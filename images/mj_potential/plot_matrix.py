import numpy as np
import pandas as pd
import json
from Bio.PDB.Polypeptide import three_to_one

with open("model_system.json") as FIN:
    js = json.load(FIN)

A = js["interaction_matrix"]
cols = js["interaction_matrix_labels"]
cols = [three_to_one(x) for x in cols]


MJ = pd.DataFrame(A, columns=cols, index=cols)

import pylab as plt
#import seaborn as sns
r0,r1 = MJ.min().min(), MJ.max().max()
r = max(abs(r0),abs(r1))

m,n = 20,20
fig = plt.figure(figsize=(15,15))
#fig,axes = plt.subplots(111,figsize=(15,15))
#fig.set_figheight(15)
#fig.set_figwidthheight(15)
#ax = axes[0]

import matplotlib as mpl
mpl.rcParams['ytick.major.pad'] = 14


ax=plt.imshow(MJ, 
          interpolation='nearest', 
          cmap='bwr',vmin=-r,vmax=r).get_axes()

ax.set_xticks(np.linspace(0, n-1, n))
ax.set_xticklabels(MJ.columns)
ax.set_yticks(np.linspace(0, m-1, m))
ax.set_yticklabels(MJ.index)
ax.grid('off')
ax.xaxis.tick_top()

ax.tick_params(axis='both', 
               which='major', labelsize=25)
cbar = plt.colorbar(fraction=.046, pad=0.04)
cbar.ax.tick_params(labelsize=20) 

for tick in ax.yaxis.get_major_ticks():
    tick.tick1line.set_markersize(0)
    tick.tick2line.set_markersize(0)
    tick.label1.set_horizontalalignment('center')

plt.savefig("MJ_matrix.png",
            bbox_inches='tight',transparent=True)
#plt.show()
