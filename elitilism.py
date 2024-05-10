from constants import ELITE_PERCENTAGE


def elitilist_survivors(parents, offspring):
    population_size = len(parents)
    elite_size = int(population_size * ELITE_PERCENTAGE)
    parents.sort(key=lambda individual: individual.fitness, reverse=True)
    new_population = parents[:elite_size] + offspring[: population_size - elite_size]
    return new_population
