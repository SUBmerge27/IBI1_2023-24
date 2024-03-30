mRNA_sequence=input("Please type a mRNA sequence:")
def translate_mRNA_to_polypeptide(mRNA):
    # Define the genetic code as a dictionary
    genetic_code = {'AUG': 'Methionine', 'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop', 'UCA': 'Serine', 'UCC': 'Serine', 'UCG': 'Serine', 'UCU': 'Serine', 'AGC': 'Serine', 'AGU': 'Serine',
'UAC': 'Tyrosine', 'UAA': 'Stop', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UUA': 'Leucine', 'UUG': 'Leucine', 'UUU': 'Leucine', 'UUC': 'Leucine',
'UAG': 'Stop', 'UGG': 'Tryptophan', 'UAU': 'Tyrosine', 'UAA': 'Stop', 'CAC': 'Histidine', 'CAU': 'Histidine', 'GUG': 'Valine', 'GUU': 'Valine',
'CUC': 'Leucine', 'CUU': 'Leucine', 'CAG': 'Glutamine', 'CAA': 'Glutamine', 'GUA': 'Tryptophan', 'GUU': 'Valine', 'GUC': 'Valine', 'GUU': 'Valine',
'GAC': 'Asparagine', 'GAU': 'Asparagine', 'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid', 'GUA': 'Tryptophan', 'GUU': 'Valine', 'GUC': 'Valine',
'GUG': 'Valine', 'UUC': 'Phenylalanine', 'UUU': 'Phenylalanine', 'UUG': 'Leucine', 'UAA': 'Stop', 'AAC': 'Asparagine', 'AAU': 'Asparagine',
'AAA': 'Lysine', 'AAG': 'Lysine', 'AGA': 'Arginine', 'AGG': 'Arginine', 'AUC': 'Isoleucine', 'AUU': 'Isoleucine', 'UGA': 'Stop',
'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'UCU': 'Serine', 'AGC': 'Serine', 'AGU': 'Serine', 'UAC': 'Tyrosine', 'UAA': 'Stop',
'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UUA': 'Leucine', 'UUG': 'Leucine', 'UUU': 'Leucine', 'UUC': 'Leucine', 'UAG': 'Stop', 'UGG': 'Tryptophan',
'UAU': 'Tyrosine', 'CAC': 'Histidine', 'CAU': 'Histidine', 'GUG': 'Valine', 'GUU': 'Valine', 'CUC': 'Leucine', 'CUU': 'Leucine', 'CAG': 'Glutamine',
'CAA': 'Glutamine', 'GUA': 'Tryptophan', 'GUU': 'Valine', 'GUC': 'Valine', 'GUU': 'Valine', 'GAC': 'Asparagine', 'GAU': 'Asparagine',
'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid', 'UUC': 'Phenylalanine', 'UUU': 'Phenylalanine', 'UUG': 'Leucine', 'UAA': 'Stop', 'AAC': 'Asparagine',
'AAU': 'Asparagine', 'AAA': 'Lysine', 'AAG': 'Lysine', 'AGA': 'Arginine', 'AGG': 'Arginine', 'AUC': 'Isoleucine', 'AUU': 'Isoleucine',
    }

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