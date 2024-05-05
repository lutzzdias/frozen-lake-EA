import random

import gymnasium as gym

from constants import *
from maps import *

# Representation:
# - North: 00
# - South: 01
# - East: 10
# - West: 11

# [South, South, East, North, East, East, South, West, South, East, East]

# Action:
# generate a random 2 bit value (represents an action)

# Mutation:
# Change the position of one of the actions.

# Cross-over:
# Split the representation and recombine them.

# Fitness:
# Goal was reached or not. If it failed, how close to the goal was the agent.
# How many steps were taken before the end.

# Parent Selection:
# Tournament

# Survivor Selection:
# Elitilism

# globals
RENDER_MODE = "human"
env = gym.make(
    "FrozenLake-v1", desc=map_4_by_4, is_slippery=False, render_mode=RENDER_MODE
)
observation, info = env.reset(seed=42)


def update_ui():
    if RENDER_MODE is not None:
        env.render()


def initialize_population():
    # TODO: create a population of random phenotypes (individuals)
    return NotImplementedError


def main():
    update_ui()

    initialize_population()

    for generation in range(MAX_ITERATIONS_4X4):
        # TODO: implement action selection (each action is a 2bit bin)
        action = random.randint(0, 3)

        # TODO: Use this for the fitness function, etc
        observation, reward, terminated, truncated, info = env.step(action)

        update_ui()

        if terminated:
            break


if __name__ == "__main__":
    main()
