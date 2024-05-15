mRNA_sequence=input("Please type a mRNA sequence:")
def translate_mRNA_to_polypeptide(mRNA):
    # Define the genetic code as a dictionary
    genetic_code = {
    'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine',
    'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGA': 'Stop', 'UGG': 'Tryptophan',
    'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine',
    'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline',
    'CAU': 'Histidine', 'CAC': 'Histidine', 'CAA': 'Glutamine', 'CAG': 'Glutamine',
    'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine',
    'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Isoleucine', 'AUG': 'Methionine',
    'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine',
    'AAU': 'Asparagine', 'AAC': 'Asparagine', 'AAA': 'Lysine', 'AAG': 'Lysine',
    'AGU': 'Serine', 'AGC': 'Serine', 'AGA': 'Arginine', 'AGG': 'Arginine',
    'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine',
    'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine',
    'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid', 'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid',
    'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine'}

    # Initialize the polypeptide sequence
    polypeptide = ""
    # Find the start codon (AUG)
    for i in range(len(mRNA)):
        if mRNA[i:i+3] == 'AUG':
            start_index = i
            break

    # Translate the mRNA sequence from the start codon to the stop codon
    for i in range(start_index, len(mRNA), 3):
        codon = mRNA[i:i+3]
        if codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
                # Stop codon found, end the translation
            break
        else:
                # Add the corresponding amino acid to the polypeptide sequence
            polypeptide += genetic_code[codon]+", "
 

    return polypeptide

polypeptide_sequence = translate_mRNA_to_polypeptide(mRNA_sequence)
print("Polypeptide sequence:", polypeptide_sequence)