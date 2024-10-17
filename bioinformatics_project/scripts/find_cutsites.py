import sys

# Load DNA sequence from FASTA file
def read_fasta(filepath):
    sequence = ""  # Set empty sequence
    with open(filepath, 'r') as f:
        lines = f.readlines()

        stripped_lines = [] # Set empty stripped lines
        for line in lines:
            stripped_lines.append(line.strip()) # Strip each line and append to the list

        sequence = ''.join(stripped_lines) # Join the list to the sequence  
    return sequence

# Find the cutsite
def find_cut_sites(sequence, cutsite):
    cutsite_positions = []  # Set empty cutsite position
    for i in range(len(sequence)):
        if sequence.startswith(cutsite, i): # Search the cutsite
            cutsite_positions.append(i)  # Add the new cutsite to the cutsite positions list
    return cutsite_positions


# Find the cutsite paried within the specific distance
def find_cutsite_pairs(cutsite_positions, min_distance=80000, max_distance=120000):
    pairs = [] # Set empty pairs list
    for i, pos1 in enumerate(cutsite_positions): # Get the first position
        for pos2 in cutsite_positions[i+1:]: # Get the second position
            distance = pos2 - pos1 # Caluculate the distance
            if min_distance <= distance <= max_distance:
                pairs.append((pos1, pos2)) # Add the new pair to the list
    return pairs

# Process with command-line arguments
if __name__ == "__main__":
    fasta_file = sys.argv[1]
    cutsite = sys.argv[2].replace('|', '')  # Replace "|" to "" for excluding it
    sequence = read_fasta(fasta_file) # Load the fasta file
    
    # Find the cutsites
    cutsite_positions = find_cut_sites(sequence, cutsite)
    print(f"Total cut sites found: {len(cutsite_positions)}")
    
    # Find the cutsites pair between 80-120kbp
    cutsite_pairs = find_cutsite_pairs(cutsite_positions)
    print(f"Cut site pairs 80-120 kbp apart: {len(cutsite_pairs)}")
    
    # Print the fiest five pairs
    print("First 5 pairs:")
    for i, (pos1, pos2) in enumerate(cutsite_pairs[:5]):
        print(f"{i+1}. {pos1} - {pos2}")
    
    # Save the results
    with open('../results/distant_cutsite_summary.txt', 'w') as f:
        f.write(f"Total cut sites found: {len(cutsite_positions)}\n")
        f.write(f"Cut site pairs 80-120 kbp apart: {len(cutsite_pairs)}\n")
        f.write("First 5 pairs:\n")
        for i, (pos1, pos2) in enumerate(cutsite_pairs[:5]):
            f.write(f"{i+1}. {pos1} - {pos2}\n")
    
    print("Results saved to bioinformatics_project/results/distant_cutsite_summary.txt")