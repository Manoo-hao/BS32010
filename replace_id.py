#Replacing the >P1; identifier with the standard fasta-identifier '>' in order to make a amps-processed multiple alignment loadable in jalview.
PF01924 = open("PF01924_mult100.out","r") #open file PF01924_mult100.out in read mode and store in variable PF01924
content = PF01924.read() #read the file, stored in the variable, and store the file-content in the variable content
newfile = open("PF01924_modified.out","w") #open the new file Pf01924_modified.out in write mode and store it in the variable newfile
newfile.write(content.replace(">P1;",">")) #write into newfile the content of the original file while replacing the old identifier >P1; by the new identifyer >
#close the files
PF01924.close()
newfile.close()

#there are definitely better ways of doing this since there could be hidder >P1; in the text somewhere.
#Ideally it the content should be read line by line with a filehandle.readline, and the block where
#the aligned proteins are listed specified to avoid the reading of lines that are outside this block altogether.