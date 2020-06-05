import matplotlib.pyplot as plt
from matplotlib  import cm
import numpy as np
import sys

#This file gets the ABSOLUTE difference in DCCM between two files

#DCCM File one contents.
filename1=str(sys.argv[1])
#DCCM File two contents.
filename2=str(sys.argv[2])
#File with outputted difference for each atom pair.
filename3=str(sys.argv[3])

subdccmfile=open(filename3,"w")
list1=[]
list2=[]
with open(filename1) as f:
	for line in f:
		if len(line)>0:
			list1.append(line)

with open(filename2) as f:
	for line in f:
		if len(line)>0:
			list2.append(line)

thefile=[]
for element1 in list1:
	listele1=element1.split()
	for element2 in list2:
		listele2=element2.split()
		if (listele1[0:2]==listele2[0:2]):
			if ((len(listele1)>0) and (len(listele2)>0)):
				thefile.append(str(listele1[0])+" "+str(listele1[1])+" "+str(abs((abs(float(listele1[2])))-(abs(float(listele2[2])))))+"\n")
			else:
				if ((len(listele1)>0) and (len(listele2)>0)):
					thefile.append(str(listele1[0])+" "+str(listele1[1])+" "+str(abs(float(listele1[2])))+"\n")
				if ((len(listele1)>0) and (len(listele2)>0)):
					thefile.append(str(listele2[0])+" "+str(listele2[1])+" "+str(abs(float(listele2[2])))+"\n")
noduplicatebig=""
for element in list1:
	splitelement=element.split()
	if len(splitelement)>0:
		noduplicatebig+=(splitelement[0]+"|"+splitelement[1]+' '+str(abs(float(splitelement[2])))+"\n")
for element in list2:
	splitelement=element.split()
	if len(splitelement)>0:
		noduplicatebig+=(splitelement[0]+"|"+splitelement[1]+' '+str(abs(float(splitelement[2])))+"\n")
noduplicatebig=noduplicatebig.split('\n')
noduplicatebig = list(dict.fromkeys(noduplicatebig))

onlyonetwo=[]
parsedlist=[]
for i in noduplicatebig:
	onetwo=i.split()
	if len(onetwo)>0:
		onlyonetwo.append(onetwo[0])
for thing in noduplicatebig:
	thething=thing.split(" ")
	if (onlyonetwo.count(thething[0]))<2:
		parsedlist.append(thing.replace("|"," "))

actualparse=[]
for i in parsedlist:
	if len(i)>0:
		actualparse.append(i)

thefile = list(dict.fromkeys(thefile))
newlines=[]
for i in thefile:
	thelines=i.split()
	if float(thelines[2])>0:
		newlines.append(i)
newlines=newlines+actualparse

for line in sorted(newlines, key=lambda line: float(line.split()[2])):
	subdccmfile.write(line.strip()+"\n")
