import random

# Generate random DNA Sequence (k=1000000)
sequence = ''.join(random.choices('ACGT', k=1000000))

# Save to FASTA file
with open('../data/random_sequence.fasta', 'w') as f:
    # Write the sequence with 80 base pairs per line
    for i in range(0, len(sequence), 1):
        f.write(sequence[i:i+80] + '\n')

print("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")
