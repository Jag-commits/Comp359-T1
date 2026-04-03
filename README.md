# Comp359 - Design & Analysis of Algorithms - Assignment 3

This is Group 1's submission for the third assignment of Comp359, Design & Analysis of Algorithms. 

Group 1 Members:
- Brayden Schneider  
- Joel Algera  
- Alexander Calderon  
- Jacob Thompson  
- Jagpreet Dhaliwal  
- Natasha Maundu  


Given Prompt (Number One) - UnionFind variations
  * compare three different implementations and the runtimes of find and union operations
  * apply UnionFind to construct 2D mazes given input parameters for number of cells N, dimensions rows X, columns Y and number of connected components C (i.e., disjoint subsets)
  * explore how you can design changes in maze structure using statistics random variables of different kinds  

# How to Run

## Prerequisites
Required Libraries: Pygame

Commands:

`pip install pygame`

## Running Program

All Configurable Features:
- Specific Union Find Implementation
- Number of Rows
- Number of Columns
- Number of Connected Regions
- Random Statistical Variables (0 = standard, 1 = Vertical Corridors, 2 = Horizontal Corridors, 3 = Circular Pattern (Must be an nxn maze)
- Print node unions
  
The GUI interface allows you to access the following:
- Number of Rows
- Number of Columns
- Maze Solver

To configure additional features use the following:

`python3 .\main.py --ufClass {Configure} --rows {Configure} --cols {Configure} --components {Configure} --random {Options: 0,1,2,3} --verbose`

Ex) `python3 .\main.py --ufClass PathCompression --rows 25 --cols 25 --components 1 --random 0`

View All Feature Descriptions: `python3 .\main.py --h`

*Note: adding verbose prints the individual unions between nodes

# Assignment Plan
1) Implement different variations of Union and Find such as Quick Find, Quick Union, Path Compression, Union by Rank etc.
2) Compare these variations runtimes for both Union and Find.  
3) Using an efficient variant of the data structure create 2D mazes with input parameters for its size.
4) Using statistics random variables to bias specific wall openings and see how the maze generation gets effected with these differing variables.  
5) Create a maze searching/solving algorithm to solve the created mazes.  
6) Visually display these mazes and their solving to the user with a clean GUI.

Team Planning Files: https://drive.google.com/drive/folders/1D0Zv-jDg2stmmtaUT6hYRIS_4WbXMhoC?usp=sharing

# Results
We implemented four UnionFind algorithms in Python (Quick Find, Quick Union, Path Compression, Union by Rank) and compared the efficiency of each operation across multiple input sizes:

We also created another implementation of quick find in Java and compared the efficiency differences between languages:

The results of these efficiency tests are shown in the graphs below:
<img width="2942" height="1975" alt="COMP359Project3_SmallDataTest" src="https://github.com/user-attachments/assets/86ebd0c2-9753-4488-9002-7251c1dfd502" />
<img width="2484" height="1943" alt="COMP359Project3_MediumDataTest" src="https://github.com/user-attachments/assets/2d8329ac-6863-487a-97bf-926dde54513e" />
<img width="2516" height="1938" alt="COMP359Project3_LargeDataTest" src="https://github.com/user-attachments/assets/09968e8b-378f-4d84-a7e0-8343301706ac" />
<img width="2461" height="1934" alt="COMP359Project3_ChainedDataTest" src="https://github.com/user-attachments/assets/125bbc37-3a64-42a9-bc50-2508149480e7" />

As we would expect the more complex impementations of Path Compression and Union By Rank are vastly more efficient when it comes to both the Union and find operations when compared to the simpler Quick Union and Quick Find implementations. Although the simpler implementations are comparable when it comes to their specified operation as a whole they are not as practical as the others. This speed by Path Compression and Union By Rank comes from the work they do to reorder the trees into more manageable systems. These reordered trees are far easier to union and faster to locate nodes than leaving the trees as they began. As shown in the graphs when the amount of inputs in the trees is increased the gap of the simpler to more complex implementations only grow.

Using the UnionFind implementation, we created a random maze algorithm, visualized with PyGame, which generates a unique maze at runtime. When generated with one component, all spaces in the maze are part of one subset, and there is a path between any two grid cells.

To solve the generated maze, an A* search algorithm was implemented, and its solution is displayed over the generated maze

## Random Statistical Variables

Random Stastical Variables are used to influence the probability of opening particular walls between nodes when generating the maze.

Walls are defined as the following: North = 0, South = 1, East = 2, West = 3.

#### 0) Standard:               

$X = \\{0, 1, 2 ,3\\}$

| x | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P(X=x) | 0.25 | 0.25 | 0.25 | 0.25 |

#### 1) Vertical Corridors:

$X = \\{0, 1, 2 ,3\\}$

| x | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P(X=x) | 0.375 | 0.375 | 0.125 | 0.125 |

#### 2) Horizontal Corridors:

$X = \\{0, 1, 2 ,3\\}$

| x | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P(X=x) | 0.125 | 0.125 | 0.375 | 0.375 |

#### 3) Circular (Closest Wall to Center):

This method does not set static probabilities to certain directions.

$$
X = \\{W_1, W_2, W_3, W_4\\}
$$

$$P(X = W_i) = 
\begin{cases} 
0.85 & \text{if } W_i = \text{ Closest Wall } \\
0.05 & \text{otherwise } 
\end{cases} $$




# Work Logs
*see logs folder for development screenshots*
- Brayden: https://youtu.be/QOmA8hE1Sko
- Joel: https://youtu.be/K4kGVkSzDbY
- Alexander: https://youtu.be/J-dTH17Fcxo
- Jacob: All logs shown in Log Folder
- Jagpreet: https://www.youtube.com/watch?v=ddr8Ht8NS5U (Check Description for Timestamps)
- Natasha: Logs in Log Folder




# Bibliography

- Potato Coders. (2020, December 3). Union Find in 5 minutes — Data Structures & Algorithms. YouTube. https://www.youtube.com/watch?v=ayW5B2W9hfo
- Sedgewick, R., & Wayne,K.(2011).Algorithms,Fourth Edition. Addison-Wesley Professional
- WilliamFiset. (2017, April 7). Union Find Path Compression. Youtube https://www.youtube.com/watch?v=VHRhJWacxis
- LaTeX/Mathematics. (2026, March 21). Wikibooks. https://en.wikibooks.org/wiki/LaTeX/Mathematics
- **Pygame**
- take U forward. (2022, October 22). Disjoint Set | Union by Rank | Union by Size | Path Compression. YouTube. https://youtu.be/aBxjDBC4M1U?si=iwJjPUffQIsgTJ7L
