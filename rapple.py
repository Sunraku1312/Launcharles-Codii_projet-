import pygame
from random import randint 

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Écran d'Accueil de rapple")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

player = {
    "x": 375,
    "y": 275,
    "size": 50,
    "color": (0,30,250),
    "speed": 0.1,
}

font = pygame.font.SysFont(None, 55)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_button(text, font, color, surface, x, y, width, height):
    pygame.draw.rect(surface, color, (x, y, width, height))
    draw_text(text, font, WHITE, surface, x + width // 2, y + height // 2)

def jeu():
    score = 0
    scoresuiv = score+5
    font = pygame.font.Font(None, 40)

    WIDTH, HEIGHT = 800, 600

    dead = False

    screen = pygame.display.set_mode((WIDTH ,HEIGHT))
    pygame.display.set_caption('rapple v 0.000000003')

    running = True

    apple = {
        "size":30
    }

    xa = randint(0, WIDTH-apple["size"])
    ya = randint(0, HEIGHT-apple["size"])

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            running=False

        if keys[pygame.K_LEFT] or keys[pygame.K_q] or keys[pygame.K_a]:
            player["x"] = player["x"]- player["speed"]
        if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
            player["x"] = player["x"]+ player["speed"]
        if keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.K_w]:
            player["y"] = player["y"]- player["speed"]
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player["y"] = player["y"]+ player["speed"]
        player["x"] = max(0, min(WIDTH - player["size"], player["x"]))
        player["y"] = max(0, min(HEIGHT - player["size"], player["y"]))

        if player["y"] < ya < player["y"]+player["size"] and player["x"] < xa < player["x"]+player["size"] or player["y"] < ya+apple["size"] < player["y"]+player["size"] and player["x"] < xa < player["x"]+player["size"] or player["y"] < ya+apple["size"] < player["y"]+player["size"] and player["x"] < xa+apple["size"] < player["x"]+player["size"] or player["y"] < ya < player["y"]+player["size"] and player["x"] < xa+apple["size"] < player["x"]+player["size"]:
            score+=1
            xa = randint(0, WIDTH-apple["size"])
            ya = randint(0, HEIGHT-apple["size"])

        screen.fill(BLACK)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and keys[pygame.K_l] :
            pygame.quit()
            import launcharles as launcharles

        pygame.draw.rect(screen, player["color"], (player["x"], player["y"], player["size"], player["size"]))
        pygame.draw.rect(screen, (0,255,0), (xa, ya, apple["size"], apple["size"]))
        draw_text("score :", font, RED, screen, screen_width // 1.25, screen_height // 1.0575)
        draw_text(str(score), font, RED, screen, screen_width // 1.13, screen_height // 1.0545)
        pygame.display.flip()

        if score == scoresuiv:
            scoresuiv=score+5
            player["speed"] = player["speed"] * 1.3
    

        if player["x"] == 0 or player["y"] == 0 or player["x"] == WIDTH - player["size"] or player["y"] == HEIGHT - player["size"]:
            dead=True
            while dead==True:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH ,HEIGHT))
                draw_text("Game over !!!", font, RED, screen, screen_width // 2, screen_height // 3)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    running=False
                    dead=False

                if keys[pygame.K_SPACE]:
                    dead=False
                    player["x"]=375
                    player["y"]=275
                    player["speed"]=0.1
                    score=0
                    scoresuiv=score+5

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running=False
                        dead=False
                pygame.display.flip()

def accueil():
    running = True
    while running:
        screen.fill(BLACK)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and keys[pygame.K_l] :
            pygame.quit()
            import launcharles as launcharles

        draw_text("Bienvenue dans rapple !", font, RED, screen, screen_width // 2, screen_height // 3)

        draw_button("Commencer", font, RED, screen, screen_width // 2.05 - 100, screen_height // 2, 220, 50)

        draw_button("Quitter", font, RED, screen, screen_width // 2 - 100, screen_height // 1.5, 200, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 2 < mouse_y < screen_height // 2 + 50:
                    print("Jeu lancé !")
                    running = False
                    jeu()
                elif screen_width // 2 - 100 < mouse_x < screen_width // 2 + 100 and screen_height // 1.5 < mouse_y < screen_height // 1.5 + 50:
                    pygame.quit()

        pygame.display.update()

accueil()

pygame.quit()