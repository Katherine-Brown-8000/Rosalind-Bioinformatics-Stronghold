from scipy.stats import binom

def independent_alleles(k, N):
    n = 2 ** k
    p = 0.25

    probability = 1 - binom.cdf(N - 1, n, p)
    return probability

k = 2
N = 1
print(f"{independent_alleles(k, N):.3f}")
