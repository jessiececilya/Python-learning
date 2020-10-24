import numpy as np
import matplotlib.pyplot as plt
# Build a vector of 10000 normal deviates with variance 0.5^2 and 
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)
# Compute the histogram with numpy and then plot it# NumPy version (no plot)(n, bins) = 
np.histogram(v, bins=50, density=True)
plt.plot(.5*(bins[1:]+bins[:-1]), n)
plt.show()
