import numpy as np
import pandas as pd
import json

with open("model_system.json") as FIN:
    js = json.load(FIN)

A = js["interaction_matrix"]
cols = js["interaction_matrix_labels"]

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

ax=plt.imshow(MJ, 
          interpolation='nearest', 
          cmap='Oranges',vmin=-r,vmax=r).get_axes()


ax.set_xticks(np.linspace(0, n-1, n))
ax.set_xticklabels(MJ.columns)
ax.set_yticks(np.linspace(0, m-1, m))
ax.set_yticklabels(MJ.index)
ax.grid('off')
ax.xaxis.tick_top()
plt.savefig("MJ_matrix.png",bbox_inches='tight')
#plt.show()
