
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
BRCA1_transcript = "/Users/alittle23/Documents/Personal Projects/Genomics-Data-Parser/data/BRCA1_refseq_transcript.fasta"
for record in SeqIO.parse(BRCA1_transcript,"fasta"):
    print(record.id)
