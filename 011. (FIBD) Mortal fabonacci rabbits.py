# n represents the amount of time that passes in months
# m represents the lifespan of rabbits in months
n = 6
m = 3

def mortal_fabonacci_rabbits(n, m):
    rabbits = [0] * m
    rabbits[0] = 1

    for month in range(1, n):
        new_rabbits = sum(rabbits[1:])
        rabbits = [new_rabbits] + rabbits[:-1]

    return sum(rabbits)

print(mortal_fabonacci_rabbits(n, m))
