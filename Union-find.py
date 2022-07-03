class UF:
    UF = []
    def __init__(self, N):
        for i in range(N):
            self.UF.append(i)
    def union(self, p, q):
        if self.UF[p] == self.UF[q]:
            return('Ya estaban conectados.')
        min = 0;
        if self.UF[p] < self.UF[q]:
            min = p
            max = q
        else:
            min = q
            max = p
        for i in self.UF:
            if self.UF[i] == self.UF[max]:
                self.UF[i] = self.UF[min]
        return('Conexión realizada.')
    def connected(self, p, q):
        return self.UF[p] == self.UF[q]

A = 0
import fileinput

with fileinput.input(files= 'tinyUF.txt') as f:
    for line in f:
        if not ' ' in (line):
            X = UF(int(line))
            A = X
            print(X.UF)
            continue
        p = int(line.split()[0])
        q = int(line.split()[1])
        if not(X.connected(p, q)):
            X.union(p, q)

print(A.UF)
