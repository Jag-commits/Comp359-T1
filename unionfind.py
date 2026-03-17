# this is one of the Union-Find methods that is used to find the connected components in the maze
# it is used to find the connected components in the maze and to union the components

class UnionFind:
    def __init__(self, numOfElements):
        self.parent = self.makeSet(numOfElements)
        self.size = [1]*numOfElements
        self.count = numOfElements
    
    def makeSet(self, numOfElements):
        return [x for x in range(numOfElements)]

    # Time: O(logn) | Space: O(1)
    def find(self, node):
        while node != self.parent[node]:
            # path compression
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    # Time: O(1) | Space: O(1)
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        # already in the same set
        if root1 == root2:
            return

        if self.size[root1] > self.size[root2]:
            self.parent[root2] = root1
            self.size[root1] += 1
        else:
            self.parent[root1] = root2
            self.size[root2] += 1
        
        self.count -= 1

    #helper
    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)
