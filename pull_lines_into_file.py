import matplotlib.pyplot as plt
from matplotlib  import cm
import numpy as np
import sys

#File pulls lines (as specified in aalist) into seperate files (see line 19).
#Intended to be used with series of files and structural bioinformatic pipeline.

#File format of series of pdb files reading.
filename=str(sys.argv[1])
aalist=[7,27,31,36,37,45,56,60,62,85,89,104,135,137,138,139]
for i in range(1,52):
	count=0
	with open(filename+str(i)+".xvg") as f:
		for line in f:
			count=count+1
			if count in aalist:
				linesplit=line.split()
                #can change name of writeilfe.
				writefile=open(filename+"resid"+str(count)+".dat","a")
				writefile.write(str(i)+" "+str(linesplit[1])+"\n")
