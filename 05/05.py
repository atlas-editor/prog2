import numpy as np
import matplotlib.pyplot as plt
import math

# Základní velikost písma
plt.rcParams.update({'font.size': 22})

# Triviální příklad: jedna křivka
def example1():
    x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
    y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
    z = np.polyfit(x, y, 10)
    p = np.poly1d(z)
    xp = np.linspace(-2, 6, 100)
    plt.plot(x, y, '.')
    plt.plot(xp, p(xp))
    plt.show()

example1()