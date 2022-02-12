import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from random import  randint


apples = { "Январь": 0,
          "Февраль": 0,
          "Март": 0,
          "Апрель": 0,
          "Май": 0,
          "Июнь": 0,
          "Июль": 0,
          "Август": 0,
          "Сентябрь": 0,
          "Октябрь": 0,
          "Ноябрь": 0,
          "Декабрь": 0,
}

for key in apples.keys():
    apples[key] = randint(10, 113)
    


fig, ax = plt.subplots(figsize=(15, 4), layout='constrained')
ax.bar(apples.keys(), apples.values())


rects = ax.patches
labels = apples.values()
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
            ha='center', va='bottom')




plt.show()



