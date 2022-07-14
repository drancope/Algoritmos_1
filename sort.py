entrada = [5,4,1,3,8,7,13,6,0,9,14,12,11,2]
salida1 = entrada[ :7 ]
salida2 = entrada[7: ]
print(salida1)
datos = [3, 2, 6, 5]
datos1 = datos[0:len(datos)//2]
print(datos1, len(datos1))

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
print('salida1: ',salida,"  veces: ", veces, "   operaciones: ", op)
salida1 = salida

salida = salida2
N = len(salida)
op, veces = ordenar()
print('salida2: ',salida,"  veces: ", veces, "   operaciones: ", op)
salida2 = salida

entrada = [6,0,3,2]
salida1 = entrada[ :2 ]
salida2 = entrada[2: ]

mezcla = entrada
N = len(mezcla)
j = 0
k = 0
op = 0
for i in range(N):
    if (j == N//2):
        for l in range(k-1, N//2-1):
            mezcla[l+i-1] = salida2[k]
            k += 1
        print(mezcla)
        break
    elif (k == N//2):
        for l in range(j-1, N//2-1):
            mezcla[l+i] = salida1[j]
            j += 1
        print(mezcla, i, j, k)
        break
    else:
        if salida1[j] < salida2[k]:
            mezcla[i] = salida1[j]
            j += 1
        else:
            mezcla[i] = salida2[k]
            k += 1
        print(mezcla, i, j, k)
        op +=3

print(mezcla, op)
