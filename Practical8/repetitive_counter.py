seq ="ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
import re
match1=re.findall(r'GTGTGT?',seq)
match2=re.findall(r"GTCTGT?",seq)
number=len(match1)+len(match2)
print(f"The total number of repeat elements within this sequence is {number}.")


