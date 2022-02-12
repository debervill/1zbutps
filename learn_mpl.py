import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

"""
plt.plot([1, 2, 3, 4, 5], [1, 12, 13, 4, 5])
plt.show()
"""

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']

ax.bar(categories, np.random.rand(len(categories)))

plt.show()