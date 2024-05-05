import random
from typing import List

import gymnasium as gym

from constants import GENOTYPE_MAX_SIZE, MAP, MAP_SIZE, RENDER_MODE

# TODO: Check if this is useful
# observation, info = env.reset(seed=42)


class Individual:
    def __init__(self, map=MAP, genotype=None):
        self.genotype = self.initialize_genotype() if genotype is None else genotype
        self.fitness_value = None

        self.env = gym.make(
            "FrozenLake-v1",
            desc=map,
            is_slippery=False,
            render_mode=RENDER_MODE,
        )

    def initialize_genotype(self) -> List[int]:
        genotype = []
        genotype_size = random.randint(1, GENOTYPE_MAX_SIZE)

        for _ in range(genotype_size):
            genotype.append(random.randint(0, 3))

        return genotype

    def fitness(
        self,
        observation,
        reward,
        terminated,
        truncated,
        info,
    ) -> int:
        final_position = (MAP_SIZE - 1) * MAP_SIZE + (MAP_SIZE - 1)

        fitness = 100 * reward + 100 / (final_position - observation)
        self.fitness_value = fitness

        return fitness

    def traverse_maze(self):
        env = self.env
        # initialize ui
        env.reset()

        for action in self.genotype:
            observation, reward, terminated, truncated, info = env.step(action)

            # update ui
            env.render()

            if terminated or action == self.genotype[-1]:
                env.close()
                return self.fitness(
                    observation,
                    reward,
                    terminated,
                    truncated,
                    info,
                )
