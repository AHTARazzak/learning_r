from string import digits
import math
#requires python2.7
import sys
#READS THE XVG FILE
#need to put script file in same directory as the avg

#Reads an multiple .xvg files and returns the average and dihedral angle across all .xvg files

#Name of file name to read
fileread=str(sys.argv[1])
#Name of filename to output to
file=str(sys.argv[3])

filewrite=open(file,'w')
for i in range(1,54):
	linecount=0
	secondlinecount=0
	total=0
	mean=0
	summation=0
	summationsmaller=0
	standarddeviation=0
	standarderror=0
	numbers=0
	numberstwo=0
	total=0
	with open(fileread+str(i)+".dat") as f:
	#YOU WILL NEED TO EDIT THIS FOR YOUR FILE
	#what xvg stuff its reading
		for line in f:
			if "@" not in line:
				if "#" not in line:
					linesplit=line.split()
					linecount=linecount+1
					if len(linesplit)>1:
						numbers=numbers+1
						total=total+float(linesplit[2])

	mean=float(total/(numbers))
	print "mean is: "+str(mean)
	filewrite.write(str(float(i))+" "+str(mean)+"\n")
