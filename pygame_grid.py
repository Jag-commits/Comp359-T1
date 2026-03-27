import pygame

from MazeGraph import buildGraph, wall_segments

#All colors 
BG_COLOR = (255, 255, 255)
WALL_COLOR = (0, 0, 0)
CELL_COLOR = (255, 255, 255)
SIDEBAR_BG = (45, 45, 48)
SIDEBAR_FG = (230, 230, 230)
BUTTON_BG = (70, 70, 75)
BUTTON_HOVER = (95, 95, 105)
BUTTON_BORDER = (120, 120, 130)

#all the sizes 
SIDEBAR_WIDTH = 200
CELL_SIZE = 28
WALL_THICKNESS = 2
PADDING = 12
FONT_SIZE = 24
SIDEBAR_PAD = 10
BUTTON_HEIGHT = 40
# THESE MAKE EVERYTHING LOOK NICE AND POLISHED, feel free to change them if you find something that looks better


def make_maze(uf_name: str, rows: int, cols: int, components: int, random: int, verbose: bool = False): #helper
    maze_data = buildGraph(
        uf_name,
        random,
        components,
        cols,
        rows,
        verbose=verbose,
    )   
    return maze_data


def draw_grid(screen, grid, offset_x: int, offset_y: int, rows: int, cols: int): #helper
    # this looks really bad, but all it does is dynamicaly draw the cells and walls based on the grid 
    for r in range(rows):
        for c in range(cols):
            x = offset_x + c * CELL_SIZE
            y = offset_y + r * CELL_SIZE
            pygame.draw.rect(screen, CELL_COLOR, (x, y, CELL_SIZE, CELL_SIZE))

    for (a, b) in wall_segments(grid):
        pygame.draw.line(
            screen,
            WALL_COLOR,
            (offset_x + a[0] * CELL_SIZE, offset_y + a[1] * CELL_SIZE),
            (offset_x + b[0] * CELL_SIZE, offset_y + b[1] * CELL_SIZE),
            WALL_THICKNESS,
        )


def draw_button(screen, font, rect: pygame.Rect, label: str, hover: bool): #helper
    if hover:
        bg = BUTTON_HOVER
    else:
        bg = BUTTON_BG
    #draw button
    pygame.draw.rect(screen, bg, rect)
    pygame.draw.rect(screen, BUTTON_BORDER, rect, 1)

    #draw text
    text = font.render(label, True, SIDEBAR_FG)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)


def run(uf_name: str, rows: int, cols: int, components: int, random: int, verbose: bool = False):
    grid = make_maze(uf_name, rows, cols, components, random, verbose) 

    grid_w = cols * CELL_SIZE
    grid_h = rows * CELL_SIZE
    grid_area_w = grid_w + WALL_THICKNESS + PADDING * 2 #*2 applies to both side of the screen
    window_w = grid_area_w + SIDEBAR_WIDTH
    window_h = grid_h + WALL_THICKNESS + PADDING * 2

    pygame.init()
    screen = pygame.display.set_mode((window_w, window_h))
    pygame.display.set_caption(f"Maze {rows}x{cols}")
    font = pygame.font.Font(None, FONT_SIZE)
    clock = pygame.time.Clock()

    sidebar = pygame.Rect(grid_area_w, 0, SIDEBAR_WIDTH, window_h)
    btn_w = sidebar.w -  SIDEBAR_PAD * 2
    btn_new = pygame.Rect(
        sidebar.x + SIDEBAR_PAD,
        sidebar.y + BUTTON_HEIGHT,
        btn_w,
        BUTTON_HEIGHT,
    )

    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #windows quit button
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if btn_new.collidepoint(event.pos):  # new maze button
                    grid = make_maze(uf_name, rows, cols, components, random, verbose=verbose)
                                                     # add more buttons here
                                                     #input for width and hight and components

        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, SIDEBAR_BG, sidebar)

        draw_grid(screen, grid, PADDING, PADDING, rows, cols)

        draw_button(screen, font, btn_new, "New maze", btn_new.collidepoint(mouse))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
