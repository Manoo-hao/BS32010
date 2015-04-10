#Project report

This folder contains files associated with the final report of the 
module BS32010 Applied Bioinformatics.

##Files


###dge_markdown

An R-markdown file that is largely the markdown file used by Dr. 
Schofield in one of her workshops. A few subtle changes have been made, 
most importantly referring to the full RNAseq data as opposed to the 
data used in the workshop.

###homologs_list

An xls-file exported from ensembl - biomart containing all identified 
homologs of the species used for this report, including the homology 
type for each.

###ntt-copy

A list of the top 50 most differentially expressed genes and associated 
parameters. The file was exported from Rstudio after a differential 
expression analysis using edgeR.

###treebuilding

An R-markdown file based on the code provided in the phylogeny workshop.


##Folders

###Aligned sequences

Contains files with aligned amino acid sequences of the identified 
homologs after alignment with T-coffee Expresso.

###Raw sequences

Contains the unaligned amino acid and DNA sequences of the identified 
homologs.

###Structures

Contains .pdb files of a crystal structure that was retrieved from the 
protein databank(PDB) as a model, and a structure of a homolog that was 
modelled based on it. Furthermore, sequential chimera-sessions were 
added in order to reconstruct illustrations used in the report.
