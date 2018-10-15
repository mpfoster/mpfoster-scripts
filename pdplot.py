#!/usr/bin/env python
# python script to read data using pandas, then plot it
# uses pandas dataframe structure
# uses argparse to parse command line arguments
# MPF 2018-07-21

import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('fname', nargs='+', help='file name')
parser.add_argument("-x", help="specify column number for x axis [first col is 0]", type=int, default=0)
parser.add_argument("-y", help="specify column numbers for y axis", nargs='+', type=str, default=['1'])
parser.add_argument("-marker", help="specify marker", type=str, default='')

args = parser.parse_args()
print args

fname = args.fname[0]

df = pd.read_table(fname, comment='#')
xcol = args.x
ycol = [int(item) for item in args.y[0].split(',')]

#print('Plotting colums %i x %i of %s...' % (args.x,args.y,fname))
#df.plot(xcol, ycol, color=args.color, marker=args.marker, title=fname, legend=False)
#if len(ycol) == 1:
#	df.plot(xcol, ycol, marker=args.marker, title=fname, legend=False)
#	plt.ylabel(df.columns[ycol[0]])
#else:
#	df.plot(xcol, ycol, marker=args.marker, title=fname)

#plt.ticklabel_format(style='sci',axis='x',scilimits=(0,0))
#plt.ticklabel_format(style='sci',scilimits=(-3,4),axis='both')
#plt.xlim(xmin=0.0, xmax=1e-6)

# using plt instead of df.plt
fig = plt.figure()
ax = fig.add_subplot(111)
if len(ycol) == 1:
	ax.plot(df.iloc[:,xcol], df.iloc[:,ycol], args.marker)
	ax.set_ylabel(df.columns[ycol[0]])
else:
	ax.plot(df.iloc[:,xcol], df.iloc[:,ycol], args.marker)
	ax.legend(df.columns[ycol])

ax.set_title(fname)
ax.set_xlabel(df.columns[xcol])
ax.ticklabel_format(style='sci',scilimits=(-3,4),axis='both')

plt.show()
print "...done"
