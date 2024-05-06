from typing import List

from constants import *
from crossover import one_point_crossover, should_crossover
from individual import Individual
from maps import *
from mutation import mutate, should_mutate

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

    population.sort(key=lambda individual: individual.fitness_value, reverse=True)
    return population


def main():
    population = initialize_population()

    for gen in range(MAX_ITERATIONS_4X4):
        print(gen)

        for individual in population:
            individual.traverse_maze(ENV)

        # order population by fitness
        population = rank(population)

        # initialize next population
        new_population = []

        for _ in range(POPULATION_SIZE):
            # TODO: tournament selection
            new_individual = population[0]

            if should_crossover():
                # parent selection
                # TODO: tournament selection
                parent1 = population[0]
                parent2 = population[1]
                new_individual = one_point_crossover(parent1, parent2)

            if should_mutate():
                new_individual = mutate(new_individual)

            new_population.append(new_individual)

        # TODO: Survivor selection
        # population = survivor_selection(population, new_population)
        population = new_population

    ENV.close()


if __name__ == "__main__":
    main()
