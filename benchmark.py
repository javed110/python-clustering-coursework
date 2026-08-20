import timeit
import numpy as np
import matplotlib.pyplot as plt

setup = """
import numpy as np
labels = np.random.randint(0, 10, size=10000000)
"""

print("Baseline (with astype):", timeit.timeit("c = labels.astype(float)", setup=setup, number=100))
print("Optimized (without astype):", timeit.timeit("c = labels", setup=setup, number=100))
