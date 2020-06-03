import subprocess
import sys
import os
import math

#Needs every single PDB frame sequentially numbered, can extract concat. pdb from dcd or xtc on VMD.
#Can use Ali's script to split up concat pdb file into sequentially #'d pdbs.

#Takes 3 arguments 
#Argument 1 = number of iterations
#Argument 2 = 3d vector number
#Argument 3 = name of file with gap volumes

print "Don't forget to change CHARMM input (in this file)"
print "Don't forget to change SURFNET input (in this file)"


numitrs=int(sys.argv[1])+1
#How many PBD files to iterate through
bump=int(sys.argv[2])
#How much to bump the values out of negatives by (moving origin)
coorcutoff=float(sys.argv[3])
#minimum cutoff for distance between COM and gap (angstroms)
volumecutoff=float(sys.argv[4])
#maximum cutoff for volume of gap gap (angstroms)
gapfilename=str(sys.argv[5])
#outputfile name

count=1
outfile=open(gapfilename+".dat",'w')
for i in range(1,numitrs):
	gapfile=open("selectedgapandcom"+str(count)+".dat",'w')
	with open('surfnet.par','w') as f:
		f.write(""" 
Parameters for SURFNET              (surfnet.par)
----------------------
 
TITLE
Cool stuff and stuff
 
INPUT FILE
0100_break_"""+str(count)+""".pdb

Output files listed below. The information entered for each is as follows.
The numbers in square brackets refer to the notes at the end of the file.
The program names indicate which programs need to be rerun when any of the
parameters are changed.

            <----SURFNET----><-SURFACE-><----------SURFPLOT------------>
                                        Foregrnd  Backgrnd        
                   Atom range            colour    colour     Line 
          File     1st   Last  Contour   /shade    /shade     width  SOLID
Filename  type[1] atom   atom  level[2]  (0-10)[3] (0-10)[3]   [4]  /WIRE

OUTPUT FILES
pro1         S      1    2531   100.0       1         1        0.1
gaps         G      0       0   100.0       8         8        0.1

Program parameters
------------------

SURFNET
 1.68  4.74  -2.17  <- Origin of grid box (to use: set atom range below to 0 0)
-1000 1000     <- Atom range defining grid bounds (0 0 to use origin above)
1.5 1.5 1.5     <- Additional boundary round atom-range/origin (Angstroms)
1.0      <- Grid separation
1.6     <- Minimum radius for gap spheres (in Angstroms)
4.2     <- Maximum radius for gap spheres (in Angstroms)
N         <- (C)CP4, (I)nsightII, (Q)uanta, (S)ybyl contour files, or (N)one
Y         <- Calculate gap volume - (Y/N)?
1.0       <- Scaling factor

SURFACE
(Currently no additional parameters)

SURFPLOT
C             <- (C)olour/(B)&W Postscript file, (P)DB-format, (R)aster3D
11            <- Background colour
12            <- Colour of "walls" in back-projections
A             <- (F)loor, (L)eft wall, (R)ight wall, (A)ll three, (N)one
Y             <- Display foreground object (Y/N)?
Y             <- Margin round object - (Y/N)?
0.20          <- Atom radius (in Angstroms) for plot - NOT USED
N             <- Print sequential numbers by the atoms (Y/N)?
Y             <- Maintain x-,y-,z-axes (ignore matrix below) (Y/N)?
 0.0          <- Rotation about x-axis
 0.0          <- Rotation about y-axis
 0.0          <- Rotation about z-axis
 1.0000   0.0000    0.0000             <-
 0.0000   1.0000    0.0000             <- Transformation matrix
 0.0000   0.0000    1.0000             <-
  50.0 100.0 100.0    <- Position of light-source
 40 32         <- Raster3D size, number of tiles in x and y (Max: 80 64)
N              <- Infinite planes for back wall(s) in Raster3d (Y/N)?



---------------------------------------------------------------------------

Notes:-

Note 1. type is one of the following characters:-
    A - Atoms only, each atom will be plotted as a sphere
    a - As for A, but atoms coloured according to B-factor (0-80)
    B - Bonds between atoms
    C - Contours generated according to the density of atoms
    E - Contours generated according to the B-values
    G - Gap map (see below)
    J - Each atom coordinate is joined to the one before and after it
    P - Pairs distribution where each sidechain is shown (by bonds
        joining the atoms) separately
    S - Surface contours at van der Waals radius of each atom (contour
        level of 100.0). If an asterisk, *, follows the S, then the
        radius of each atom will be picked up from the B-value column
        of the PBD file. Otherwise, the default van der Waals radii are
        used.
    % - As C above, but all density values in the output grid are
        adjusted such that the value at each grid-point gives the
        percentage of non-zero grid-points with lower values.

For a Gap map (type G) the first number after it refers to which file is to
be used for generating gaps from. If this is a zero, then gaps are required
between ALL atoms. The second number after the G should be a zero.

For a surface contour (type S), each atom/data-point can have its own
radius defined in the B-value column of the PDB file. This will be used if
there is an asterisk, *, before the S.

Note 2. The contour level can be entered as a percentage by entry of a %
after the contour value.

Note 3. Colours can be entered separately for the foreground and projected
objects. The colours are as follows:

   0=white, 1=yellow, 2=cyan, 3=lime green, 4=green, 5=blue, 6=pink,
   7=orange, 8=red, 9=purple, 10=black, 11=Light blue, 12=Cream

If the colour PostScript option in SURFPLOT below is set to N, the colour
values will be interpreted as grey shades (0=white to 10=black).

If the colour is entered as -999 for the foreground object, the object will
not be displayed. Similarly, for the background projections

For "atom" objects (displayed as spheres), if the colour is set between -1
and -10, a single point, of the corresponding colour, will be plotted
rather than a sphere.

For SOLID surfaces, if in black and white, a negative colour causes all
polygons to be shaded white, giving a sketched, cartoon appearance.

If a 'G' is entered after the background colour, then the background
object will be displayed in grey (ie as shadow) for a colour PostScript
file.

Note 4. Line widths can be set to any real number (a sensible range being
0.0-5.0). The widths of the projected lines will be a fifth of those for
the foreground object.
""")
	f.close
	with open('comsingle.inp','w') as g:
		g.write("""* MbXe4
* Project: relaxation trajectories after Xe removal
*

BOMLev -1

!==========read topology,parameter,psf,coordinates============
READ RTF  CARD NAME top.inp
READ PARA CARD NAME par.inp
open unit 10 card read name 0100.psf
read psf card unit 10
close unit 10

open unit 20 card read name 0100_break_"""+str(count)+""".pdb
read coor pdb unit 20
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

OPEN UNIT 32 WRITE  FORMATTED NAME  thecom.dat

!COOR STAT MASS SELE BYNU 50 END
define com1 SELE BYNU 1427:1445 .or.  BYNU 1484:1506 .or. BYNU 1619:1637 .or. BYNU 1681:1699 .or. BYNU 2269:2287 .or. BYNU 2460:2532 END
COOR STAT MASS SELE com1 END

echu 32
echo ?xave ?yave ?zave 

stop
""")
	g.close
	os.system('./surfnet')
	os.system("charmmc41<comsingle.inp>whatever.txt")
	gapslist=[]
	subtractedgaplist=[]
	linecount=0
	with open('gaps.pdb','r') as v:
		gapcount=0
		with open("thecom.dat",'r') as cm:
				for line in cm:
					pdbcoor=line.split()
					#pdbvector=math.sqrt(((float(pdbcoor[0])+bump)**2)+((float(pdbcoor[1])+bump)**2)+((float(pdbcoor[2])+bump)**2))
					#print "first loop"
		for line in v:
			#print pdbvector
			splitgaps=line.split()
			gapslist+=[math.sqrt((((float(splitgaps[5]))+bump)-(float(pdbcoor[0])+bump))**2+(((float(splitgaps[6]))+bump)-(float(pdbcoor[1])+bump))**2+(((float(splitgaps[7]))+bump)-(float(pdbcoor[2])+bump))**2)]
			#gapslist+=[abs(abs(gapvector)-abs(pdbvector))]
			#print "second loop"
			#print gapslist
	v.close
	#print "next"
	with open('gaps.pdb','r') as h:
		for line in h:
			if linecount==(gapslist.index(min(gapslist))):
				#print gapslist
				#print gapslist.index(min(gapslist))
				#print "NICEONE"
				splitgapsnew=line.split()
				#print gapslist[linecount]
				if gapslist[linecount]>coorcutoff:	 
					outfile.write("\n")
					gapfile.write("nothing")
				elif float(splitgapsnew[10])>volumecutoff:	
					outfile.write("\n")
					gapfile.write("nothing")
				else:
					outfile.write(str(count) + " " + splitgapsnew[10]+"\n")
					gapfile.write(line+"\n"+"HETATM 1280  XE  GAP    19      "+str(round(float(pdbcoor[0]),3))+"   "+str(round(float(pdbcoor[1]),3))+"   "+str(round(float(pdbcoor[2]),3))+"  1.00  0.00        54.000")
			linecount+=1
		count=count+1
	h.close
	os.system('mv gaps.pdb gaps'+str(count-1)+'.pdb')

#improvements
#output com to a single file, frame by frame

