import random
from copy import deepcopy

from constants import TOURNAMENT_SIZE


def tournament(population):
    pool = random.sample(population, TOURNAMENT_SIZE)
    pool.sort(key=lambda individual: individual.fitness, reverse=True)
    return deepcopy(pool[0])
