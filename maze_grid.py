# it builds the maze using Kruskal's algorithm and some version of Union-Find(UnionFind.py)
# it also keeps track of the number of some statistics that are used for generating the maze

import random
import time
from unionfind import UnionFind


class MazeGrid:
    def __init__(self, rows, cols, target_components=1, uf_class=UnionFind):
        self.rows = rows
        self.cols = cols
        self.total_cells = rows * cols
        self.target_components = max(1, min(target_components, self.total_cells)) #Should never be less then 1!, should never be more then total cells! we take the max value from either total cells or targeted components
        self.uf_class = uf_class #what union find we should use(as we will have different types later)

        # Walls are stored as tuples 
        self.all_walls = self._create_walls()
        self.open_passages: set[tuple[int, int]] = set()

        # Stats for later
        self.num_find_operations = 0
        self.num_union_operations = 0
        self.generation_time = 0.0

    def _cell_index(self, row, col):
        #2D to 1D."
        return row * self.cols + col
        '''
         2d (3x4 grid)                     1d flattened cells
        (row,col)

        
        (0,0) (0,1) (0,2) (0,3)             0   1   2   3
        (1,0) (1,1) (1,2) (1,3)   --->      4   5   6   7
        (2,0) (2,1) (2,2) (2,3)             8   9  10  11
        
        Notice: Multipying by cols puts each one in the correct row and adding col moves us on that row, meaning
        2d       1d
        (0,0) -> 0
        (0,1) -> 1
        (0,2) -> 2
        (0,3) -> 3

        (1,0) -> 4
        (1,1) -> 5
        (1,2) -> 6
        (1,3) -> 7

        (2,0) -> 8
        (2,1) -> 9
        (2,2) -> 10
        (2,3) -> 11
        '''
        
        
    def _create_walls(self):
        #Adds walls to all its neighboring cells, if they exist
        walls = []
        for row in range(self.rows):
            for col in range(self.cols):
                cell_idx = self._cell_index(row, col)
                if col + 1 < self.cols:
                    walls.append((cell_idx, self._cell_index(row, col + 1)))  # Right neighbor
                if row + 1 < self.rows:
                    walls.append((cell_idx, self._cell_index(row + 1, col)))  # Bottom neighbor
                #walls to the left and top are already *implied* to be created, so we dont need a case for that
        return walls

    def generate(self):
        #uf is union find (:
        uf = self.uf_class(self.total_cells) 
        random.shuffle(self.all_walls) #we have all the walls, shuffle to order. Otherwise we remove the walls in the same order every time
                                       #alternatively each wall could get a weight when created, both are similar ideas

        self.open_passages.clear()
        self.num_find_operations = 0
        self.num_union_operations = 0

        start_time = time.perf_counter()

        for wall in self.all_walls: #for each wall in Kruskals
            if uf.count <= self.target_components:
                break # if we reach the target compents stop
            cell_a, cell_b = wall #cell a and b are 2 cells seperated by a wall
            self.num_find_operations += 2 
            if not uf.connected(cell_a, cell_b): # if not connected, remove the wall
                uf.union(cell_a, cell_b)
                self.num_union_operations += 1
                self.open_passages.add(wall)
            #IF connected, do nothing. This would make a cycle

        self.generation_time = time.perf_counter() - start_time

    def is_wall_removed_between(self, row1, col1, row2, col2): #helper for later
        cell_a = self._cell_index(row1, col1)
        cell_b = self._cell_index(row2, col2)
        return (cell_a, cell_b) in self.open_passages or (cell_b, cell_a) in self.open_passages
