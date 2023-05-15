import os

from Bio import SeqIO
from Bio.Seq import Seq

def find_orfs(dna_seq, trans_table, min_protein_length):
    possible_orfs = []
    for strand, nuc in [(+1, dna_seq), (-1, dna_seq.reverse_complement())]:
        for frame in range(3):
            length = 3 * ((len(nuc) - frame) // 3)
            for pro in nuc[frame:frame + length].translate(trans_table).split("*"):
                if len(pro) >= min_protein_length:
                    possible_orfs.append(str(pro))
    return possible_orfs


filename = "filetest.fasta"
sequences = SeqIO.parse(filename, "fasta")

trans_table = 1
min_protein_length = 50


for seq in sequences:
    seq_name = seq.id
    dna_seq = seq.seq

    proteins = find_orfs(dna_seq, trans_table, min_protein_length)
    output_dir = f"result/{seq_name}"
    os.makedirs(output_dir, exist_ok=True)

    for i, protein in enumerate(proteins):
        file_name = f"{seq_name}_orf{i+1}.fasta"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "w") as f:
            f.write(f">Protein {i + 1}\n{protein}\n")