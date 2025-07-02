"""
Extract:
- Sequence ID
-Description (gene Name)
-Sequence
-Length of sequence
-Organism, isoform, version
-group transcripts by gene
-translate DNS to Protein
-plot:
    -sequence length distribution
    -GC content
    -number  of transcripts
-export result to .json         
"""
from Bio.Seq import Seq

# create a sequence object
my_seq = Seq("CATGTAGACTAG")

# print out some details about it
print("seq %s is %i bases long" % (my_seq, len(my_seq)))
print("reverse complement is %s" % my_seq.reverse_complement())
print("protein translation is %s" % my_seq.translate())
