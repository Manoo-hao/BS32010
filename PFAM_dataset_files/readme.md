#Introduction

This folder contains the dataset downloaded from the PFAM (seed) 
database with the accession number PF01924, as well as documents 
associated with this dataset. A description of the protein family can be 
found [here](pfam.xfam.org/family/PF01924).

###PF01924.pir

The dataset downloaded from PFAM and modified according to the 
instructions given for assignment 2.

###PF01924_pairs100.out

The file resulting from a pairwise alignment of PF01924.pir, using amps 
with 100 randomisation and the blosum62 matrix.

###PF01924.tord/.tree/.ps

Output files from running the program order on PF01924_pairs100.out.

###PF01924_mult.out and PF01924_modified.out
PF01924_mult.out is the file resulting from multiple alignment with 
amps. PF01924_modified.out is the same file with the identifier >P1; 
replaced by the identifier >.

###PF_parser_output.out

A tab delimited table comparable to the one created for the serprot 
dataset in the parent folder.
