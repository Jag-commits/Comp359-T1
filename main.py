import argparse
from MazeGraph import buildGraph
# can run with: python3 .\main.py

# see options with: python3 .\main.py --h 
# or mess up the arugments and it will yell at you

# Examples:
# python3 .\main.py --verbose 
# python3 .\main.py --rows 10 --cols 10
#python3 .\main.py --rows 10 --cols 10 --components 2 --random 0 --verbose

#change size with

def main():
    parser = argparse.ArgumentParser(description="Generate a 2d maze with Union-Find")
    parser.add_argument("--rows", type=int, default=5, help="Number of rows")
    parser.add_argument("--cols", type=int, default=5, help="Number of columns")
    parser.add_argument("--components",type=int,default=1,help="Target number of connected components (1 = perfect maze)",)
    parser.add_argument("--random",type=int,default=0,choices=[0, 1, 2, 3],help="Random strategy: 0=(python random), 1=add here, 2=add here, 3=add here",)
    parser.add_argument("--verbose",action="store_true", help="Print each union operation during maze generation",)
    args = parser.parse_args()

    queue = buildGraph(args.random,args.components,args.cols,args.rows,verbose=args.verbose,)

    #printmap(queue or list) #TODO:add this here
    #drawmap(queue or list)  #TODO:add this here using pygames maybe?
    
    print(f"Generated {args.rows}x{args.cols} maze")
    print(f"Target components: {args.components}")
    print(f"Random mode: {args.random}")
    print(f"Walls removed: {len(queue.queue)}")

if __name__ == "__main__":
    main()