from string import digits
import math
#requires python2.7
import sys
import statistics

#READS THE XVG FILE
#need to put script file in same directory as the avg
#This file returns the mean, standard deviation, and standard error for data from determined point to the next (as specific line 19 and 21)
#Output in terminal

linecount=0
total=0
mean=0
summation=[]
summationsmaller=0
standarddeviation=0
standarderror=0
fromhere=1
#CHANGE FROMHERE TO CHANGE THE START POINT
tohere=12836
#CHANGE TOHERE TO CHANGE THE END POINT
secondlinecount=0
#This is the name of he file to be opened & analysed.
fileread=str(sys.argv[1])
numbers=0

with open(fileread) as f:
#YOU WILL NEED TO EDIT THIS FOR YOUR FILE
#what xvg stuff its reading
	for line in f:
		if "@" not in line:
			if "#" not in line:
				linesplit=line.split()
				linecount=linecount+1
				if linecount>=fromhere and linecount<=tohere:
					if len(linesplit)>1:
						numbers=numbers+1
						total=total+float(linesplit[1])

mean=float(total/(numbers))
print ("mean is: "+str(mean))
print ("N is: "+str(fromhere)+" to "+str(tohere)+" or is actually "+str(tohere-fromhere))
numbers=0
with open(fileread) as f:
#what xvg stuff its reading
	for line in f:
		if "@" not in line:
			if "#" not in line:
				linesplit=line.split()
				summation=summation+[float(linesplit[1])]
len(summation)
print ("Summation total is: " + str(sum(summation)))
print ("Summation total divided by sample number: " + str(sum(summation)/len(summation)))
standarddeviation=statistics.stdev(summation)
print ("Standard deviation is: " + str(standarddeviation))

standarderror=standarddeviation/math.sqrt(tohere-fromhere)
print ("Standard error is: " + str(standarderror))
