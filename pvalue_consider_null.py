import matplotlib.pyplot as plt
from matplotlib  import cm
import numpy as np
import sys
from scipy.stats import iqr
from scipy import mean
from scipy import stats

#This file finds the p-value of data and determines whether to reject or accept null hypothesis.
#Can modualte significance on line 24.

#Name of file to process.
filename=str(sys.argv[1])

emptyarray=[]
with open(filename) as f:
	for line in f:
		linesplit=line.split()
		emptyarray.append(float(linesplit[1]))

for element in emptyarray:
	result=(stats.ttest_ind(emptyarray,[element,element]))
	if result.statistic > 0:
		if (result.pvalue/2)<0.1:
			print(str(emptyarray.index(float(element)))+" "+str(result.pvalue/2))
