import subprocess
import sys
import os
import math

#This script runs charmm for hbond analysis for each residue
#Intended for use with charmm pipeline.
#Only parsable for someone with charmm expertise.

#File format to be read
filename=str(sys.argv[1])

for i in range(1,53):
	hbondlist=[0]*154
	with open('hbondanaproc.inp','w') as f:
		f.write("""* MbXe4
* Project: relaxation trajectories after Xe removal
*

BOMLev -1

!==========read topology,parameter,psf,coordinates============
READ RTF  CARD NAME top.inp
READ PARA CARD NAME par.inp
READ PSF  CARD NAME 0100.psf
READ COOR CARD NAME 0100.crd
update cutnb 14.0 ctonnb 10.0 ctofnb 12.0 fshift vshift cdie

open unit 51 read unform name """+filename+"""umbln-"""+str(i)+""".dcd
traj firstu 51 nunit 2 skip 250 !
traj read
update cutnb 14.0 ctonnb 10.0 ctofnb 12.0 fshift vshift cdie
label loopb
	set k 1
	label loopc
		coor hbond verbose sele resid @k .and. .not. resn HEME end sele segid MB .and. .not. resid @k end
		incr k by 1
	if k lt 154 goto loopc
STOP""")
		f.close
	os.system("charmmc42a<hbondanaproc.inp>whateverhb"+str(i)+".dat")
	with open('whateverhb'+str(i)+'.dat', 'r') as g:
		for line in g:
			if "Parameter: K" in line:
				paramline=line.split()
				resid=(int(paramline[3][1:-1]))
				hbondcount=0
			elif "      MB   " in line:
				hbondcount=hbondcount+1
			elif "incr k by 1" in line:
				hbondlist[resid]=hbondlist[resid]+hbondcount
	hbondlist.pop(0)
	writefilehbond=open(filename+"hbondn"+str(i)+".dat","a")
	for element in hbondlist:
		writefilehbond.write(str(round(float(element)))+"\n")

