import random

from constants import CROSSOVER_PROBABILITY
from individual import Individual


def should_crossover():
    return random.random() < CROSSOVER_PROBABILITY


def one_point_crossover(parent1: Individual, parent2: Individual) -> Individual:
    cut_point = random.randint(0, len(parent1.genotype) - 1)
    genotype = []

    for i in range(len(parent1.genotype)):
        if i < cut_point:
            gene_index = i % len(parent1.genotype)
            genotype.append(parent1.genotype[gene_index])
        else:
            gene_index = i % len(parent2.genotype)
            genotype.append(parent2.genotype[gene_index])

    result = Individual(genotype=genotype)
    result.traverse_maze()

    return result
