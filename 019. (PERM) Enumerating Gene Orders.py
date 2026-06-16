import itertools

def generate_permutations(n):
    numbers = list(range(1, n + 1))
    permutations = list(itertools.permutations(numbers))
    total_permutations = len(permutations)
    print(total_permutations)

    for perm in permutations:
        print(" ".join(map(str, perm)))

n = 4
generate_permutations(n)
