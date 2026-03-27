from implementations.registry import get_uf_class
from scipy.stats import bernoulli
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
def checkWalls(currentNode,n):
    if n==1:
        #N,S appear 3 times more in list
        walls=[]
        walls.extend([0]*3)
        walls.extend([1]*3)
        walls.extend([2,3])
    if n==2:
        #W,E appear 3 times more in list
        walls=[]
        walls.extend([2]*3)
        walls.extend([3]*3)
        walls.extend([0,1])
    else:
        walls = [0, 1, 2, 3]
    random.shuffle(walls)

    for Wall in walls:
        match Wall:
            case 0:
                if currentNode.N == 1:
                    return {"coord": currentNode.NIndex, "Cardinal": "N"}
            case 1:
                if currentNode.S == 1:
                    return {"coord": currentNode.SIndex, "Cardinal": "S"}
            case 2:
                if currentNode.E == 1:
                    return {"coord": currentNode.EIndex, "Cardinal": "E"}
            case 3:
                if currentNode.W == 1:
                    return {"coord": currentNode.WIndex, "Cardinal": "W"}

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
    


#ufClass = Class Name of implementation, n= selecting randomized variable, c = connected regions, x = width, y = length
#n=1: 70% chance of opening vertical walls, 30% chance or horizontal walls, n=2 the opposite of n=1, n=3 (restarting on this one, bernouli won't work since we still need x # of connected regions)
def buildGraph(ufClass, n=0, c=int,x=int, y=int, verbose=False):
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

            currentNode.y = rowlength
            currentNode.x = columnlength


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
        #random statistical variables go here
        checkWallsResult = checkWalls(currentNode,n)
        if checkWallsResult ==None: continue
        availableNeighbor = checkWallsResult["coord"]
        neighborNum = gridBoxes[availableNeighbor[1]][availableNeighbor[0]]
        if uf.find(currentNode.index)!=uf.find(neighborNum.index):
            openWalls(currentNode,neighborNum,checkWallsResult["Cardinal"])
            uf.union(currentNode.index,neighborNum.index)
            if verbose:
                print(f"Union with {currentNode.index},{neighborNum.index}")
            connectedRegions-=1
   
    return gridBoxes
    
def wall_segments(grid):
    #this is used by the pygames file to draw the walls
    # 0 = open, 1 = closed, -1 = edge on that side.

    # yield is like return but it keeps ongoing until the function is done, so it will run for all rows in the range num_rows
    # so this means every cell in the grid is visited once, going row by row, 
    num_rows, num_columns = len(grid), len(grid[0])
    for rows in range(num_rows):
        for columns in range(num_columns):
            node = grid[rows][columns]

            if rows == 0: #this is the top row, so we need to draw the top wall
                yield ((columns, rows), (columns + 1, rows))

            if columns == 0: #this is the left column, so we need to draw the left wall
                yield ((columns, rows), (columns, rows + 1))

            # this is the right colum, or inner an vertical wall 
            if columns == num_columns - 1 or node.E == 1:
                yield ((columns + 1, rows), (columns + 1, rows + 1))

            #  this is the bottom row, or inner a horizontal wall
            if rows == num_rows - 1 or node.S == 1:
                yield ((columns, rows + 1), (columns + 1, rows + 1))

            #those are all the cases, since we start in the top right, we dont need to check the top or left walls
            #we can assume they are already correct.


"""
for reference: 

0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15
"""
if __name__ == "__main__":
    x= buildGraph("QuickFind",1,5,4,4, verbose=True)  #should be 4 arrays of 4 elements
    for i in range(4):
        for j in range(4):
            print(x[i][j].index)
            print(f"{x[i][j].N},{x[i][j].S},{x[i][j].E},{x[i][j].W}")
