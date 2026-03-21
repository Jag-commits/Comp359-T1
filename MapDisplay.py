import pygame
from MazeGraph import buildGraph
from MazeGraph import Node

blockSize = 40
hRes = 800
vRes = 600

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Maze Display")
clock = pygame.time.Clock()
running = True

unions = [[(0,1), (1,1)], [(0,2), (1,2)], [(1,2), (1,3)], [(1,1), (1,2)], [(2,0), (2,1)], [(2,1), (2,2)]]  # Example union operations

queue = buildGraph("QuickFind", 0, 1, 10, 10, verbose=False)

screen.fill((255,255,255))  # Clear the screen with white


for x in range((hRes) // blockSize):
    for y in range((vRes) // blockSize):
        pygame.draw.rect(screen, (0,0,0), (x*blockSize, y*blockSize, blockSize, blockSize), 1)  # Draw grid

for union in unions:
    x1, y1 = union[0]
    x2, y2 = union[1]

    """This section deals with the weird overlap of just removing the white lines by adding padding/buffer to line endings"""
    if x1 == x2:  # Vertical union
        if y1 < y2:
            pygame.draw.line(screen, (255,255,255), (x1*blockSize, y1*blockSize + 1), (x2*blockSize, y2*blockSize - 1), 4)  # Draw union as a line
        
        else:
            pygame.draw.line(screen, (255,255,255), (x1*blockSize, y1*blockSize - 1), (x2*blockSize, y2*blockSize + 1), 4)  # Draw union as a line
    
    elif y1 == y2:  # Horizontal union
        if x1 < x2:
            pygame.draw.line(screen, (255,255,255), (x1*blockSize + 1, y1*blockSize), (x2*blockSize - 1, y2*blockSize), 4)  # Draw union as a line
        
        else:
            pygame.draw.line(screen, (255,255,255), (x1*blockSize - 1, y1*blockSize), (x2*blockSize + 1, y2*blockSize), 4)  # Draw union as a line
            




"""
for x in range (width):
        for y in range (height):
            if x < width:
                if [(x, y), (x+1, y)] not in unions:
                    print([(x, y), (x+1, y)])
                    pygame.draw.line(screen, (0,0,0), (x*blockSize, y*blockSize), (x*blockSize+blockSize, y*blockSize), 2)  # Top wall
            if y < height:
                if [(x, y), (x, y*+1)] not in unions:
                    pygame.draw.line(screen, (0,0,0), (x*blockSize, y*blockSize), (x*blockSize, y*blockSize+blockSize), 2)  # Left wall
            if x > 0:
                if [(x, y), (x-1, y)] not in unions:
                    pygame.draw.line(screen, (0,0,0), (x*blockSize, y*blockSize), (x*blockSize-blockSize, y*blockSize), 2)  # Bottom wall
            if y > 0:
                if [(x, y), (x, y-1)] not in unions:
                    pygame.draw.line(screen, (0,0,0), (x*blockSize, y*blockSize), (x*blockSize, y*blockSize-blockSize), 2)  # Right wall
"""


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    clock.tick(60)
pygame.quit()
