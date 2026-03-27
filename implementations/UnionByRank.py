from .UnionFindAbtract import Template
# abstract base class template
# run like python -m implementations.UnionByRank if you want to run the main
## Union Find by rank implementation

class UnionByRank(Template):
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, p):
        while self.parent[p] != p:  # this would traverse until we reach the root
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int) -> None:
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ      # attaches the smaller tree under bigger tree
            elif self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP      # attach smallr tree uder bigger
            else:
                self.parent[rootQ] = rootP      # equal rank, pick one as root
                self.rank[rootP] += 1           # this only increases when ranks are equal
            return True
        return False
