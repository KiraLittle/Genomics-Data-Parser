
"""
Extract:
- Sequence ID 
-Description (gene Name)
-Sequence
-Length of sequence
-Organism, isoform, version
-group transcripts by gene
-translate DNS to Protein
-Calculating base composition or amino acid frequency
-plot:
    -sequence length distribution
    -GC content
    -number  of transcripts
-export result to .json         
"""

from Bio import SeqIO
from collections import defaultdict
import re

gene_dict= dict(list)



reversedTranscript_RNA = "/Users/alittle23/Documents/Personal Projects/Genomics-Data-Parser/data/human.1.rna.fna"
for record in SeqIO.parse(reversedTranscript_RNA,"fasta"):


    print(record)
    print("seq length:",len(record.seq))
