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


# Assignment Plan
1) Implement different variations of Union and Find such as Quick Find, Quick Union, Path Compression, Union by Rank etc.
2) Compare these variations runtimes for both Union and Find.  
3) Using an efficient variant of the data structure create 2D mazes with input parameters for its size.
4) Using statistics random variables such as random and poisson see how the maze generation gets effected with these differing variables.  
5) Create a maze searching/solving algorithm to solve the created mazes.  
6) Visually display these mazes and their solving to the user with a clean GUI.

Team Planning Files: https://drive.google.com/drive/folders/1D0Zv-jDg2stmmtaUT6hYRIS_4WbXMhoC?usp=sharing

# Results
We implemented four UnionFind algorithms in Python (Quick Find, Quick Union, Path Compression, Union by Rank) and compared the efficiency of each operation across multiple input sizes:

We also created another implementation of quick find in Java and compared the efficiency differences between languages:

Using the UnionFind implementation, we created a random maze algorithm, visualized with PyGame, which generates a unique maze at runtime. When generated with one component, all spaces in the maze are part of one subset, and there is a path between any two grid cells.

To solve the generated maze, an A* search algorithm was implemented, and its solution is displayed over the generated maze




# Work Logs
*see logs folder for development screenshots*
- Brayden:
- Joel: https://youtu.be/K4kGVkSzDbY
- Alexander:
- Jacob:
- Jagpreet:
- Natasha




# Bibliography

- Potato Coders. (2020, December 3). Union Find in 5 minutes — Data Structures & Algorithms. YouTube. https://www.youtube.com/watch?v=ayW5B2W9hfo
- Sedgewick, R., & Wayne,K.(2011).Algorithms,Fourth Edition. Addison-Wesley Professional
- WilliamFiset. (2017, April 7). Union Find Path Compression. Youtube https://www.youtube.com/watch?v=VHRhJWacxis
- **Pygame**
