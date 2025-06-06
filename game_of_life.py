import pygame
import random

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de la Vie avec Bord Toroïdal")
clock = pygame.time.Clock()

def init_grid():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid(grid):
    for y in range(ROWS):
        for x in range(COLS):
            color = WHITE if grid[y][x] == 1 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def count_neighbors(grid, x, y):
    neighbors = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx = (x + dx) % COLS
            ny = (y + dy) % ROWS
            neighbors += grid[ny][nx]
    return neighbors

def update_grid(grid):
    new_grid = [[0] * COLS for _ in range(ROWS)]
    for y in range(ROWS):
        for x in range(COLS):
            neighbors = count_neighbors(grid, x, y)
            if grid[y][x] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1
    return new_grid

def create_random_soup(grid):
    for y in range(ROWS):
        for x in range(COLS):
            if random.random() < 0.2:
                grid[y][x] = 1

def main():
    grid = init_grid()
    running = True
    game_running = False

    while running:
        screen.fill(BLACK)
        draw_grid(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = mouse_x // CELL_SIZE
                grid_y = mouse_y // CELL_SIZE
                if event.button == 1:
                    grid[grid_y][grid_x] = 1 - grid[grid_y][grid_x]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_running = not game_running
                elif event.key == pygame.K_LALT:
                    grid = init_grid()
                    create_random_soup(grid)
                elif event.key == pygame.K_RALT:
                    grid = init_grid()

        if game_running:
            grid = update_grid(grid)

        pygame.display.update()
        clock.tick(10)

    pygame.quit()

main()
