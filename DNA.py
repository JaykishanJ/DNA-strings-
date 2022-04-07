#This code will return a specific chunk of nucleotide basis from a given FASTA file based on start and end position
#you have given if you give both as zero than it will print everything in a FASTA file 
def readGenome(filename):
    Genome=""
    with open(filename,'r') as f:
        for line in f:
            if not line[0]=='>':
                Genome+=line.rstrip()
    return Genome
Genome=readGenome(input("Enter a file name:"))
A=int(input("Enter start limit: "))
B=int(input("Enter end limit: "))
if A!=0 and B!=0:
    print (Genome[A:B])
else:
    print(Genome[:])
