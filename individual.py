import random
from typing import List

from constants import GENOTYPE_SIZE, MAP_SIZE

# TODO: Check if this is useful
# observation, info = env.reset(seed=42)


class Individual:
    def __init__(self, genotype=None):
        # list of decisions the agent took
        self.genotype = self.initialize_genotype() if genotype is None else genotype
        # current position of the agent
        self.phenotype = []
        # fitness value of the individual
        self.fitness = 0

    def __str__(self):
        return f"Genotype: {self.genotype}\nPhenotype: {self.phenotype}\nFitness: {self.fitness}"

    def initialize_genotype(self) -> List[int]:
        genotype = []

        for _ in range(GENOTYPE_SIZE):
            possible_actions = [0, 1, 2, 3]
            action = random.choice(possible_actions)
            genotype.append(action)

        return genotype

    # TODO: Move to util / helper
    def manhattan_distance(self, point1, point2):
        x1, y1 = point1 % MAP_SIZE, point1 // MAP_SIZE
        x2, y2 = point2 % MAP_SIZE, point2 // MAP_SIZE
        return abs(x1 - x2) + abs(y1 - y2)

    def calculate_fitness(
        self,
        observation,
        reward,
        terminated,
    ) -> float:
        """
        Calculate the fitness of an individual based on its genotype and simulation results.
        """
        target = (MAP_SIZE**2) - 1
        agent = observation

        if reward == 1:  # Agent reached the goal
            fitness = 100 - len(self.genotype)
        else:  # Agent did not reach the goal
            fitness = (self.manhattan_distance(agent, target) * 2) - len(self.genotype)

        self.fitness = fitness

        return fitness

    def traverse_maze(self, env):
        observation, reward, terminated = 0, 0, 0
        action_history = []
        position_history = [0]

        env.reset()
        for action in self.genotype:
            observation, reward, terminated, _, _ = env.step(action)

            action_history.append(action)
            position_history.append(observation)

            # update ui
            env.render()

            if terminated:
                break

        self.genotype = action_history
        self.phenotype = position_history

        return self.calculate_fitness(observation, reward, terminated)
