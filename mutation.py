import random


def should_mutate(mutation_rate):
    return random.random() < mutation_rate


def swap_decisions(genotype):
    # Select two random indices
    index_1 = random.randint(0, len(genotype) - 1)
    index_2 = random.randint(0, len(genotype) - 1)

    # Swap the positions of the decisions
    genotype[index_1], genotype[index_2] = genotype[index_2], genotype[index_1]


def mutate(genotype, mutation_rate):
    if should_mutate(mutation_rate):
        swap_decisions(genotype)
