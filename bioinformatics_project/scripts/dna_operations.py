import sys

# Returns the complement of a DNA sequence
def complement(sequence):
    # Create a translation map: A -> T, T -> A, G -> C, C -> G
    complement_map = str.maketrans('ATGCatgc', 'TACGtacg')
    
    # Translate the sequence using the translation map
    return sequence.translate(complement_map)

# Returns the reverse of a DNA sequence
def reverse(sequence):
    return sequence[::-1]

# Reverse complement function (complement + reverse)
def reverse_complement(sequence):
    return reverse(complement(sequence))


# Process with command-line arguments
if __name__ == "__main__":
    # Get the DNA sequence from the command-line arguments
    sequence = sys.argv[1]
    
    # Output the original sequence
    print(f"Original sequence: {sequence}")
    
    # Output the complement of the sequence
    print(f"Complement: {complement(sequence)}")
    
    # Output the reverse of the sequence
    print(f"Reverse: {reverse(sequence)}")
    
    # Output the reverse complement of the sequence
    print(f"Reverse complement: {reverse_complement(sequence)}")