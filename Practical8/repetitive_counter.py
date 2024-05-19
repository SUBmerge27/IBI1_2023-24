seq ="ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
import re #import libraries
match1=re.findall("GTGTGT",seq)  #find all repetitive sequences
match2=re.findall("GTCTGT",seq)
number=len(match1)+len(match2)  #count the total number
print(f"The total number of repeat elements within this sequence is {number}.")


