import argparse
from pygame_grid import run as pygame_draw
from implementations.registry import UF_REGISTRY
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
    parser.add_argument("--ufClass",type=str,default="QuickFind",choices=UF_REGISTRY.keys(),help="Union-Find implementation",)
    parser.add_argument("--rows", type=int, default=5, help="Number of rows")
    parser.add_argument("--cols", type=int, default=5, help="Number of columns")
    parser.add_argument("--components",type=int,default=1,help="Target number of connected components (1 = perfect maze)",)
    parser.add_argument("--random",type=int,default=0,choices=[0,1,2,3],help="0 = Std, 1 = Vertical Corridors, 2 = Horizontal Corridors, 3 = Circular (Must be n x n)",)
    parser.add_argument("--verbose",action="store_true", help="Print each union operation during maze generation",)
    parser.add_argument("--autoplay", type=bool, default=0, help="autoplay 0 = false, 1 =true")
    parser.add_argument("--speed", type=int, default=60, help="how fast the solver runs")
    args = parser.parse_args()

    pygame_draw(
        args.ufClass,
        args.rows,
        args.cols,
        args.components,
        args.random,
        verbose=args.verbose,
        autoplay=args.autoplay,
        speed=args.speed
    )
    
#ding input to the pygame window, to allow the user to change this easier
    # running the file will make a 5x5 defult size you can change the size using the parser right now
    # see above, the new maze button will help us with this!

if __name__ == "__main__":
    main()
