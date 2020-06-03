import subprocess
import sys

#Combines the first column of two files [x] and [y] into a single file with two columns [x y]

xydone=""
#Name of first file
file1=str(sys.argv[1])
#Name of second file
file2=str(sys.argv[2]) 
#Final file with combined columns
fileout=str(sys.argv[3])

open1=open(file1, 'r')
open2=open(file2, 'r')
newarray=[]
for line in open1:
	splitline=line.split()
	newarray.append(splitline[1])
	
for line in open2:
	splitline=line.split()
	xydone=xydone + newarray[count]+"  "+splitline[1]+"\n"
open(fileout,'w').write(xydone)
