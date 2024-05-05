import random


def should_mutate(mutation_rate):
    return random.random() < mutation_rate


def swap_decisions(chromosome):
    # Select two random indices
    index_1 = random.randint(0, len(chromosome) - 1)
    index_2 = random.randint(0, len(chromosome) - 1)

    # Swap the positions of the decisions
    chromosome[index_1], chromosome[index_2] = chromosome[index_2], chromosome[index_1]


def mutate(chromosome, mutation_rate):
    if should_mutate(mutation_rate):
        swap_decisions(chromosome)
