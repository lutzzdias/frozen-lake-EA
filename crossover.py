import random

from constants import CROSSOVER_PROBABILITY, ENV
from individual import Individual


def should_crossover():
    return random.random() < CROSSOVER_PROBABILITY


def crossover(parent1: Individual, parent2: Individual) -> Individual:
    smallest_genotype_length = min(len(parent1.genotype), len(parent2.genotype))
    cut_point = random.randint(0, (smallest_genotype_length - 1))

    child1_genotype = parent1.genotype[:cut_point] + parent2.genotype[cut_point:]
    child2_genotype = parent2.genotype[:cut_point] + parent1.genotype[cut_point:]

    child1 = Individual(genotype=child1_genotype)
    child2 = Individual(genotype=child2_genotype)

    # recalculate fitness
    child1.traverse_maze(ENV)
    child2.traverse_maze(ENV)

    # return only the child with the highest fitness
    return max(child1, child2, key=lambda child: child.fitness)
