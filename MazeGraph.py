from implementations.registry import get_uf_class
import random
class Node:
        def __init__(self,n):
            #Index
            self.index = n

            self.x = 0
            self.y = 0
           

            #cardinal directions represent the walls. 0 = Open, 1 = Closed, -1 = Edge
            self.N=1
            self.S=1
            self.W=1
            self.E=1

            #coordinates of i,j
            self.NIndex=(0,0)
            self.SIndex=(0,0)
            self.WIndex=(0,0)
            self.EIndex=(0,0)

#Check for avaialable walls, send coordinates and Cardinal Dir
def checkWalls(currentNode):
    if currentNode.N==1:
        return {"coord": currentNode.NIndex, "Cardinal" :"N"}
    elif currentNode.S==1:
        return {"coord": currentNode.SIndex, "Cardinal" :"S"}
    elif currentNode.E==1: 
        return {"coord": currentNode.EIndex, "Cardinal" :"E"}
    elif currentNode.W==1: 
        return {"coord": currentNode.WIndex, "Cardinal" :"W"}
    return None


def openWalls(currentNode:Node,neighborNode:Node,Cardinal:str):
    if Cardinal == "N":
        currentNode.N= 0
        neighborNode.S=0
    elif Cardinal == "S":
        currentNode.S= 0
        neighborNode.N=0
    elif Cardinal == "E":
        currentNode.E= 0
        neighborNode.W=0
    elif Cardinal == "W":
        currentNode.W= 0
        neighborNode.E=0
    else:
        print("Error: No Valid Cardinal")
    

#If the node is on the edge of the matrix, it cannot have the associated neighbor
def checkEdge(currentNode, x,y, columnlength, rowlength): #y is row, x is col 
    if rowlength==(y-1): currentNode.S=-1
    if rowlength==0: currentNode.N =-1
    if columnlength==(x-1): currentNode.E=-1
    if columnlength==0: currentNode.W =-1
    


#ufClass = Class Name of implementation, n= selecting randomized variable, c = connected regions, x = width, y = length, outputArray = return 2d array instead of Queue
# Index = Node.index; index: 0-> X*Y
def buildGraph(ufClass, n=int, c=int,x=int, y=int, verbose=False,outputArray=False):
    output = []
    numBoxes = x*y 
    connectedRegions = numBoxes
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

            currentNode.x = rowlength
            currentNode.y = columnlength


            rowValue[columnlength]=(currentNode)
            currentNum+=1
            
        gridBoxes[rowlength]=rowValue

    # registry key to class
    if isinstance(ufClass, str):
        ufClass = get_uf_class(ufClass)

    # this changes which union find we are using
    uf = ufClass(numBoxes)
    print("Using UF class:", uf.__class__.__name__)
  
    
    while c < connectedRegions:
        randomX,randomY  = random.randint(0,(x)-1), random.randint(0,(y)-1)
        currentNode = gridBoxes[randomY][randomX]
        checkWallsResult = checkWalls(currentNode)
        if checkWallsResult ==None: continue
        availableNeighbor = checkWallsResult["coord"]
        neighborNum = gridBoxes[availableNeighbor[1]][availableNeighbor[0]]
        if uf.find(currentNode.index)!=uf.find(neighborNum.index):
            openWalls(currentNode,neighborNum,checkWallsResult["Cardinal"])
            uf.union(currentNode.index,neighborNum.index)
            if verbose:
                print(f"Union with {currentNode.index},{neighborNum.index}")
            output.append(currentNode)
            connectedRegions-=1
    if outputArray:
        #Return both the 2D array and the Queue
        return {"Queue":output, "List":gridBoxes}
    return output



"""
for reference: 

0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15
"""
if __name__ == "__main__":
    x= buildGraph("QuickFind",10,5,4,4, verbose=True,outputArray=True)  #should be 4 arrays of 4 elements
    x=x["List"]
    for i in range(4):
        for j in range(4):
            print(x[i][j].index)
            print(f"{x[i][j].N},{x[i][j].S},{x[i][j].E},{x[i][j].W}")
