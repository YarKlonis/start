import re

from Bio import SeqIO

forward_primer = 'GAGCCTGCGTTCTTCGATGC'
reverse_primer = 'TTCTTCCGGCACGGAGTACT'

primer_regex = re.compile(f'({forward_primer}|{reverse_primer})')

fasta_file = 'example.fasta'

for record in SeqIO.parse(fasta_file, 'fasta'):
    genome_sequence = str(record.seq)
    amplicons = primer_regex.findall(genome_sequence)
    for amplicon in amplicons:
        print(amplicon)