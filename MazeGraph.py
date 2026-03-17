from unionfind import *
import random
class Node:
        def __init__(self,n):
            self.n = n
            #cardinal directions represent the walls
            #Maybe set the cardinal directions to the index they're connected to?

            #If we set these to be the carinal directions, then you can delete the associated index to represent an open wall.
            self.N=1
            self.S=1
            self.W=1
            self.E=1

            #Have to be coordinates of i,j
            self.NIndex=(0,0)
            self.SIndex=(0,0)
            self.WIndex=(0,0)
            self.EIndex=(0,0)


def checkWalls(currentNode):
    if currentNode.N==1:
        currentNode.N= 0
        return currentNode.NIndex
    elif currentNode.S==1:
        currentNode.S= 0
        return currentNode.SIndex
    elif currentNode.E==1:
        currentNode.E= 0
        return currentNode.EIndex
    elif currentNode.W==1:
        currentNode.W= 0
        return currentNode.WIndex
    return None

#If the node is on the edge of the matrix, it cannot have the associated neighbor
def checkEdge(currentNode, x,y, columnlength, rowlength): #y is row, x is col 
    if rowlength==(y-1): currentNode.S=0
    if rowlength==0: currentNode.N =0
    if columnlength==(x-1): currentNode.E=0
    if columnlength==0: currentNode.W =0



    #Needs to output array with node positions and what they're connected to ie retain position data
    #So maybe create an adjacency list that represents what nodes it's connected to from the norht, south, east west?
def buildGraph(n=int, c=int,x=int, y=int):
    numBoxes = x*y 
    #How to determine the number of connected regions?
    connectedRegions = numBoxes
    #The plan was to make some sort of randomized picker for the walls of a grid between the node and another node

    #Create the boxes themselves -> 2d Matrix
    currentNum = 0
    gridBoxes = [None]*y # y = num of rows
    for rowlength in range(y):
        rowValue = [None]*x # x= num of columns
        for columnlength in range(x):
            currentNode = Node(currentNum) #Node coordinates x,y

            checkEdge(currentNode,x,y,columnlength,rowlength)

            currentNode.NIndex= (columnlength,rowlength-1)
            currentNode.SIndex= (columnlength,rowlength+1)
            currentNode.EIndex= (columnlength+1,rowlength)
            currentNode.WIndex= (columnlength-1,rowlength)

            rowValue[columnlength]=(currentNode)
            currentNum+=1
        gridBoxes[rowlength]=rowValue

    # ______________________Replace this with what the actual UnionFind returns______________________
    uf = UnionFind(numBoxes)

    #Maybe loop until you get all the connected regions made?
    while c < connectedRegions:
        randomX,randomY  = random.randint(0,(x)-1), random.randint(0,(y)-1)
        currentNode = gridBoxes[randomX][randomY]
        availableNeighbor = checkWalls(currentNode)
        if availableNeighbor ==None: continue
        neighborNum = gridBoxes[availableNeighbor[0]][availableNeighbor[1]]
        if uf.find(currentNode.n)!=uf.find(neighborNum.n):
            uf.union(currentNode.n,neighborNum.n)
            print(f"Union with {currentNode.n},{neighborNum.n}")
            connectedRegions-=1
        
        



    #So each ID 0->N represents the object

    #The UnionFind is just a check, the array is what you really want

    #note: Pick node at random, look at avaialble wall and that is the node you want to connect to
    
buildGraph(10,5,4,4)  #should be 10 arrays of 10 elements

# Return should be an adjacency list of all the nodes and what connection exists between the node and it's NSWE Node: N,S,W,E
 