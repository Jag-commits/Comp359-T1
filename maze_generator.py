import argparse

from maze_grid import MazeGrid



def print_maze(maze):
    rows, cols = maze.rows, maze.cols

    # top 
    print("+" + "---+" * cols)

    for r in range(rows):
        # vertical 
        line1 = "|"
        # horizontal 
        line2 = "+"

        for c in range(cols):
            line1 += "   "

            # check right wall
            if c < cols - 1 and maze.is_wall_removed_between(r, c, r, c+1):
                line1 += " "
            else:
                line1 += "|"

            # check bottom wall
            if r < rows - 1 and maze.is_wall_removed_between(r, c, r+1, c):
                line2 += "   +"
            else:
                line2 += "---+"

        print(line1)
        print(line2)


def main():
    # this allows the user to specify the number of rows, columns, and components for the maze in the command line
    # it looks bad, but its just for the command line and very nice to have for testing

    # see this by running python3 .\maze_generator.py -h
    # change the size by running python3 .\maze_generator.py --rows 10 --cols 10 --components 1
    
    parser = argparse.ArgumentParser(description="Generate a 2D maze with Union-Find (Using Kruskal's algorithm)")
    parser.add_argument("--rows", type=int, default=30, help="Number of rows (default 30)")
    parser.add_argument("--cols", type=int, default=30, help="Number of columns (default 30)")
    parser.add_argument("--components", type=int, default=1, help="default is 1 (perfect maze)")
    args = parser.parse_args()

    # create the maze
    maze = MazeGrid(args.rows, args.cols, args.components)
    maze.generate()


    print_maze(maze)
    #draw_maze(maze) #using pygame?


if __name__ == "__main__":
    main()

