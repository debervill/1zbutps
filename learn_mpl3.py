from base64 import encode
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

pervz = {}
 
with open('per-gruz2.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=';')
	rows = list(csv_reader)



years = rows[3]

years2 =years[1:len(years)] 

data = rows[5]
data2 = data[1:len(data)]

for i in range(len(years2)):
    pervz[years2[i]] = int(data2[i])
    
    
    

fig, ax = plt.subplots(figsize=(15, 4), layout='constrained')
ax.bar(pervz.keys(), pervz.values())

rects = ax.patches
labels = pervz.values()
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
            ha='center', va='bottom')
plt.show()


