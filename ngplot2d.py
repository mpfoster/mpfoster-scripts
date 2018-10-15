#! /usr/bin/env python
# nmrglue script to plot 2D spectrum
# added nv plotting via nmrfam's nv2ucsf
# MPF 2018-10-11

import sys
import argparse
import nmrglue as ng
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm
#
parser = argparse.ArgumentParser()
parser.add_argument('fname', nargs='+', help='file name')
parser.add_argument("-pos", help="plot positive contours", action="store_true")
parser.add_argument("-neg", help="plot negative contours", action="store_true")
parser.add_argument("-posneg", help="plot positive and negative contours", action="store_true")
parser.add_argument("-fmin", help="fractional minimum counter level (default is 0.05)", type=float, default=0.05)
parser.add_argument("-x0", help="x-dim start ppm", type=float, default=None)
parser.add_argument("-xn", help="x-dim end ppm", type=float, default=None)
parser.add_argument("-y0", help="y-dim start ppm", type=float, default=None)
parser.add_argument("-yn", help="y-dim end ppm", type=float, default=None)
parser.add_argument("-mult", help="counter level multiplier (default is 1.3)", type=float, default=1.3)
parser.add_argument("-lev", help="number of contours (default is 20)", type=int, default=20)
parser.add_argument("-lw", help="linewidth for contours (default is 1.5)", type=float, default=1.5)
parser.add_argument("-pdf", help="save a spectrum.pdf", action="store_true")
parser.add_argument("-grid", help="draw grid lines", action="store_true")
parser.add_argument("-legend", help="show legend on plot", action="store_true")

args = parser.parse_args()
print args

# plot parameters
contour_num = args.lev                # number of contour levels
contour_factor = args.mult          # scaling factor between contour levels
mpl.rcParams['lines.linewidth'] = args.lw


# create the figure
fig = plt.figure()
ax = fig.add_subplot(111)
# define colors to use for multiple plots
#colors = ('k','r','b','g','m','c','y')
colors = ('C0','C1','C2','C3','C4','C5','C6','C7','C8','C9')

nfiles = len(args.fname)

pmap = matplotlib.cm.Blues_r    # contour map (colors to use for contours)
nmap = matplotlib.cm.Reds    # contour map (colors to use for neg contours)
# use a color map for one file; single colors for many
if nfiles > 1:
	pmap=None
	nmap=None

files = args.fname
print "files:", files
#dic, data = ng.pipe.read("test.ft2")
#for infile in files:
for i in range(nfiles):
	infile = files[i]
	if infile.endswith(('.ft2', '.ft1', '.fid')):
		dic, data = ng.pipe.read(infile)
	elif infile.endswith('.ucsf'):
		dic, data = ng.sparky.read(infile)
		C = ng.convert.converter()
		C.from_sparky(dic, data)
		dic, data = C.to_pipe()
	elif infile.endswith('.nv'):    # requires nv2ucsf in path
       		from subprocess import call
       	 	call(["nv2ucsf", infile, "/tmp/tmp.ucsf"])
       	 	dic, data = ng.sparky.read("/tmp/tmp.ucsf")
       	 	C = ng.convert.converter()
        	C.from_sparky(dic, data)
        	dic, data = C.to_pipe()
        	call(["rm", "/tmp/tmp.ucsf"])
	
	#dic, data = ng.process.pipe_proc.tp(dic,data)
	print "File:", infile
	print "DIMORDER" , dic['FDDIMORDER']
	print dic['FDF1OBS'], "x",  dic['FDF2OBS']
	print dic['FDF1FTSIZE'], "x", dic['FDF2FTSIZE']
	print dic['FDF1LABEL'], "x", dic['FDF2LABEL']

	# set threshghold at percent of max
	f_thresh = args.fmin
	maxdata = np.amax(data)
	contour_start = maxdata * f_thresh           # contour level start value
	print "Countour Start:", contour_start

	# make ppm scales
	uc_d1 = ng.pipe.make_uc(dic, data, dim=1)	# uc: unit conversion
	ppm_d1 = uc_d1.ppm_scale()
	ppm_d1_0, ppm_d1_1 = uc_d1.ppm_limits()
	uc_d0 = ng.pipe.make_uc(dic, data, dim=0)
	ppm_d0 = uc_d0.ppm_scale()
	ppm_d0_0, ppm_d0_1 = uc_d0.ppm_limits()
	limits = uc_d0.ppm_limits() + uc_d1.ppm_limits()


	# plot the contours
	#ax.contour(data, cl, cmap=cmap )
	#ax.contour(data, cl, cmap=cmap, extent=( limits ) )
	if args.neg:
		# calculate negative contour levels
		nl = -contour_start * contour_factor ** np.arange(contour_num-1,-1,-1) 
		cl=nl
		if nfiles == 1:
			ax.contour(data, cl, 
				cmap=pmap, 
       				extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))
		else:
			CS = ax.contour(data, cl, 
				colors=colors[i],
       				extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))
#		ax.contour(data, cl, cmap=nmap,
#      			extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))

	elif args.pos:
		# calculate positive contour levels
		cl = contour_start * contour_factor ** np.arange(contour_num) 
		if nfiles == 1:
			ax.contour(data, cl, 
				cmap=pmap, 
       				extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))
		else:
			CS = ax.contour(data, cl, 
				colors=colors[i],
       				extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))
	else:
		nl = -contour_start * contour_factor ** np.arange(contour_num-1,-1,-1) 
		pl = contour_start * contour_factor ** np.arange(contour_num) 
#		cl=np.append(nl,pl)
		if nfiles == 1:
			ax.contour(data, pl, 
				cmap=pmap, 
       				extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))
			ax.contour(data, nl, 
				cmap=nmap, 
       				extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))
		else:
			CS = ax.contour(data, pl, 
				colors=colors[i],
       				extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))
			ax.contour(data, nl, 
				colors=colors[i],
       				extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))
#		ax.contour(data, pl, 
#			cmap=pmap, 
#			colors=color,
#       			extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))
#		ax.contour(data, nl, 
#			cmap=nmap, 
#       			extent=(ppm_d1_0, ppm_d1_1, ppm_d0_0, ppm_d0_1))

# add some labels
#ax.text(59.25, 104.0, "T49", size=8, color='r')
#ax.text(58.75, 106, "T11", size=8, color='k')

# plot slices in each direction
#xslice = data[uc_15n("111.27 ppm"), :]
#ax.plot(ppm_13c, -xslice / 4.e4 + 111.27)
#yslice = data[:, uc_13c("62.0 ppm")]
#ax.plot(yslice / 2.e4 + 62.0, ppm_15n)

# decorate the axes
ax.set_ylabel( dic['FDF1LABEL'] + " ppm" )
ax.set_xlabel( dic['FDF2LABEL'] + " ppm" )
if nfiles == 1:
	ax.set_title( infile )

if args.grid:
	plt.grid(True)

if args.legend:
	ax.legend()

#ax.set_xlim( uc_d1.ppm_limits() )
#ax.set_xlim(10,6)
#ax.set_ylim( uc_d0.ppm_limits() )
#ax.set_ylim(132, 105)
print uc_d1.ppm_limits()
x_start, x_end = uc_d1.ppm_limits()
y_start, y_end = uc_d0.ppm_limits()
if args.x0:
	x_start = args.x0
if args.xn:
	x_end = args.xn
if args.y0:
	y_start = args.y0
if args.yn:
	y_end = args.yn
ax.set_xlim(x_start,x_end)
ax.set_ylim(y_start,y_end)

#print CS.collections

plt.show()

if args.pdf:
	fig.savefig("spectrum.pdf") # this can be .pdf, .ps, .png, etc

