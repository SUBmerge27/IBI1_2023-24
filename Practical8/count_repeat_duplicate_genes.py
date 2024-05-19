import re #IMPORT re MODULE
user_input=input("Please enter one of the two repetitive sequences ('GTGTGT' or 'GTCTGT'): ")
#Prompt the user to enter one of the two repetitive sequences
with open("/Users/submerge/IBI1_2023-24/Practical8/duplicate_genes.fa", "r", encoding="UTF-8") as file1:
    content=file1.read() #Open the file with the path and read its content
    one_line_seqs=[] #Initialize lists to store one-line sequences, filtered sequences, counts, names, and sequences
    filtered_seqs=[]
    count_list=[]
    names=[]
    seqs_and_names=re.findall(r">.+\n(?:[^>].+\n)+",content) #transform the seq and name of each gene into  a list
    for seq_and_name in seqs_and_names:
        one_line_string="".join(seq_and_name.splitlines())
        one_line_seqs.append(one_line_string) #integrate into one row
    for one_line_seq in one_line_seqs:
        if f"{user_input}" in one_line_seq:
            filtered_seqs.append(one_line_seq)  #find seqs and names containing repetitive sequences
    for element1 in filtered_seqs:
        number=element1.count(f"{user_input}") 
        count_list.append(number)  #count the number of instances of the given repetitive
    for element2 in filtered_seqs: #extract gene names
        names=[re.match(r">.+_mrna", element2).group() for element2 in filtered_seqs]
    for element3 in filtered_seqs: #extract gene sequences
        sequences=[re.sub(r"^>.+_mrna", "", element3) for element3 in filtered_seqs]
    output=""
    for count,name,sequence in zip(count_list,names,sequences):
        output+=f"{name} The number of instances of the given repetitive is {count}\n{sequence}\n"
with open(f"/Users/submerge/IBI1_2023-24/Practical8/{user_input}.fa", "w", encoding="UTF-8") as file2:
    file2.write(output)