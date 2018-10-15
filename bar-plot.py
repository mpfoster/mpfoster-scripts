#!/usr/bin/env python
#
import os
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
#import numpy as np

# expect datfile as argument:
data_file = sys.argv[1]
base_name = os.path.splitext(os.path.basename(data_file))[0]
# data file has 
# site concenration in column 0
#ligand concentraton in column 1, 
# populations in the remaining columns
#data = np.genfromtxt(data_file, comments='#', unpack=False)
#data = np.genfromtxt(data_file, comments='#', skip_header=3, names=True, unpack=False)
#data = np.genfromtxt(data_file, comments='#', unpack=True)
df = pd.read_table(data_file, comment='#')

#rows are conc; columns are states
print df.shape
nconc, nstates = df.iloc[:,2:].shape

print "Number of concentrations:", nconc
print "Number of states:", nstates
#print "Ligand concentrations:", data[:,0]
#print "Ligand concentrations:", df.iloc[:,1]
#print "Populations, state 0:", data[:,1]

#bar_width = 0.8 * (data[-1,1]-data[0,1])/len(data[:])
bar_width = 0.8 * (df.iloc[-1,1]-df.iloc[0,1])/nconc

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#for i in range(2,len(data[0])): 
for i in range(2,len(df.iloc[0])): 
#	xs = range(nconc)
#	xs = data[:,1]*1e6
	xs = df.iloc[:,1]
#	xs = range(1,len(data)+1)
#	xs = data[1]
#	ys = data[:,i]
	ys = df.iloc[:,i]
# make array for the Z values. 
	zs = i-2
#	print xs
#	print ys
	
	# You can provide either a single color or an array. To demonstrate this,
	# the first bar of each set will be colored cyan.
#	cs = [c] * len(xs)
 #   cs[0] = 'c'
#	dx = 0.1
#	dy = ys
#	dz = 0.1
#	ax.bar3d(xs, ys, [0.0]*len(zs), dx=dx,dy=dy,dz=zs, color=plt.cm.jet(1. * i / 12), zsort='average')
#	ax.bar3d(xs, [0.0]*ys,zs, dx=dx,dy=dy,dz=dz, zdir='y', color=plt.cm.jet(1. * i / nstates), zsort='average')
#	ax.bar(xs, ys,zs, zdir='y',color=plt.cm.jet(1. * i / nstates),alpha=0.8)
#	ax.bar(xs, ys,zs, zdir='y',color=plt.cm.jet(1. * i / 12),alpha=0.8)
#	ax.bar(xs, ys,zs, zdir='y',width=0.8, color=plt.cm.winter(1. * i / nstates),alpha=0.8, linewidth=1,edgecolor='b')
	ax.bar(xs, ys,zs, zdir='y',width=bar_width, color=plt.cm.winter(1. * i / nstates),alpha=0.8, linewidth=1,edgecolor='b')
#	ax.bar(xs, ys,zs, zdir='y',width=bar_width, color=plt.cm.winter(1. * i / (nstates+1)),alpha=0.8)

ax.set_title(data_file)
ax.set_xlabel('[Ligand] /M')
ax.set_ylabel('State')
#ax.set_ylabel('# bound Trp')
ax.set_zlabel('Population')
ax.ticklabel_format(style='sci',scilimits=(-3,4),axis='both')
#ax.set_xlim([0,15])
ax.set_zlim([0,1])
#ax.invert_yaxis()
#ax.view_init(elev=-70.0, azim=20.0)

# if (hardcopy) uncomment next line
# plt.savefig(base_name + ".pdf", format='pdf')

# if graphic, uncomment:
plt.show()
