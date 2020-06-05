import matplotlib.pyplot as plt
from matplotlib  import cm
import numpy as np
import sys

#This script reads a charmm log file following Hbond analysis
#It then counts the number of Hbond for a given residue and molecule ID (line 17)
#Intended for usage in CHARMM pipeline.

#Name of .log file to search for hbonds.
filename1=str(sys.argv[1])

hbondlist=[]
with open(filename1,'r') as g:
	for line in g:
		if "Parameter: K" in line:
			paramline=line.split()
			resid=(int(paramline[3][1:-1]))
			hbondcount=0
		#Can select molecule ID here
		elif "      MB   " in line:
			hbondcount=hbondcount+1
		elif "incr k by 1" in line:
			hbondlist.append(hbondcount)
	print(len(hbondlist))
