from UnionFindAbtract import Template # abstract base class template
#This is one of the testable Union and Find options 


class QuickUnion(Template):
    def __init__(self, n: int):
        #All nodes are their own parent allowing for each node to begin as its own set
        self.parent = [i for i in range(n)]

    def find(self, p: int) -> int:
        #Find the root node of the set by working up the tree
        while p != self.parent[p]:
            p = self.parent[p]
        return p
    def union(self, p: int, q: int) -> None:
        rootP = self.find(p)
        rootQ = self.find(q)
        #If already connected do nothing
        if rootP == rootQ:
            return
        #Connect the roots
        self.parent[rootP] = rootQ

    def connected(self, p: int, q: int) -> bool:
        #Return True if both nodes share the same root
        return self.find(p) == self.find(q)

#Test
if __name__ == "__main__":
    uf = QuickUnion(10)

    print("Initial:", uf.parent)
    uf.union(1, 7)
    uf.union(2, 7)
    print("After unions:", uf.parent)
    print("Find(1):", uf.find(1))
    print("Find(7):", uf.find(7))
    print("Connected(1,7):", uf.connected(1, 7))
    print("Connected(1,9):", uf.connected(1, 9))
