
lista = []
listb = []
similarity_score = 0

with open("input") as file:
    while line := file.readline():
        parts = line.split()
        lista.append(int(parts[0]))
        listb.append(int(parts[1]))

for a in lista:
    similarity_score += a * listb.count(a)

print(similarity_score)
       
