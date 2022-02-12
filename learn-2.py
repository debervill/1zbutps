import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



#Пример работы с словарём

slr = { "apple":12,
       "lemon": 8,
       "orange": 5
}

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = slr.keys()
ax.bar(slr.keys(), slr.values())
plt.show()