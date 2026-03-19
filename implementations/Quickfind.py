from .UnionFindAbtract import Template
# abstract base class template
# run like python -m implementations.Quickfind if you want to run the main
## quick find implementation


class QuickFind(Template):
    def __init__(self, n: int):
        self.id = list(range(n)) 

    def find (self,p):
        return self.id[p] # constant time find
    
    def connected(self, p, q):
        return self.find(p) == self.find(q) #true if connected
    
    def union(self, p: int, q: int) -> None:
        pid = self.find(p)
        qid = self.find(q)

        for i in range(len(self.id)): # changes all of the elements from one group to the next group when union is called
            if self.id[i] == pid:
                self.id[i] = qid


if __name__ == "__main__":
    uf = QuickFind(7)
    uf.union(1, 2)
    uf.union(2, 5)
    print(uf.id)
    print(uf.connected(1, 2))
    print(uf.connected(1, 4))
    print("test")
