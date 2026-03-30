import pygame

from MazeGraph import buildGraph, wall_segments
from pathPlanning import aStar

#All colors 
BG_COLOR = (255, 255, 255)
WALL_COLOR = (0, 0, 0)
CELL_COLOR = (255, 255, 255)
SIDEBAR_BG = (45, 45, 48)
SIDEBAR_FG = (230, 230, 230)
BUTTON_BG = (70, 70, 75)
BUTTON_HOVER = (95, 95, 105)
BUTTON_BORDER = (120, 120, 130)
PATH_COLOR = (200, 0, 0,125)

#all the sizes 
SIDEBAR_WIDTH = 200
CELL_SIZE = 20
WALL_THICKNESS = 2
PADDING = 12
FONT_SIZE = 24
SIDEBAR_PAD = 10
BUTTON_HEIGHT = 40

INPUT_H = 32
LABEL_H = 18
MAX_DIM = 50
# THESE MAKE EVERYTHING LOOK NICE AND POLISHED, feel free to change them if you find something that looks better

DROPDOWN_BG = (60, 60, 60)
DROPDOWN_HOVER = (90, 90, 90)
DROPDOWN_SELECT = (100, 120, 120)
DROPDOWN_BORDER = (100, 100, 100)

SPEED = 60
 

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


def rebuild_maze(uf_name: str, rows_text: str, cols_text: str, rows: int, cols: int, random: int, verbose: bool):
    r = max(1, min(int(rows_text.strip() or str(rows)), MAX_DIM))
    c = max(1, min(int(cols_text.strip() or str(cols)), MAX_DIM))
    grid = make_maze(uf_name, r, c, 1, random, verbose=verbose)
    pygame.display.set_caption(f"Maze {r}x{c}")
    return r, c, grid

def draw_grid(screen, grid, offset_x: int, offset_y: int, rows: int, cols: int, path=None): #helper
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

    if path:
        for (r, c) in path:
            draw_path(screen, c, r, offset_x, offset_y)

def draw_path(screen, row: int, col: int, offset_x: int, offset_y: int):
        x = offset_x + col * CELL_SIZE
        y = offset_y + row * CELL_SIZE
        alpha_surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        alpha_surface.fill(PATH_COLOR)
        screen.blit(alpha_surface, (x, y))
        #pygame.draw.rect(screen, PATH_COLOR, width = 0, rect = (x  , y , CELL_SIZE, CELL_SIZE))  Previously using rectangles
        #pygame.draw.rect(screen,PATH_COLOR,(x, y, CELL_SIZE * 0.5, CELL_SIZE *0.5))

        


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


def draw_box(screen, font, rect: pygame.Rect, text: str, focused: bool):
    if focused: bg_color = BUTTON_HOVER 
    else: bg_color = BUTTON_BG

    pygame.draw.rect(screen, bg_color, rect)
    pygame.draw.rect(screen, BUTTON_BORDER, rect, 2 if focused else 1)
    
    text_surf = font.render(text, True, SIDEBAR_FG)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)
#makes it when a key is pressed we can turn it into a number we can use
def get_keyboard_input(event: pygame.event.Event) -> str | None:
    if event.unicode and event.unicode.isdigit():
        return event.unicode #return as string
    if pygame.K_0 <= event.key <= pygame.K_9: #this is the numbers 0-9
        return str(event.key - pygame.K_0)
    if pygame.K_KP0 <= event.key <= pygame.K_KP9: #this is the keypad, why they are diffent I have no idea
        return str(event.key - pygame.K_KP0)
    return None

def run(uf_name: str, rows: int, cols: int, components: int, random: int, verbose: bool = False, autoplay = False, speed = SPEED):
    grid = make_maze(uf_name, rows, cols, components, random, verbose) 

    grid_w = cols * CELL_SIZE
    grid_h = rows * CELL_SIZE
    grid_area_w = grid_w + WALL_THICKNESS + PADDING * 2 #*2 applies to both side of the screen
    window_w = grid_area_w + SIDEBAR_WIDTH
    window_h = grid_h + WALL_THICKNESS + PADDING * 2

    pygame.init()
    screen = pygame.display.set_mode((window_w, window_h), pygame.RESIZABLE)
    pygame.display.set_caption(f"Maze {rows}x{cols}")
    font = pygame.font.Font(None, FONT_SIZE)
    clock = pygame.time.Clock()
    rows_text = str(rows)
    cols_text = str(cols)
    active_input = None  # None | rows | cols

    show_solution = False
    is_playing = autoplay
    SPEED = max(1, speed)
    running = True
    while running:
        window_w, window_h = screen.get_size()
        sidebar = pygame.Rect(window_w - SIDEBAR_WIDTH, 0, SIDEBAR_WIDTH, window_h)
        btn_w = sidebar.w -SIDEBAR_PAD * 2
        row_input_y = SIDEBAR_PAD + LABEL_H + 2
        rect_rows = pygame.Rect(sidebar.x + SIDEBAR_PAD, row_input_y, btn_w, INPUT_H)
        col_label_y = row_input_y + INPUT_H + 6
        col_input_y = col_label_y + LABEL_H + 2
        rect_cols = pygame.Rect(sidebar.x + SIDEBAR_PAD, col_input_y, btn_w, INPUT_H)
        btn_new_y = col_input_y + INPUT_H + 6
        btn_new = pygame.Rect(
            sidebar.x + SIDEBAR_PAD,
            btn_new_y,
            btn_w,
            BUTTON_HEIGHT,
        )
        btn_solve = pygame.Rect(
            sidebar.x + SIDEBAR_PAD,
            btn_new_y + BUTTON_HEIGHT + SIDEBAR_PAD,
            btn_w,
            BUTTON_HEIGHT,
        )
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #windows quit button
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            #elif my life there must be a better way...
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if rect_rows.collidepoint(event.pos):
                    active_input = "rows"
                elif rect_cols.collidepoint(event.pos):
                    active_input = "cols"
                elif btn_new.collidepoint(event.pos):   # new maze button
                    active_input = None
                    rows, cols, grid = rebuild_maze(
                        uf_name, rows_text, cols_text, rows, cols, random, verbose
                    )
                    rows_text, cols_text = str(rows), str(cols)
                    show_solution = False
                elif btn_solve.collidepoint(event.pos):
                    active_input = None
                    show_solution = True

            elif event.type == pygame.KEYDOWN:
                if active_input:
                    if event.key == pygame.K_BACKSPACE:
                        if active_input == "rows":
                            rows_text = rows_text[:-1]
                        else:
                            cols_text = cols_text[:-1]
                    elif event.key == pygame.K_TAB:
                        active_input = "cols" if active_input == "rows" else "rows"
                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        active_input = None
                        rows, cols, grid = rebuild_maze(
                            uf_name, rows_text, cols_text, rows, cols, random, verbose
                        )
                        rows_text, cols_text = str(rows), str(cols)
                        show_solution = False
                    else:
                        d = get_keyboard_input(event)
                        if d is not None:
                            if active_input == "rows":
                                rows_text += d
                            else:
                                cols_text += d
                elif event.key == pygame.K_SPACE: #pause / start
                    is_playing = not is_playing
                        
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, SIDEBAR_BG, sidebar)

        if show_solution:
            path = aStar((0, 0), (cols - 1, rows - 1), grid)
            draw_grid(screen, grid, PADDING, PADDING, rows, cols, path)
        else:
            draw_grid(screen, grid, PADDING, PADDING, rows, cols)

        screen.blit(font.render("Rows", True, SIDEBAR_FG), (sidebar.x + SIDEBAR_PAD, SIDEBAR_PAD))
        screen.blit(font.render("Cols", True, SIDEBAR_FG), (sidebar.x + SIDEBAR_PAD, col_label_y))
        draw_box(screen, font, rect_rows, rows_text, active_input == "rows")
        draw_box(screen, font, rect_cols, cols_text, active_input == "cols")
        draw_button(screen, font, btn_new, "New maze", btn_new.collidepoint(mouse))
        draw_button(screen, font, btn_solve, "Solve", btn_solve.collidepoint(mouse))

        pygame.display.flip()
        clock.tick(SPEED)

    pygame.quit()
