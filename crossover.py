import random


def one_point_crossover(parent1, parent2):
    cut_point = random.randint(0, parent1 - 1)
    genotype = []

    for i in range(len(parent1)):
        if i < cut_point:
            genotype.append(parent1[i])
        else:
            genotype.append(parent2[i])

    return genotype
