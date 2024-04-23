import re
with open(r"/Users/submerge/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa") as file:
    matching_lines = []
    for line in file:
        matching_lines+=line
    title=re.findall(r">.*?]","".join(matching_lines))
    