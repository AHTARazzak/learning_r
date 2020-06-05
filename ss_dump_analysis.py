import subprocess
import sys
import os
import math
from collections import Counter
import operator

#This file reads the secondary structure association for each residue and prints it out into a time series format (see line 20).
#Intended to be used in groamcs pipeline. Need output from gmx ss_dump http://manual.gromacs.org/archive/5.0.5/programs/gmx-do_dssp.html.
#Need -dump command output to be read.

#Reads ss dump output.
filename=str(sys.argv[1])
#Saves to this file.
fileout=str(sys.argv[2])
#Can change number of frames in time series.
for i in range(1,53):
	with open(filename+"_"+str(i)+".dat",'r') as g:
		count=0
		#Can change number of amino acids to analyse from 153.
		collarray=[""]*153
		for line in g:
			lineelement=[]
			if count>1:
				colcount=0
				for element in line:

					collarray[colcount]=str(collarray[colcount])+str(element)
					colcount=colcount+1

			count=count+1
	writefile=open(str(fileout+"_"+str(i)),"a")
	for item in range(0,152):
		k=(Counter(collarray[item]))
		j=(str([max(k.items(), key=operator.itemgetter(1))[0]])[2])
		if j=="~":
			writefile.write(str(1)+"\n")
		elif j=="B":
			writefile.write(str(2)+"\n")
		elif j=="G":
			writefile.write(str(3)+"\n")
		elif j=="H":
			writefile.write(str(4)+"\n")
		elif j=="E":
			writefile.write(str(5)+"\n")
		elif j=="I":
			writefile.write(str(6)+"\n")
		elif j=="S":
			writefile.write(str(7)+"\n")
		elif j=="T":
			writefile.write(str(8)+"\n")
