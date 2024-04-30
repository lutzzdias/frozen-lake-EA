import random

import gymnasium as gym

from maps_to_evaluate import *

# Representation:
# [South, South, East, North, East, East, South, West, South, East, East]

# Action:
# choose one of the directions to move (enum). After decision, update representation.

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

RENDER_MODE = "human"
env = gym.make(
    "FrozenLake-v1", desc=map_4_by_4, is_slippery=False, render_mode=RENDER_MODE
)
observation, info = env.reset(seed=42)

if RENDER_MODE is not None:
    env.render()

for step in range(MAX_ITERATIONS_4_by_4):
    action = random.randint(0, 3)
    observation, reward, terminated, truncated, info = env.step(action)
    if RENDER_MODE is not None:
        env.render()
    if terminated:
        break
