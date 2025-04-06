import pygame
import sys

def projet_final():
    print("Lancement du Projet Final...")
    pygame.quit()

def rapple():
    print("Lancement de Rapple...")
    pygame.quit()
    import rapple

def flappy_bird():
    print("Lancement de Flappy Bird...")
    pygame.quit()
    import flappybird

def racecar():
    print("Lancement de Racecar...")
    pygame.quit()
    import racecar

def calculatrice():
    print("Lancement de Minecraft 3D...")
    pygame.quit()
    import minecraft3d.main

def boby():
    print("Lancement de Dino IA...")
    pygame.quit()
    import dinoIA

def rpg_text():
    print("Lancement de Minecrafty...")
    pygame.quit()
    import minecrafty

def jeu1():
    print("Lancement de Clikeurs...")
    pygame.quit()
    import clickeur as clickeur

def jeu2():
    print("Lancement de Casse-Bricks...")
    pygame.quit()
    import cassebricks

def jeu3():
    print("Lancement de Racourci...")
    pygame.quit()
    import racourci

def jeu4():
    print("Lancement de Calculatrice...")
    pygame.quit()
    import calculatrice

def ia():
    pygame.quit()
    import sacos.acceuille as acceuille

pygame.init()

largeur = 500
hauteur = 650
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Launcharles")

blanc = (255, 255, 255)
bleu = (0, 0, 255)
vert = (0, 255, 0)
gris_clair = (200, 200, 200)
rouge = (255, 0, 0)
marron = (139, 69, 19)

largeur_bouton = 180
hauteur_bouton = 50
marge_bouton = 10

textes_boutons = [
    "Projet Final", "Rapple", "Flappy Bird", "Racecar", "Minecraft 3D",
    "Dino IA", "Minecrafty", "Clikeurs", "Casse-Bricks", "Racourci", "Calculatrice", "Sacos"
]

font = pygame.font.SysFont('Arial', 20)

def dessiner_bouton(x, y, texte, couleur, couleur_texte=blanc):
    pygame.draw.rect(ecran, couleur, (x, y, largeur_bouton, hauteur_bouton), border_radius=15)
    label = font.render(texte, True, couleur_texte)
    ecran.blit(label, (x + (largeur_bouton - label.get_width()) // 2, y + (hauteur_bouton - label.get_height()) // 2))

def clic_sur_bouton(x, y, bouton_rect):
    return bouton_rect.collidepoint(x, y)

def dessiner_fond():
    for i in range(hauteur):
        r = min(i // 4, 150)
        g = min(i // 4, 50)
        b = max(100 - i // 4, 0)
        pygame.draw.line(ecran, (r, g, b), (0, i), (largeur, i))

def afficher_interface():
    run = True
    while run:
        ecran.fill(gris_clair)
        dessiner_fond()

        for i in range(len(textes_boutons)):
            x = (largeur - largeur_bouton) // 2
            y = 50 + (hauteur_bouton + marge_bouton) * i
            bouton_rect = pygame.Rect(x, y, largeur_bouton, hauteur_bouton)
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if bouton_rect.collidepoint(mouse_x, mouse_y):
                dessiner_bouton(x, y, textes_boutons[i], bleu)
            else:
                dessiner_bouton(x, y, textes_boutons[i], vert)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i in range(len(textes_boutons)):
                        x = (largeur - largeur_bouton) // 2
                        y = 50 + (hauteur_bouton + marge_bouton) * i
                        bouton_rect = pygame.Rect(x, y, largeur_bouton, hauteur_bouton)
                        if clic_sur_bouton(mouse_x, mouse_y, bouton_rect):
                            jeux[i]()
                            run = False
        
        pygame.display.update()

    pygame.quit()

jeux = {
    0: projet_final,
    1: rapple,
    2: flappy_bird,
    3: racecar,
    4: calculatrice,
    5: boby,
    6: rpg_text,
    7: jeu1,
    8: jeu2,
    9: jeu3,
    10: jeu4,
    11: ia
}

afficher_interface()
