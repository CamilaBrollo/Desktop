v = [5, 1, 4, 2, 7, 8, 3, 6]
for i in range (7, 4, -1):
    aux = v[i]

    v[i] = v[7-i]
    print(v[i])
    v[7-i] = aux
    print(aux)
    print(v)

v[2] = v[0]
v[v[2]] = v[v[1]]

print(v)
