# There seems to be an error with some of the files being called because uniprot changes their names.
# Remove Names from the files in place of numbers
# For that reason I was unable to complete this problem, but left the code here for later attempts

import requests
import re

def read_uniprot_ids(file_path):
    with open(file_path, 'r') as file:
        fasta_data = file.readlines()
    return fasta_data

def fetch_fasta_data(uniprot_id):
    clean_id = uniprot_id.split('_')[0]
    url = f"http://www.uniprot.org/uniprot/{clean_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        fasta_data = response.text
        sequence = ''.join(fasta_data.splitlines()[1:])
        return sequence
    else:
        print(f"Error fetching data for {uniprot_id}: HTTP Status {response.status_code}")
        return None

def find_motif_locations(sequence, motif_pattern):
    return [m.start() + 1 for m in re.finditer(motif_pattern, sequence)]

def main(uniprot_ids):
    motif_pattern = r'N[^P][ST][^P]'
    results = {}

    for uniprot_id in uniprot_ids:
        sequence = fetch_fasta_data(uniprot_id)
        if sequence:
            locations = find_motif_locations(sequence, motif_pattern)
            if locations:
                results[uniprot_id] = locations

            else:
                print(f"No motifs found in {uniprot_id}")
        else:
            print(f"Failed to fetch sequence for {uniprot_id}")
    return results

file_path = 'C:/Users/scien/Desktop/rosalind_mprt2.txt'
uniprot_ids = read_uniprot_ids(file_path)
result = main(uniprot_ids)


for uniprot_id, locations in result.items():
    print(uniprot_id)
    print(" ".join(map(str, locations)))