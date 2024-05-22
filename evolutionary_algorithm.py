from typing import List

from constants import ENV, GENERATIONS, POPULATION_SIZE
from crossover import crossover, should_crossover
from elitilism import elitilist_survivors
from individual import Individual
from mutation import mutate, should_mutate
from tournament import tournament


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


def evolutionary_algorithm():
    data = []
    population = initialize_population()

    for _ in range(GENERATIONS):
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

        data.append(rank(population))

        # Survivor selection
        population = elitilist_survivors(population, new_population)

    ENV.close()
    return data
