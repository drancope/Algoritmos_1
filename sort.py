entrada = [5,4,1,3,8,7,13,6,14,9,0,12,11,2]
salida1 = entrada[ :7 ]
salida2 = entrada[7: ]

N = len(salida1)
print(N)

def pasada(op, final):
    final = 0
    for i in range(N-1):
        if salida[i]>salida[i+1]:
            salida[i], salida[i+1] = salida[i+1], salida[i]
            op += 3
            final = 1
    return op, final

def ordenar():
    op=0
    veces = 0
    final = 1
    while final == 1:
        op, final = pasada(op, final)
        veces +=1
    return op, veces

salida = entrada
N = len(salida)
op, veces = ordenar()
print(salida)
print("veces: ", veces)
print("operaciones: ", op)

salida = salida1
N = len(salida)
op, veces = ordenar()
print(salida)
print("veces: ", veces)
print("operaciones: ", op)
salida1 = salida

salida = salida2
N = len(salida)
op, veces = ordenar()
print(salida)
print("veces: ", veces)
print("operaciones: ", op)
salida2 = salida

mezcla = entrada
j = 0
k = 0
op = 0
for i in range(N):
    if salida1[j] < salida2[k]:
        mezcla[i] = salida1[j]
        j += 1
    else:
        mezcla[i] = salida2[k]
        k += 1
    op +=3

print(mezcla, op)
