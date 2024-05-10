from typing import List

from constants import *
from crossover import crossover, should_crossover
from elitilism import elitilist_survivors
from individual import Individual
from maps import *
from mutation import mutate, should_mutate
from tournament import tournament

# Representation:
# - North: 0
# - South: 1
# - East: 2
# - West: 3

# genotype_example = [0, 3, 2, 2, 1, 0, 3]

# Mutation:
# 1. append random decision
# 2. delete random decision
# 3. change random decision

# Cross-over:
# Single point crossover

# Fitness:
# Goal was reached or not. If it failed, how close to the goal was the agent.
# How many steps were taken before the end.

# Parent Selection:
# Tournament

# Survivor Selection:
# Elitilism


def initialize_population() -> List[Individual]:
    population = []

    for _ in range(POPULATION_SIZE):
        population.append(Individual())

    return population


def rank(population) -> List[Individual]:
    """
    Sorts the population based on their fitness, the highest fitness individuals
    will be in the beginning of the list
    """

    population.sort(key=lambda individual: individual.fitness, reverse=True)
    return population


def main():
    population = initialize_population()

    for _ in range(MAX_ITERATIONS_4X4):
        for individual in population:
            individual.traverse_maze(ENV)

        # order population by fitness
        population = rank(population)

        # initialize next population
        new_population = []

        for _ in range(POPULATION_SIZE):
            new_individual = tournament(population)

            if should_crossover():
                # parent selection
                parent1 = tournament(population)
                parent2 = tournament(population)
                new_individual = crossover(parent1, parent2)

            if should_mutate():
                new_individual = mutate(new_individual)

            new_population.append(new_individual)

        # Survivor selection
        population = elitilist_survivors(population, new_population)

    ENV.close()


if __name__ == "__main__":
    main()
