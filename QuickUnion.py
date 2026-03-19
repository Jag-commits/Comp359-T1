#This is one of the testable Union and Find options 
#Note- not made to directly work with MazeGraph as it wont be the best Union Find Implementation

class QuickUnion:

    def __init__(self, n):
        #All nodes are their own parent allowing for each node to begin as its own set
        self.parent = [i for i in range(n)]

    def Find(self, p):
        #Find the root node of the set by working up the tree
        while p != self.parent[p]:
            p = self.parent[p]
        return p
    
    def Union(self, p, q):
        rootP = self.Find(p)
        rootQ = self.Find(q)

        #If already connected do nothing
        if rootP == rootQ:
            return
        #Connect the roots
        self.parent[rootP] = rootQ

    def Connected(self, p, q):
        #Return True if both nodes share the same root
        return self.Find(p) == self.Find(q)

#Test
uf = QuickUnion(10)

print("Initial:", uf.parent)

uf.Union(1, 7)
uf.Union(2, 7)

print("After unions:", uf.parent)

print("Find(1):", uf.Find(1))
print("Find(7):", uf.Find(7))

print("Connected(1,7):", uf.Connected(1,7))
print("Connected(1,9):", uf.Connected(1,9))