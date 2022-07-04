class UF:
    UF = []
    length = 0
    def __init__(self, N):
        for i in range(N):
            self.UF.append(i)
        self.length = N
    def union(self, p, q):
        pid = self.UF[p]
        qid = self.UF[q]
        for i in range(self.length):
            if self.UF[i] == pid:
                self.UF[i] = qid
    def connected(self, p, q):
        return self.UF[p] == self.UF[q]

A = 0
B = 0
C = 0
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

def resetear(uf, N):
    for i in range(N):
        uf.UF[i]=i

class QU:
    QU = []
    length = 0
    def __init__(self, N):
        for i in range(N):
            self.QU.append(i)
        self.length = N
    def root(self, i):
        while (i != self.QU[i]):
            i = self.QU[i]
        return i
    def union(self, p, q):
        i = self.QU[p]
        j = self.QU[q]
        self.QU[i] = j
    def connected(self, p, q):
        return self.root(p) == self.root(q)

with fileinput.input(files= 'tinyUF.txt') as f:
    for line in f:
        if not ' ' in (line):
            X = QU(int(line))
            B = X
            print(X.QU)
            continue
        p = int(line.split()[0])
        q = int(line.split()[1])
        if not(X.connected(p, q)):
            X.union(p, q)

print(X.QU)


class QI:
    QI = []
    QS = []
    length = 0
    def __init__(self, N):
        for i in range(N):
            self.QI.append(i)
            self.QS.append(1)
        self.length = N
    def root(self, i):
        while (i != self.QI[i]):
            i = self.QI[i]
        return i
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if (i == j):
            return 0
        if self.QS[i] < self.QS[j]:
            self.QI[i] = j
            self.QS[j] += self.QS[i]
        else:
            self.QI[j] = i
            self.QS[i] += self.QS[j]
    def connected(self, p, q):
        return self.root(p) == self.root(q)


with fileinput.input(files='tinyUF.txt') as f:
    for line in f:
        if not ' ' in (line):
            X = QI(int(line))
            C = X
            print(X.QI)
            continue
        p = int(line.split()[0])
        q = int(line.split()[1])
        if not(X.connected(p, q)):
            X.union(p, q)

print(C.QI)
print(C.QS)