import matplotlib.pyplot as plt


def histogram(data, title, xlabel, ylabel, bins=10):
    plt.hist(data, bins=bins)
    plt.grid(axis="y")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
