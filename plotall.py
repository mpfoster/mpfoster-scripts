import os
import sys
import glob
from natsort import natsorted
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from natsort import natsort

# get files from command line:
files = natsorted(sys.argv[1:])

# select all matching files in directory:
#files = natsorted(glob.glob('PLH_20180507_[1-9]*.txt')) 

nf = len(files)

print("NF:", nf)
print("Files:", files)

data_columns = [0, 2]
print("plotting columns %s\n" % (data_columns))

f, axarr = plt.subplots(nf, sharex=True, sharey=True, figsize=(7,10))
#f, axarr = plt.subplots(nf, sharex=True, sharey=True)
#f.suptitle('Stacked Plots')
f.suptitle( os.path.basename(os.getcwd()) )

data = list()
#for fname in files:
for i in range(0,nf):
    print i, files[i]
    data.append(i)
    data[i]=np.genfromtxt(files[i], comments='#', skip_header=2, usecols=data_columns, invalid_raise=False)
#    axarr[i].plot(data[i][:,0], data[i][:,1], label=files[i], lw=1)
    axarr[i].plot(data[i][:,0], data[i][:,1], lw=1)

    f.subplots_adjust(hspace=0)
# Hide x labels and tick labels for all but bottom plot.
    for ax in axarr:
        ax.yaxis.set_visible(False)
        ax.grid(linestyle='-')
#        ax.set_xlim(4750,4925)
#        ax.grid(axis='x')
#        ax.set_xlabel('$m/z$')
        ax.set_xlabel('$m/z$')
        ax.legend(frameon=False, handletextpad=-2.0, handlelength=0)
        ax.label_outer()

# if (hardcopy) 
plt.savefig("plot.pdf", format='pdf')

plt.show()
