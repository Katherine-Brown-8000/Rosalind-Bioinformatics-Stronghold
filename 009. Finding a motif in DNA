DNA_sample = "GATATATGCATATACTT"
motif = "ATAT"

def find_motif(DNA_sample, motif):
    seq = []
    motif_length = len(motif)
    for index in range(len(DNA_sample) - motif_length + 1):
        if DNA_sample[index:index + motif_length] == motif:
            seq.append(index + 1)
    return seq

seq = find_motif(DNA_sample, motif)

print(f"The motif '{motif}' is found at positions: {' '.join(map(str, seq))}")
