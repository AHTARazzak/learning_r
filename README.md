ALI RAZZAK SCRIPT MADE DURING Theoretical chemistry PhD at UNIVERSITY OF BASEL
For "makerama.py" to be run in Python2.7

Takes sequentially ordered list of dihedral angles so in column 1 x axis sequence and column 2 the dihedral angle. Produces 3D histogram of ramachandran plot and outputs onto customisable GUI.

for "makerama.py"
File takes 2 inputs:
1) Fle containing time series of dihedral angles.
2) Number of bins in raster.

for "2dhistopls.py"
(Much more efficient 3d histogram)
takes 1 input:
1) Fle containing time series of dihedral angles.

For "compilegap2.py" to be run in Python3

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
