# Nucleotide counter

nucleotides = ["A", "C", "G", "T"]

# You might want to change the name of the rosalind file because it can get confusing, here I changed it to rosalind_dna_1
file_name = r"C:\Users\scien\Downloads\rosalind_dna_1.txt"

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
        sequence = "".join([line.strip() for line in content if not line.startswith('>')])
    return sequence

sequence = read_file(file_name)

def nucleotide_count(seq):
    nucleotides_calculator = {"A": 0, "C": 0, "G": 0, "T": 0}
    for num in seq:
        nucleotides_calculator[num] += 1
    return nucleotides_calculator

# For the solution type A, C, G, and T in that order, it will be marked wrong if :"{} are included
print(nucleotide_count(sequence))
