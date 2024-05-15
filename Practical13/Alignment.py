import blosum as bl #import library
matrix = bl.BLOSUM(62) #make a blosum62 matrix
blosum62_dict = {(f"{k1}{k2}"): v for k1, row in matrix.items() for k2, v in row.items()} #transform the matrix into a dictionary
human=""#Initialize three variables
mouse=""
rat=""
#Read 3 files and extract the sequence data
with open("/Users/submerge/IBI1_2023-24/Practical13/SLC6A4_HUMAN.fa", 'r') as file:
    for line in file:
        if line.startswith('>'):
            continue #skip the description
        human+=line.strip()
with open("/Users/submerge/IBI1_2023-24/Practical13/SLC6A4_MOUSE.fa", 'r') as file:
    for line in file:
        if line.startswith('>'):
            continue
        mouse+=line.strip()
with open("/Users/submerge/IBI1_2023-24/Practical13/SLC6A4_RAT.fa", 'r') as file:
    for line in file:
        if line.startswith('>'):
            continue
        rat+=line.strip()
def alignment(human, mouse, rat, blosum62_dict): 
    #define a function to calculate alignment score and percentage of similarity
    h_and_m_score = 0 #Initialize all value to be 0
    h_and_r_score = 0
    m_and_r_score = 0
    h_and_m_similarity = 0
    h_and_r_similarity = 0
    m_and_r_similarity = 0
    for i in range(len(human)): #iterate each amino acid in 3 sequeces
        h_and_m_letter = human[i] + mouse[i]
        h_and_r_letter = human[i] + rat[i]
        m_and_r_letter = mouse[i] + rat[i]
        #sum up the score according to the blosum62 
        h_and_m_score += blosum62_dict.get(h_and_m_letter, 0)
        h_and_r_score += blosum62_dict.get(h_and_r_letter, 0)
        m_and_r_score += blosum62_dict.get(m_and_r_letter, 0)
        #search for same amino acids
        if human[i] == mouse[i]:
            h_and_m_similarity += 1
        if human[i] == rat[i]:
            h_and_r_similarity += 1
        if mouse[i] == rat[i]:
            m_and_r_similarity += 1
    h_and_m_similarity /= len(human) #count the percentage of similarity
    h_and_r_similarity /= len(human)
    m_and_r_similarity /= len(human)
    return h_and_m_score, h_and_r_score, m_and_r_score,h_and_m_similarity,h_and_r_similarity,m_and_r_similarity
scores = alignment(human, mouse, rat, blosum62_dict)
print(f"Human vs Mouse alignment score: {scores[0]}, percentage of identical amino acids: {scores[3]}")
print(f"Human vs Rat alignment score: {scores[1]}, percentage of identical amino acids: {scores[4]}")
print(f"Mouse vs Rat alignment score: {scores[2]}, percentage of identical amino acids: {scores[5]}")