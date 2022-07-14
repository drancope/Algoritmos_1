class mergesort:
    def swap(a):
        if len(a)<2:
            return a
        if a[0]>a[1]:
            a[0],a[1] = a[1],a[0]
        return a
    def merge(la, lb, N, mezcla):
        j=0
        k=0
        na=N//2
        nb=N-na
        for i in range(N):
            #print('inicio ciclo: ',la, lb, mezcla, i, j, k)
            if (j == na):
                for l in range(k, nb):
                    mezcla[i] = lb[k]
                    k += 1
                    i += 1
                #print('j es n. ', mezcla, i, j, k)
                break
            elif (k == nb):
                for l in range(j, na):
                    mezcla[i] = la[j]
                    j += 1
                    i += 1
                #print('k es n. ', mezcla, i, j, k)
                break
            else:
                if la[j] < lb[k]:
                    mezcla[i] = la[j]
                    j += 1
                else:
                    mezcla[i] = lb[k]
                    k += 1
                #print(mezcla, i, j, k)
        return mezcla
    def ms(lista):
        largo = len(lista)
        n = largo//2
        if largo > 2:
            la = lista[0:n]
            lb = lista[n:largo]
            mergesort.ms(la)
            mergesort.ms(lb)
            lista = mergesort.merge(la, lb, largo, lista)
        else:
            return mergesort.swap(lista)
        return lista


import time
listafinal = [6,0,100,63,25,45,25,12,87,1,5,8,3,47,32,35,33,12,23,78,73,9]

tic = time.perf_counter()
print(mergesort.ms(listafinal))
print('Tiempo empleado: ', time.perf_counter() - tic)
