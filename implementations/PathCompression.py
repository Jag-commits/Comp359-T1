from .UnionFindAbtract import Template
# abstract base class template
# run like python -m implementations.PathCompression if you want to run the main
## Union Find by path compression implementation

class PathCompression(Template):
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find (self,p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p]) # path compression step, makes the parent of p point to the root of the tree
    
        return self.parent[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p: int, q: int) -> None:
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            if self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            elif self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

            return True

        return False


#if __name__ == "__main__":
    


"""https://www.youtube.com/watch?v=VHRhJWacxis - Video By WilliamFiset On Path Compression to help me understand theory"""