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
        if self.UF[p] == self.UF[q]:
            return True
        else:
            return False

import fileinput

with fileinput.input(files= 'tinyUF.txt') as f:
    for line in f:
        if len(line)<4:
            X = UF(int(line))
            continue
        p = int(line.split()[0])
        q = int(line.split()[1])
        if not(X.connected(p, q)):
            X.union(p, q)

print(X.UF)
