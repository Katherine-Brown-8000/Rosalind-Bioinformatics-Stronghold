# Change both your user name and the name of the file, both of which are under file_path

def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        fasta_data = file.readlines()
    return fasta_data

def parse_fasta(data):
    sequence = {}
    current_label = None
    for line in data:
        line = line.strip()
        if line.startswith('>'):
            current_label = line[1:]
            sequence[current_label] = ('')
        elif current_label:
            sequence[current_label] += line
    return sequence

def overlap_graph(sequence, k):
    adjacency_list = []
    for label1, seq1 in sequences.items():
        for label2, seq2 in sequences.items():
            if label1 != label2 and seq1[-k:] == seq2[:k]:
                adjacency_list.append(f"{label1} {label2}")
    return adjacency_list

file_path = r"C:/Users/username/Desktop/rosalind_grph.txt"

fasta_data = read_fasta_file(file_path)
sequences = parse_fasta(fasta_data)
adjacency_list = overlap_graph(sequences, 3)

for edge in adjacency_list:
    print(edge)

