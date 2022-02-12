
file_1 = open('123.txt', 'r').readlines()
file_2 = open('22.txt', 'r').readlines()


clear_data = []

for elem in file_1:
    print(elem.replace('\n',''))
    clear_data.append(float(elem.replace('\n','')))

print(clear_data)

sum = 0

for elem in clear_data:
    sum = sum + elem


print(sum)
