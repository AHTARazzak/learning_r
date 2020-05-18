from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import sys
filename1=str(sys.argv[1])
xarray=[]
yarray=[]

count=0
with open('filename') as f:
	for line in f:
		splitline=line.split()
		xarray=xarray+[float(splitline[1])]
		yarray=yarray+[float(splitline[2])]
		count=count+1
		print count

plt.hist2d(xarray, yarray, range=[[-180,180],[-180,180]], bins=90, norm=LogNorm())
plt.colorbar()	
plt.show()
