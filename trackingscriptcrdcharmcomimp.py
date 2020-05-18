import subprocess
import sys
import os
import math

#in the file you need top.inp par.inp & psf + make sure charmm(line157) correct for how you run charmm in terminal window

#to process track (sits in certain position for at least 10 ps) run trackingscriptprocess.py

#TRACK CODE
#1 = Cav1
#2 = Cav2
#3 = Cav3
#4 = Cav4
#5 = Cav2-1
#6 = Cav2-3
#7 = Cav2-4
#8 = Cav1-3
#9 = dp
#10 = outside
#11 = Cav4-dp

pdbread=str(sys.argv[1])
checkatomname=str(sys.argv[2])
startiterations=int(sys.argv[3])
numberiterations=int(sys.argv[4])
cutoff=int(sys.argv[5])
systemnumber=str(sys.argv[6])
iter=1
for dcdi in range(40,100):
	countone=0
	counttwo=0
	countthree=0
	countfour=0
	countfive=0
	countsix=0
	countseven=0
	counteight=0
	countnine=0
	countten=0
	counteleven=0
	bump=float(50)
	proportionfile=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_tracknumbers.txt","w+")
	cav1disttrack=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_cav1disttrack.txt","w+")
	cav2disttrack=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_cav2disttrack.txt","w+")
	cav3disttrack=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_cav3disttrack.txt","w+")
	cav4disttrack=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_cav4disttrack.txt","w+")
	cav5disttrack=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_cav5disttrack.txt","w+")
	writeit1=open("pdblist1.txt","w+")
	writeit2=open("pdblist2.txt","w+")
	writevecdif1=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_writevecdif1.txt","w+")
	writevecdif2=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_writevecdif2.txt","w+")
	writevecdif1r=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_writevecdif1r.txt","w+")
	writevecdif2r=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_writevecdif2r.txt","w+")
	#cav1
	writevecdifr1r2a=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_writevecdifr1r2.1.txt","w+")
	#cav2
	writevecdifr1r2b=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_writevecdifr1r2.2.txt","w+")
	#cav3
	writevecdifr1r2c=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_writevecdifr1r2.3.txt","w+")
	#cav4
	writevecdifr1r2d=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_writevecdifr1r2.4.txt","w+")
	#cav-dp
	writevecdifr1r2e=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_writevecdifr1r2.5.txt","w+")
	track=open(str(dcdi)+"_"+str(systemnumber)+str(checkatomname)+"_tracking"+str(checkatomname)+".txt","w+")
	for i in range(startiterations,numberiterations+1):
		with open('comsingle.inp','w') as g:
			g.write("""* MbXe4

	BOMLev -1

	!==========read topology,parameter,psf,coordinates============
	READ RTF  CARD NAME top.inp
	READ PARA CARD NAME par.inp
	open unit 10 card read name """+systemnumber+""".psf
	read psf card unit 10
	close unit 10

	open unit 20 card read name """+pdbread+str(dcdi)+"""_"""+str(i)+""".cor
	read coor card unit 20
	close unit 20


	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	!periodic boundaries and cutoffs, SHAKE
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	set 6 65.1907
	set 7 58.9821
	set 8 46.5648

	! reads in image file for translation images
	OPEN UNIT 3 READ CARD NAME waterbox.img
	READ IMAGE UNIT 3
	!IMAGE BYRES XCEN 0.0 YCEN 0.0 ZCEN 0.0 SELE SEGID BULK END
	!IMAGE BYSEG XCEN 0.0 YCEN 0.0 ZCEN 0.0 SELE SEGID TUDO END
	IMAGE BYRES XCEN 0.0 YCEN 0.0 ZCEN 0.0 SELE ALL END

	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	!Minimization and Heating
	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	OPEN UNIT 32 WRITE  FORMATTED NAME  thecom1.dat

	!COOR STAT MASS SELE BYNU 50 END
	define com1 SELE BYNU 1427:1445 .or.  BYNU 1484:1506 .or. BYNU 1619:1637 .or. BYNU 1681:1699 .or. BYNU 2269:2287 .or. BYNU 2460:2532 END
	COOR STAT MASS SELE com1 END

	echu 32
	echo ?xave ?yave ?zave 

	CLOSE UNIT 32

	OPEN UNIT 33 WRITE  FORMATTED NAME  thecom2.dat

	!COOR STAT MASS SELE BYNU 50 END
	define com2 SELE BYNU 1151:1169 .or.  BYNU 1681:1699 .or. BYNU 1735:1764 .or. BYNU 2138:2156 .or. BYNU 2191:2209 .or. BYNU 2460:2532 END
	COOR STAT MASS SELE com2 END

	echu 33
	echo ?xave ?yave ?zave 

	CLOSE UNIT 33

	OPEN UNIT 34 WRITE  FORMATTED NAME  thecom3.dat

	define com3 SELE BYNU 86:109 .or.  BYNU 1187:1205 .or. BYNU 1206:1224 .or. BYNU 1291:1297 .or. BYNU 1315:1331 .or. BYNU 2128:2137 .or. BYNU 2172:2210 END
	COOR STAT MASS SELE com3 END

	echu 34
	echo ?xave ?yave ?zave 

	CLOSE UNIT 34

	OPEN UNIT 35 WRITE  FORMATTED NAME  thecom4.dat

	define com4 SELE BYNU 373:379 .or. BYNU 409:446 .or. BYNU 1055:1061 .or. BYNU 1092:1126 .or. BYNU 1151:1169 .or. BYNU 1735:1753 .or. BYNU 1790:1808 END
	COOR STAT MASS SELE com4 END

	echu 35
	echo ?xave ?yave ?zave 

	CLOSE UNIT 35

	OPEN UNIT 36 WRITE  FORMATTED NAME  thecom5.dat

	define com5 SELE BYNU 428:446 .or. BYNU 734:753 .or. BYNU 1038:1054 .or. BYNU 1092:1107 .or. BYNU 1135:1753 .or. BYNU 2460:2532 END
	COOR STAT MASS SELE com5 END

	echu 36
	echo ?xave ?yave ?zave 

	CLOSE UNIT 36

	stop
	""")
		g.close
		os.system("charmmc41<comsingle.inp>whatever.txt")
		for k in range(1,6):
			with open("thecom"+str(k)+".dat",'r') as cm:
				for line in cm:
					pdbcoor=line.split()
					if k==1:
						vectorindex1=math.sqrt(((float(pdbcoor[0])+bump)**2)+((float(pdbcoor[1])+bump)**2)+((float(pdbcoor[2])+bump)**2))
					if k==2:
						vectorindex2=math.sqrt(((float(pdbcoor[0])+bump)**2)+((float(pdbcoor[1])+bump)**2)+((float(pdbcoor[2])+bump)**2))
					if k==3:
						vectorindex3=math.sqrt(((float(pdbcoor[0])+bump)**2)+((float(pdbcoor[1])+bump)**2)+((float(pdbcoor[2])+bump)**2))
					if k==4:
						vectorindex4=math.sqrt(((float(pdbcoor[0])+bump)**2)+((float(pdbcoor[1])+bump)**2)+((float(pdbcoor[2])+bump)**2))
					if k==5:
						vectorindex5=math.sqrt(((float(pdbcoor[0])+bump)**2)+((float(pdbcoor[1])+bump)**2)+((float(pdbcoor[2])+bump)**2))
		with open(pdbread+str(dcdi)+"_"+str(i)+".cor") as f:
			for line in f:
				splitline=line.split()
				if len(splitline)>3:
					if (splitline[2]==str(checkatomname)):
						vectorindexmain=math.sqrt(((float(splitline[4])+bump)**2+(float(splitline[5])+bump)**2+(float(splitline[6])+bump)**2))
		difference1=math.sqrt(((vectorindexmain)-(vectorindex1))**2)
		difference2=math.sqrt(((vectorindexmain)-(vectorindex2))**2)
		difference3=math.sqrt(((vectorindexmain)-(vectorindex3))**2)
		difference4=math.sqrt(((vectorindexmain)-(vectorindex4))**2)
		difference5=math.sqrt(((vectorindexmain)-(vectorindex5))**2)
		differenceout=math.sqrt(((vectorindexmain)-float(0)))
		cav1disttrack.write(str(i)+" "+str(difference1)+"\n")
		cav2disttrack.write(str(i)+" "+str(difference2)+"\n")
		cav3disttrack.write(str(i)+" "+str(difference3)+"\n")
		cav4disttrack.write(str(i)+" "+str(difference4)+"\n")
		cav5disttrack.write(str(i)+" "+str(difference5)+"\n")
		if differenceout<float(18):
			#1
			if difference1<difference4:
				#1-3
				if difference3<difference2:
					if difference1<difference3:
						if difference1<cutoff:
							countone+=1
							writeit1.write(str(i)+" ")
							writevecdif1.write(str(i)+" "+str(difference1)+"\n")
							writevecdifr1r2a.write(str(difference1)+" "+str(difference2)+"\n")
							track.write(str(i)+" 1"+"\n")
						else:
							counteight+=1
							track.write(str(i)+" 8"+"\n")
					#3-1
					if difference3<difference1:
						if difference3<cutoff:
							countthree+=1
							writeit1.write(str(i)+" ")
							writevecdif1.write(str(i)+" "+str(difference1)+"\n")
							writevecdifr1r2c.write(str(difference1)+" "+str(difference2)+"\n")
							track.write(str(i)+" 3"+"\n")
						else:
							counteight+=1
							track.write(str(i)+" 8"+"\n")
				#1-2
				if difference2<difference3:
					if difference1<difference2:
						if difference1<cutoff:
							countone+=1
							writeit1.write(str(i)+" ")
							writevecdif1.write(str(i)+" "+str(difference1)+"\n")
							writevecdifr1r2a.write(str(difference1)+" "+str(difference2)+"\n")
							track.write(str(i)+" 1"+"\n")
						else:
							countfive+=1
							track.write(str(i)+" 5"+"\n")
					#2-1
					if difference2<difference1:
						if difference2<cutoff:
							counttwo+=1
							writeit2.write(str(i)+" ")
							writevecdif2.write(str(i)+" "+str(difference2)+"\n")
							writevecdifr1r2b.write(str(difference1)+" "+str(difference2)+"\n")
							track.write(str(i)+" 2"+"\n")
						else:
							countfive+=1
							track.write(str(i)+" 5"+"\n")

			#4
			if difference4<difference3:
				if difference4<difference1:
					#4-dp
					if difference4<difference5:
						#4-2
						if difference4<difference2:
							if difference4<cutoff:
								countfour+=1
								writeit2.write(str(i)+" ")
								writevecdif2.write(str(i)+" "+str(difference2)+"\n")
								writevecdifr1r2d.write(str(difference1)+" "+str(difference2)+"\n")
								track.write(str(i)+" 4"+"\n")
							else:
								countseven+=1
								track.write(str(i)+" 7"+"\n")
						#2-4
						if difference2<difference4:
							if difference2<cutoff:
								counttwo+=1
								writeit2.write(str(i)+" ")
								writevecdif2.write(str(i)+" "+str(difference2)+"\n")
								writevecdifr1r2b.write(str(difference1)+" "+str(difference2)+"\n")
								track.write(str(i)+" 2"+"\n")
							else:
								countseven+=1
								track.write(str(i)+" 7"+"\n")
					#dp-4
					if difference5<difference4:
						if difference5<cutoff:
							countnine+=1
							writeit2.write(str(i)+" ")
							writevecdif2.write(str(i)+" "+str(difference2)+"\n")
							writevecdifr1r2e.write(str(difference1)+" "+str(difference2)+"\n")
							track.write(str(i)+" 9"+"\n")
						else:
							countseven+=1
							track.write(str(i)+" 11"+"\n")

			#3-2
			if difference3<difference4:
				if difference3<difference1:
					if difference3<difference2:
						if difference3<cutoff:
							countthree+=1
							writeit2.write(str(i)+" ")
							writevecdif2.write(str(i)+" "+str(difference2)+"\n")
							writevecdifr1r2c.write(str(difference1)+" "+str(difference2)+"\n")
							track.write(str(i)+" 3"+"\n")
						else:
							countsix+=1
							track.write(str(i)+" 6"+"\n")		
					if difference2<difference3:
						if difference2<cutoff:
							counttwo+=1
							writeit2.write(str(i)+" ")
							writevecdif2.write(str(i)+" "+str(difference2)+"\n")
							writevecdifr1r2b.write(str(difference1)+" "+str(difference2)+"\n")
							track.write(str(i)+" 2"+"\n")
						else:
							countsix+=1
							track.write(str(i)+" 6"+"\n")

		else:
			countten+=1
			track.write(str(i)+" 10"+"\n")

	proportionfile.write(checkatomname+" in pocket 1 "+str(countone)+"\n")
	proportionfile.write(checkatomname+" in pocket 2 "+str(counttwo)+"\n")
	proportionfile.write(checkatomname+" in pocket 3 "+str(countthree)+"\n")
	proportionfile.write(checkatomname+" in pocket 4 "+str(countfour)+"\n")
	proportionfile.write(checkatomname+" in pocket dp "+str(countnine)+"\n")
	proportionfile.write(checkatomname+" in pocket 2-1 "+str(countfive)+"\n")
	proportionfile.write(checkatomname+" in pocket 2-3 "+str(countsix)+"\n")
	proportionfile.write(checkatomname+" in pocket 2-4 "+str(countseven)+"\n")
	proportionfile.write(checkatomname+" in pocket 1-3 "+str(counteight)+"\n")
	proportionfile.write(checkatomname+" in pocket 4-dp "+str(counteleven)+"\n")
	proportionfile.write(checkatomname+" in outside "+str(countten)+"\n")
	print checkatomname+" in pocket 1 "+str(countone)
	print checkatomname+" in pocket 2 "+str(counttwo)
	print checkatomname+" in pocket 3 "+str(countthree)
	print checkatomname+" in pocket 4 "+str(countfour)
	print checkatomname+" in pocket dp "+str(countnine)
	print checkatomname+" in pocket 2-1 "+str(countfive)
	print checkatomname+" in pocket 2-3 "+str(countsix)
	print checkatomname+" in pocket 2-4 "+str(countseven)
	print checkatomname+" in pocket 1-3 "+str(counteight)
	print checkatomname+" in pocket 4-dp "+str(counteleven)
	print checkatomname+" in outside "+str(countten)
