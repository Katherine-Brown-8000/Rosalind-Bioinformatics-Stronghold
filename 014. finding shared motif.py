# Remember to match username and file name to match your computer
# This change can be made on line 44 under file path

def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        fasta_data = file.readlines()
    return fasta_data


def parse_fasta(data):
    sequences = []
    sequence = ""
    for line in data:
        line = line.strip()
        if line.startswith(">"):
            if sequence:
                sequences.append(sequence)
            sequence = ""
        else:
            sequence += line.strip()
    if sequence:
        sequences.append(sequence)
    return sequences


def longest_common_substring(dna_strings):
    if not dna_strings:
        return ""

    shortest_seq = min(dna_strings, key=len)
    length = len(shortest_seq)
    longest_substrings = set()

    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = shortest_seq[i:j]
            if all(substring in seq for seq in dna_strings):
                if not longest_substrings or len(substring) > len(next(iter(longest_substrings))):
                    longest_substrings = {substring}
                elif len(substring) == len(next(iter(longest_substrings))):
                    longest_substrings.add(substring)
    return list(longest_substrings)

file_path = r'C:/Users/username/Desktop/rosalind_lcsmT.txt'

data = read_fasta_file(file_path)
dna_strings = parse_fasta(data)
result = longest_common_substring(dna_strings)
print(result)