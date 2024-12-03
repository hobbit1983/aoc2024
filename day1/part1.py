lista = []
listb = []
sum_of_distance = 0

with open("input") as file:
    while line := file.readline():
        parts = line.split()
        lista.append(int(parts[0]))
        listb.append(int(parts[1]))

lista.sort()
listb.sort()

for a in lista:
    b = listb[lista.index(a)]
    sum_of_distance += abs(a - b)

print(sum_of_distance)