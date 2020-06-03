ALI RAZZAK SCRIPT MADE DURING Physical Chemistry PhD at UNIVERSITY OF BASEL
For "combine_column_1s.py" to be run in Python2.7

Takes the first row of two files [x] and [y] and combines them into a single file with two rows [x y]. Particularly usefulin preperation for the "make_ramachandran.py" script.

for "makerama.py"
File takes 2 inputs:
1) File one containing column.
2) File two containing column.
3) File three combination of column 1 from both files.

For "make_ramachandran.py" to be run in Python2.7

Takes sequentially ordered list of dihedral angles so in column 1 x axis sequence and column 2 the dihedral angle. Produces 3D histogram of ramachandran plot and outputs onto customisable GUI.

for "makerama.py"
File takes 2 inputs:
1) Fle containing time series of dihedral angles.
2) Number of bins in raster.

for "generic_make_3d_histogram.py"
(Much more efficient 3d histogram)
takes 1 input:
1) Fle containing time series of dihedral angles.

For "calculate_cavity_cutoff_SURFNET.py" to be run in Python3

This cavity calculation script requries:
1) a working local compilation of CHARMM all atom simulation engine - see line 157 to make changes in exectuable.
2) a working local (in directory) installation of SURFNET (https://omictools.com/surfnet-tool)
Works best in tandem with https://github.com/ternlef11/Break_concat_pdb.git to break up concatenated pdb file and name files sequentially.
the specifications of the protein for surfnet should be modified for at line 42, the parameters about lines 63 to 67 can also be tinkered with depending on cae.
The charmm specifications should be adapted to circumstance (lines 168-201)
perhaps the charmm exectubale also might need specification depending on user version (line 210)

The scripts takes 5 inputs:
1) number of pdb files to itterate through
2) the bump number (incase of negative atom coordinates)
3) Cutoff for cavity selection
4) Upper volume cutoff
5) Name of output cavity file name

For "trackingscriptcrdcharmcomimp.py" to be run in Python3

This tracking script requries a working local compilation of CHARMM all atom simulation engine - see line 157 to make changes in exectuable.
This file tracks a atom within myoglobin and assigns it into 11 different possible allocations as defined by literature. It writes the atom assignment into 1 of the 11 allocations for every pdb file.
The system use and cavity allocation can be modulated, see line 66 onwards.

The assignments are:

1) Cavity 1
2) Cavity 2
3) Cavity 3
4) Cavity 4
5) Between cavity 2 and 1
6) Between cavity 2 and 3
7) Between cavity 2 and 4
8) Between cavity 1 and 3
9) Distal pocket
10) Outside proint
11) Between cavity 4 and distal pocket

The scripts takes 6 inputs:
1) the pdb name format (it assumes serial numbers at end, perhaps use following: https://github.com/ternlef11/Break_concat_pdb.git
2) Atom name to be tracked
3) Which pdb to start the track from (int)
4) Number of frames (from to track from starting) (int)
5) Cutoff for cavity assignments
6) System number (consider removing and change where applicable in script for your circumstance)
