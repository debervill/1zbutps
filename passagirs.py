import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

month = { 0:"Январь",
          1:"Февраль",
          2:"Март",
          3:"Апрель",
          4:"Май",
          5:"Июнь",
          6:"Июль",
          7:"Август",
          8:"Сентябрь",
          9:"Октябрь",
          10:"Ноябрь",
}



passagirs = {}

with open('passagirs.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=';')
	rows = list(csv_reader)


data_all = rows[6]

data2 = data_all[1:len(data_all)-1]
data3 = []

for data in data2:
	data3.append(data.replace(',', '.'))


for i in range(len(data2)):
	if i == 0:
		passagirs["Январь"]=int(float(data3[i]))
	else:
		passagirs[month[i]]=int(float(data3[i]) - float(data3[i-1]))



fig, ax = plt.subplots(figsize=(15, 4), layout='constrained')
ax.bar(passagirs.keys(), passagirs.values())

rects = ax.patches
labels = passagirs.values()
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
            ha='center', va='bottom')
plt.show()
