def expected_dominant_offspring(couples):
    probabilities = [1, 1, 1, 0.75, 0.5, 0]
    expected_value = sum(2 * couples[i] * probabilities[i] for i in range(6))
    return expected_value

couples = [1, 0, 0, 1, 0, 1]
result = expected_dominant_offspring(couples)
print(result)
