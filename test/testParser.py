from src.FASTAparser import parseFASTA
def test_fasta_reads():
    sequences = parse_fasta("data/example.fasta")
    assert len(sequences) == 2