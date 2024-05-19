import re #imoort library
with open("/Users/submerge/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r") as file:
    fasta=file.read() #open and read a fasta file
    names=re.findall(r"gene:(\S+).*duplication",fasta) #find all gene names with "duplication"
    sequences=re.findall(r"duplication.+\n((?:[^>].+\n)+)",fasta) #find all gene sequences with "duplication"
    print(sequences)
a='' #define an empty string to store gene names and sequences
for name,sequence in zip(names,sequences): #iterate every name and sequence
    a+=f'>{name}_mrna\n{sequence}' #append names and sequences into the empty string
with open("/Users/submerge/IBI1_2023-24/Practical8/duplicate_genes.fa", "w", encoding="UTF-8") as file:
    file.write(a) #create a new fasta file to stroe gene names and sequences


    


