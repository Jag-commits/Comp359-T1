## quick find implementation


class quickfind:
    def __init__(self, n):
        self.id = list(range(n)) 

    def find (self,p):
        return self.id[p] # constant time find
    
    def connected(self, p, q):
        return self.find(p) == self.find(q) #true if connected
    
    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)

        for i in range(len(self.id)): # changes all of the elements from one group to the next group when union is called
            if self.id[i] == pid:
                self.id[i] = qid


uf = quickfind(7)
uf.union(1,2)
uf.union(2,5)
print(uf.id)
print(uf.connected(1,2))
print(uf.connected(1,4))
