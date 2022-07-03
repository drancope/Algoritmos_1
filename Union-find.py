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
