import matplotlib.pyplot as plt
from matplotlib  import cm
import numpy as np
import sys

filename1=str(sys.argv[1])
filename2=str(sys.argv[2])
e1list=[]
e2list=[]
e3list=[]
e4list=[]
with open(filename1,'r') as g:
	for line in g:
		if "Parameter: E1" in line:
			esplit=line.split()
			#print(esplit)
			e1list.append(float(esplit[3][1:-1]))
		elif "Parameter: E2" in line:
			esplit=line.split()
			e2list.append(float(esplit[3][1:-1]))
		elif "Parameter: E3" in line:
			esplit=line.split()
			e3list.append(float(esplit[3][1:-1]))
		elif "Parameter: E4" in line:
			esplit=line.split()
			e4list.append(float(esplit[3][1:-1]))
#	e1list.pop(0)
#	e1list.pop(1)
#	e1list.pop(2)
#	e1list.pop(3)
#	e1list.pop(3)
	writefilevdw=open(filename2+"leu89VDWmb.dat","a")
	writefiledih=open(filename2+"leu89DIHmb.dat","a")
	writefileele=open(filename2+"leu89ELEmb.dat","a")
	writefileall=open(filename2+"leu89ALLmb.dat","a")
	for element in e1list:
		writefilevdw.write(str((float(element)))+"\n")
	for element in e2list:
		writefiledih.write(str((float(element)))+"\n")
	for element in e3list:
		writefileele.write(str((float(element)))+"\n")
	for element in e4list:
		writefileall.write(str((float(element)))+"\n")
