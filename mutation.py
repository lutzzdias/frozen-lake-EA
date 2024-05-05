import random


def should_mutate(mutation_rate):
    return random.random() < mutation_rate


def append_decision(genotype):
    # TODO: Randomly choose any other direction (can't be the same as current)
    decision = "00"

    genotype.append(decision)

    return genotype


def change_decision(genotype):
    # Select random index
    index = random.randint(0, len(genotype) - 1)

    # TODO: Randomly choose any other direction (can't be the same as current)
    return NotImplementedError


def mutate(genotype, mutation_rate):
    if should_mutate(mutation_rate):
        change_decision(genotype)
