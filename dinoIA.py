import pygame
import random
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Run IA")

WHITE = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

DINO_WIDTH = 50
DINO_HEIGHT = 50
dino_x = 50
dino_y = SCREEN_HEIGHT - DINO_HEIGHT - 10
dino_velocity_y = 0
gravity = 0.5
jump_strength = -10
is_jumping = False

OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 50
obstacle_speed = 5
obstacle_gap = 200
obstacles = []

font = pygame.font.Font(None, 36)
best_score = 0

def draw_dino(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, DINO_WIDTH, DINO_HEIGHT))

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, BROWN, obstacle)

def jump():
    global dino_velocity_y, is_jumping
    if not is_jumping:
        dino_velocity_y = jump_strength
        is_jumping = True

def update_game():
    global dino_y, dino_velocity_y, obstacles, score, is_jumping, best_score

    dino_velocity_y += gravity
    dino_y += dino_velocity_y

    if dino_y > SCREEN_HEIGHT - DINO_HEIGHT - 10:
        dino_y = SCREEN_HEIGHT - DINO_HEIGHT - 10
        dino_velocity_y = 0
        is_jumping = False

    if random.randint(0, 100) < 2:
        obstacles.append(pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT - OBSTACLE_HEIGHT - 10, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    for obstacle in obstacles:
        obstacle.x -= obstacle_speed
        if obstacle.x < 0:
            obstacles.remove(obstacle)
            score += 1

    if score > best_score:
        best_score = score

def check_collision():
    dino_rect = pygame.Rect(dino_x, dino_y, DINO_WIDTH, DINO_HEIGHT)
    for obstacle in obstacles:
        if dino_rect.colliderect(obstacle):
            return True
    return False

def can_jump_over_two_obstacles():
    if len(obstacles) < 2:
        return False

    first_obstacle = obstacles[0]
    second_obstacle = obstacles[1]

    distance_between_obstacles = second_obstacle.x - first_obstacle.x
    if distance_between_obstacles > DINO_WIDTH * 2:
        return False

    highest_point = max(first_obstacle.top, second_obstacle.top)
    if highest_point > dino_y + dino_velocity_y:
        return False

    return True

def ai_decision():
    global is_jumping
    for obstacle in obstacles:
        distance_to_obstacle = obstacle.x - dino_x
        if 0 < distance_to_obstacle < 125 and not is_jumping:
            obstacle_top = obstacle.top - DINO_HEIGHT - 10
            jump_threshold = obstacle_top - (dino_y + dino_velocity_y)
            if jump_threshold < 0:
                jump()

    if len(obstacles) > 1 and can_jump_over_two_obstacles() and 0 < distance_to_obstacle < 100 and not is_jumping:
        jump()

def display_score(score, best_score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    best_score_text = font.render(f"Best: {best_score}", True, (255, 255, 255))
    screen.blit(best_score_text, (SCREEN_WIDTH - 150, 10))

def draw_trajectory():
    trajectory_points = []
    for i in range(0, SCREEN_WIDTH, 10):
        x = dino_x + DINO_WIDTH / 2
        y = dino_y

        for obstacle in obstacles:
            if obstacle.x > i and obstacle.x < i + 100:
                obstacle_top = obstacle.top - DINO_HEIGHT - 10
                distance = (obstacle.x - i) / 100
                curve_height = obstacle_top + distance * 100
                y = min(y, curve_height)

        trajectory_points.append((x + (i - dino_x), y))

    pygame.draw.lines(screen, RED, False, trajectory_points, 2)

def draw_anticipation_trajectory():
    anticipation_points = []
    anticipation_y = dino_y
    for i in range(0, SCREEN_WIDTH, 10):
        x = dino_x + DINO_WIDTH / 2
        y = anticipation_y
        for obstacle in obstacles:
            if obstacle.x > i and obstacle.x < i + 100:
                obstacle_top = obstacle.top - DINO_HEIGHT - 10
                distance = (obstacle.x - i) / 100
                curve_height = obstacle_top + distance * 100
                y = max(y, curve_height)

        anticipation_points.append((x + (i - dino_x), y))

    pygame.draw.lines(screen, BLUE, False, anticipation_points, 2)

def game_loop():
    global dino_x, dino_y, obstacles, score, obstacle_speed, best_score

    clock = pygame.time.Clock()
    running = True
    score = 0

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ai_decision()
        update_game()

        draw_dino(dino_x, dino_y)
        draw_obstacles(obstacles)
        display_score(score, best_score)
        draw_trajectory()
        draw_anticipation_trajectory()

        if check_collision():
            score = 0
            obstacles.clear()
            dino_y = SCREEN_HEIGHT - DINO_HEIGHT - 10
            dino_velocity_y = 0

        pygame.display.update()
        clock.tick(30)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and keys[pygame.K_l] :
            pygame.quit()
            running = False
            import launcharles as launcharles


game_loop()
pygame.quit()
