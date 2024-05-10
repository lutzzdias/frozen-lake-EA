import random

from constants import ENV, MUTATION_PROBABILITY
from individual import Individual


def should_mutate():
    return random.random() < MUTATION_PROBABILITY


def mutate(individual: Individual):
    index = random.randint(0, len(individual.genotype) - 1)

    options = [0, 1, 2, 3]
    options.remove(individual.genotype[index])

    individual.genotype[index] = random.choice(options)

    # recalculate fitness
    individual.traverse_maze(ENV)

    return individual
