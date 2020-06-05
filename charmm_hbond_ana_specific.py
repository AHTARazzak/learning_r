import subprocess
import sys
import os
import math

#This script runs charmm for hbond analysis for specific residues as selected in aaresidue (line 12)
#Intended for use with charmm pipeline.
#Only parsable for someone with charmm expertise.

#File format to be read
filename=str(sys.argv[1])
aalist=[6,7,14,36,45,54,139,146]
resid=0
for i in range(1,53):
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

open unit 51 read unform name 1000umbln-"""+str(i)+""".dcd
traj firstu 51 nunit 2 skip 250 !
traj read
update cutnb 14.0 ctonnb 10.0 ctofnb 12.0 fshift vshift cdie
DEFIne backbone SELEct TYPE N  .OR. TYPE CA .OR. TYPE C .OR. TYPE HN .OR. TYPE HA .OR. TYPE CB END
label loopb
        set k 1
        label loopc
                coor hbond verbose sele resid @k .and. .not. resn HEME .and. .not. backbone end sele segid MB .and. .not. resid @k .and. .not. backbone end
                incr k by 1
        if k lt 154 goto loopc
STOP
""")
		f.close
	os.system("charmmc42a<hbondanaproc.inp>whateverhbnew"+str(i)+".dat")
	with open('whateverhbnew'+str(i)+'.dat', 'r') as g:
		for line in g:
			if "Parameter: K" in line:
				paramline=line.split()
				resid=(int(paramline[3][1:-1]))
				residdict={}
			elif int(resid) in aalist:
				if "      MB   " in line:
					hbline=line.split()
					if int(hbline[7]) in residdict:
						residdict[int(hbline[7])]+=1
					else:
						residdict[int(hbline[7])]=1
				writefilehbond=open(filename+"hbondspecn"+str(resid)+"_"+str(i)+".dat","w")
				residdictstr=str(residdict)
				residdictstr=residdictstr[1:-1]
				residdictstr=residdictstr.replace(',','\n')
				residdictstr=residdictstr.replace(':','')
				writefilehbond.write(str(residdictstr)+"\n")

	#hbondlist.pop(0)
	#writefilehbond=open(filename+"hbondn"+str(i)+".dat","a")
	#for element in hbondlist:
		#writefilehbond.write(str(round(float(element)))+"\n")

