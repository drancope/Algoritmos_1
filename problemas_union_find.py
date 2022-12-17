import fileinput
#comentario
class social:
    nodes = []
    size = []
    length = 0
    def __init__(self, N):
        for i in range(N):
            self.nodes.append(i)
            self.size.append(1)
        self.length = N
    def root(self, i):
        while (i != self.nodes[i]):
            self.nodes[i] = self.nodes[self.nodes[i]]
            i = self.nodes[i]
        return i
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if (i == j):
            return -1
        if self.size[i] < self.size[j]:
            self.nodes[i] = j
            self.size[j] += self.size[i]
        else:
            self.nodes[j] = i
            self.size[i] += self.size[j]
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    def components(self):
        count = 0
        for i in range(self.length):
            if i == self.root(i):
                count +=1
        return count
    def find(self, i):
        max = i
        root = self.root(i)
        for id in range(i, self.length): # no need to ask for elements below i
            if self.root(id) == root:
                if id > max:
                    max = id
        return max

C = 0

# CREATE AND POPULATE

with fileinput.input(files='social_network_friendships.txt') as f:
    for line in f:
        if not ' ' in (line):
            X = social(int(line))
            C = X
            print(X.nodes)
            continue
        data = line.split()
        p = int(data[0])
        q = int(data[1])
        t = int(data[2])
        if not(X.connected(p, q)):
            X.union(p, q)
            if X.components() == 1:
                print('Total group friendship achieved.')
                print('Timestamp: ', t)
                break

print(C.nodes)
print(C.size)
