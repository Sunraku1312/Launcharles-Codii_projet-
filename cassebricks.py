import pygame
import random

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600
screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Casse-briques Infini")

BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
VERT = (0, 255, 0)
NOIR = (0, 0, 0)

raquette_largeur = 100
raquette_hauteur = 15
raquette_vitesse = 10

balle_radius = 10
balle_vitesse_x = 5
balle_vitesse_y = -5

raquette = pygame.Rect(largeur_fenetre // 2 - raquette_largeur // 2, hauteur_fenetre - raquette_hauteur - 10, raquette_largeur, raquette_hauteur)

briques = []
nb_briques_lignes = 5
nb_briques_colonnes = 8
brique_largeur = largeur_fenetre // nb_briques_colonnes - 10
brique_hauteur = 30

def create_briques():
    briques.clear()
    for i in range(nb_briques_lignes):
        for j in range(nb_briques_colonnes):
            brique = pygame.Rect(j * (brique_largeur + 10) + 5, i * (brique_hauteur + 5) + 5, brique_largeur, brique_hauteur)
            briques.append(brique)

def draw_briques():
    for brique in briques:
        pygame.draw.rect(screen, BLEU, brique)

def game():
    global balle_vitesse_x, balle_vitesse_y
    balle_x = largeur_fenetre // 2
    balle_y = hauteur_fenetre - 50
    balle_dx = balle_vitesse_x
    balle_dy = balle_vitesse_y

    raquette_dx = 0
    running = True
    score = 0
    clock = pygame.time.Clock()

    create_briques()

    while running:
        screen.fill(NOIR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and raquette.left > 0:
            raquette_dx = -raquette_vitesse
        elif keys[pygame.K_RIGHT] and raquette.right < largeur_fenetre:
            raquette_dx = raquette_vitesse
        else:
            raquette_dx = 0

        raquette.x += raquette_dx

        balle_x += balle_dx
        balle_y += balle_dy

        if balle_x - balle_radius <= 0 or balle_x + balle_radius >= largeur_fenetre:
            balle_dx = -balle_dx

        if balle_y - balle_radius <= 0:
            balle_dy = -balle_dy

        if raquette.colliderect(pygame.Rect(balle_x - balle_radius, balle_y - balle_radius, balle_radius * 2, balle_radius * 2)):
            balle_dy = -balle_dy

        for brique in briques[:]:
            if brique.colliderect(pygame.Rect(balle_x - balle_radius, balle_y - balle_radius, balle_radius * 2, balle_radius * 2)):
                balle_dy = -balle_dy
                briques.remove(brique)
                score += 10
                if len(briques) == 0:
                    create_briques()
                    balle_vitesse_x += 1
                    balle_vitesse_y -= 1
                    balle_dx = balle_vitesse_x
                    balle_dy = balle_vitesse_y

        if balle_y > hauteur_fenetre:
            running = False
            game()

        pygame.draw.rect(screen, VERT, raquette)
        pygame.draw.circle(screen, ROUGE, (balle_x, balle_y), balle_radius)

        draw_briques()

        font = pygame.font.SysFont('Arial', 24)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        clock.tick(60)

game()

pygame.quit()
