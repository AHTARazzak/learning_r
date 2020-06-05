from string import digits
import math
#requires python2.7
from string import digits
import sys

#READS THE XVG FILE
#need to put script file in same directory as the avg
#This file returns the mean, standard deviation, and standard error for entire file per section for series of files.
#section sizes dtermined line 25 and 27 (250 right now but can be changed)
#Output in terminal and to file (see line 62)

#file format of series of files
fileout=str(sys.argv[2])
with open(fileout,'a') as g:
	for i in range(1,53):
		print "i is "+str(i)
		linecount=0
		total=0
		mean=0
		summation=0
		summationsmaller=0
		standarddeviation=0
		standarderror=0
		fromhere=(250*i)-250
		#CHANGE FROMHERE TO CHANGE THE START POINT
		tohere=250*i
		#CHANGE TOHERE TO CHANGE THE END POINT
		secondlinecount=0
		fileread=str(sys.argv[1])

		with open(fileread) as f:
			for line in f:
				if "@" not in line:
					if "#" not in line:
						linesplit=line.split()
						linecount=linecount+1
						if linecount>=fromhere and linecount<=tohere:
							if len(linesplit)>1:
								total=total+float(linesplit[1])

		mean=float(total/(tohere-fromhere))
		print "mean is: "+str(mean)
		print "N is: "+str(fromhere)+" to "+str(tohere)+" or is actually "+str(tohere-fromhere)

		with open(fileread) as f:
		#what xvg stuff its reading
			for line in f:
				if "@" not in line:
					if "#" not in line:
						linesplit=line.split()
						secondlinecount=secondlinecount+1
						if len(linesplit)>1:
							if secondlinecount>=fromhere and secondlinecount<=tohere:
								summation=summation+math.sqrt(((float(linesplit[1])-float(mean)))**2)

		summationsmaller=(summation/(tohere-fromhere))
		standarddeviation=math.sqrt(summationsmaller)
		print "Standard deviation is: " + str(standarddeviation)

		standarderror=standarddeviation/math.sqrt(tohere-fromhere)
		g.write(str(i) + " " + str(mean) + " " + str(standarddeviation)+"\n")
