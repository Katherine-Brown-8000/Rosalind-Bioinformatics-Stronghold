num_AA = 2
num_Aa = 2
num_aa = 2

# List of all parent types and their counts
parents = ["AA"] * num_AA + ["Aa"] * num_Aa + ["aa"] * num_aa

# Define genotype combinations and their dominant phenotype probabilities
genotype_values = {
    ("AA", "AA"): 1.0,
    ("AA", "Aa"): 1.0,
    ("AA", "aa"): 1.0,
    ("Aa", "Aa"): 0.75,
    ("Aa", "aa"): 0.50,
    ("aa", "aa"): 0.0
}

# Function to calculate the value of phenotypic dominance for all combinations
def calculate_pheno_dom(parents, genotype_values):
    pheno_dom_sum = 0
    total_combinations = 0

    for i in range(len(parents)):
        for j in range(i + 1, len(parents)):
            parent1 = parents[i]
            parent2 = parents[j]
            pheno_dom_sum += genotype_values[(parent1, parent2)]
            total_combinations += 1

    return pheno_dom_sum, total_combinations

# Calculate the phenotypic dominance value and the total number of combinations
pheno_dom_sum, total_combinations = calculate_pheno_dom(parents, genotype_values)

# Calculate the percentage of dominant phenotypes
percentage_dom_pheno = pheno_dom_sum / total_combinations

# Print the results
print(f"Sum of phenotypic dominance values: {pheno_dom_sum}")
print(f"Total combinations: {total_combinations}")
print(f"Sum of phenotypic dominance values / Total combination = {percentage_dom_pheno:.5f}")
print(f"Percentage of dominant phenotypes: {percentage_dom_pheno:.5f}")
