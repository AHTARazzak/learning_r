import matplotlib.pyplot as plt
from matplotlib  import cm
import numpy as np
import sys
from scipy.stats import iqr
from scipy import mean

#This script finds the upper and lower quartiles of data.
#Does it for second column and must only contain data values.

#Name of file to find quartiles for.
filename=str(sys.argv[1])

emptyarray=[]
with open(filename) as f:
	for line in f:
		linesplit=line.split()
		emptyarray.append(float(linesplit[1]))

themean=mean(emptyarray)
halfiqr=(iqr(emptyarray))/2

upperq=themean+halfiqr
lowerq=themean-halfiqr
for value in emptyarray:
	if float(value)>upperq:
		print(emptyarray.index(float(value)))
