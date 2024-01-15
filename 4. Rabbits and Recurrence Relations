# I came across two ways to solve this problem, the first one is from ChatGPT and the second is from rebelscience

# Method from ChatGPT
import numpy as np

def fibonacci_matrix_exponentiation(months, offsprings):
    base_matrix = np.array([[1, offsprings], [1, 0]])
    result_matrix = np.linalg.matrix_power(base_matrix, months - 1)
    return result_matrix[0, 0]

print(fibonacci_matrix_exponentiation(28, 2)) 

# Method from reblescience
def Fibonacci_Loop_Pythonic(months, offsprings):
    parent, child = 1, 1
    for itr in range(months -1):
        child, parent = parent, parent + (child * offsprings)
    return child

print(Fibonacci_Loop_Pythonic(28, 5))

