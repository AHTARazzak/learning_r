import matplotlib.pyplot as plt
from matplotlib  import cm
import numpy as np
import sys

#This file swaps columns 1 and 2 within a file.

#Name of file with columns wanting to swap.
filename1=str(sys.argv[1])
#Name of file outputing to.
filename2=str(sys.argv[2])
outfile=[]
with open(filename1,"r") as f:
	for line in f:
		linesplit=line.split()
		outfile.append(linesplit[1] + " " + linesplit[0] + " " + linesplit[2])

subdccmfile=open(filename2,"w")
for i in outfile:
	subdccmfile.write(i+"\n")
