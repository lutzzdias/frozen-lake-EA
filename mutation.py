import random

from constants import ENV, MUTATION_PROBABILITY
from individual import Individual


def should_mutate():
    return random.random() < MUTATION_PROBABILITY


def append_decision(genotype):
    decision = random.randint(0, 3)
    genotype.append(decision)
    return genotype


def delete_decision(genotype):
    index = random.randint(0, len(genotype) - 1)
    genotype.pop(index)
    return genotype


def change_decision(genotype):
    index = random.randint(0, len(genotype) - 1)
    decision = random.randint(0, 3)

    while decision == genotype[index]:
        decision = random.randint(0, 3)

    genotype[index] = decision
    return genotype


def mutate(individual: Individual):
    genotype = individual.genotype

    mutations = [
        append_decision(genotype),
        delete_decision(genotype),
        change_decision(genotype),
    ]

    mutation = random.choice(mutations)
    individual.genotype = mutation
    individual.traverse_maze(ENV)

    return individual
