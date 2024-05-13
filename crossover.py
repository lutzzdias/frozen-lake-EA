import random

from constants import CROSSOVER_PROBABILITY, ENV
from individual import Individual


def should_crossover():
    return random.random() < CROSSOVER_PROBABILITY


def crossover(parent1: Individual, parent2: Individual) -> Individual:
    shorter_parent = min(parent1, parent2, key=lambda i: len(i.genotype))
    longer_parent = max(parent1, parent2, key=lambda i: len(i.genotype))

    cut_point = random.randint(0, (len(shorter_parent.genotype) - 1))

    child_genotype = (
        shorter_parent.genotype[:cut_point] + longer_parent.genotype[cut_point:]
    )
    child = Individual(genotype=child_genotype)

    # recalculate fitness
    child.traverse_maze(ENV)

    return child
