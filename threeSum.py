class ThreeSum:
    def count(a):
        N = len(a)
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if (a[i] + a[j] + a[k] == 0):
                        count += 1
        return count

import fileinput

data = []
with fileinput.input(files='Numeros.txt') as f:
    for line in f:
        dat = line.split()
        for i in range(len(dat)):
            data.append(int(dat[i]))

print(data)
print(ThreeSum.count(data))
