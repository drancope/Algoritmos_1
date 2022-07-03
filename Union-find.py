class UF:
    UF = []
    def __init__(self, N):
        for i in range(N):
            self.UF.append(i)
    def union(self, p, q):
        self.UF[q] = self.UF[p]
#    def connected(p, q):
#        return 2

X = UF(8)
print(X.UF)

X.union(6, 3)

print(X.UF)
