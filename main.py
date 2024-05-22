from evolutionary_algorithm import evolutionary_algorithm
from util import histogram


def main():
    bests = []

    for _ in range(30):
        # list of lists, each list contains the individuals of a generation
        data = evolutionary_algorithm()

        last_generation = data[-1]
        best_individual = last_generation[0]
        bests.append(best_individual)

    avg_fitness = sum([i.fitness for i in bests]) / len(bests)

    steps = [len(i.phenotype) for i in bests]

    histogram(steps, "Path size", "Path size", "Ocurrence")


if __name__ == "__main__":
    main()
