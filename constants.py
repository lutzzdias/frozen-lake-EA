import gymnasium as gym

from maps import *

# Map
MAP = map_4_by_4
MAP_SIZE = 4

# Number of generations
MAX_ITERATIONS_4X4 = 100
MAX_ITERATIONS_8X8 = 200
MAX_ITERATIONS_12X12 = 500

# Number of individuals
POPULATION_SIZE = 100

# Genotype max size
GENOTYPE_MAX_SIZE = 50

# Variation probabilities
CROSSOVER_PROBABILITY = 0.8
MUTATION_PROBABILITY = 0.05

# Parent selection
TOURNAMENT_SIZE = 5
ELITE_PERCENTAGE = 0.05  # 5% of the population

# Maze rendering
RENDER_MODE = "human"

# Environment
ENV = gym.make(
    "FrozenLake-v1",
    desc=MAP,
    is_slippery=False,
    render_mode=None,
    # render_mode=RENDER_MODE,
)
