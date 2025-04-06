import pygame
from random import randint
import numpy as np

pygame.init()

carcolors = (0, 0, 0)
BACKGROUND = (255, 255, 255)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Voiture Trop Cool !!!!!!!")
clock = pygame.time.Clock()

car_img = pygame.image.load("image/limagetropcool.png")
background_img = pygame.image.load("image/laroute.webp")

background_img = pygame.transform.scale(background_img, (WIDTH * 2, HEIGHT * 2))

# Initialisation du meilleur score global
best_score = -1

# Fonction pour afficher le score actuel
def show_score(score):
    font = pygame.font.SysFont("Arial", 30)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

# Fonction pour afficher le meilleur score
def show_best_score(best_score):
    font = pygame.font.SysFont("Arial", 30)
    score_text = font.render(f"MS: {best_score-1}", True, (0, 0, 0))
    screen.blit(score_text, (WIDTH - 200, 10))

# Fonction pour initialiser la Q-table
def initialize_q_table(actions):
    q_table = {}
    for state in range(WIDTH):  # état basé sur la position x
        q_table[state] = {action: 0.0 for action in actions}
    return q_table

# Fonction pour choisir une action en fonction de l'exploration et de l'exploitation
def choose_action(state, q_table, actions, epsilon):
    if np.random.rand() < epsilon:  # Exploration
        return np.random.choice(actions)
    else:  # Exploitation
        return max(actions, key=lambda action: q_table[state][action])

# Fonction pour mettre à jour la Q-table
def update_q_table(q_table, state, action, reward, next_state, actions, alpha, gamma):
    if next_state not in q_table:
        q_table[next_state] = {action: 0.0 for action in actions}  # Assurez-vous que next_state existe dans q_table
    
    best_next_action = max(actions, key=lambda action: q_table[next_state][action])
    q_table[state][action] += alpha * (reward + gamma * q_table[next_state][best_next_action] - q_table[state][action])

# Fonction principale du jeu
# Fonction principale du jeu
def game_loop(q_table, epsilon, alpha, gamma):
    global best_score  # Permet de modifier la variable globale best_score

    score = 0
    ssuivant = score + 5
    tcar = randint(30, 90)
    yc = 2000
    xc = 0.0
    speedcar = 4
    running = True
    x = (WIDTH * 0.45)
    y = (HEIGHT * 0.8)
    x_change = 0

    actions = [-5, 0, 5]  # Actions possibles : aller à gauche (-5), rester en place (0), aller à droite (+5)
    
    state = int(x)  # L'état de l'IA dépend de la position x de la voiture

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Choisir une action en fonction de la Q-table
        action = choose_action(state, q_table, actions, epsilon)

        # Appliquer l'action
        x_change = action
        x += x_change

        # Limiter la position de la voiture pour qu'elle ne sorte pas de l'écran
        x = max(0, min(x, WIDTH - 70))  # x doit être entre 0 et WIDTH - 70

        # Gérer la logique des collisions et du score
        if yc < y < yc + tcar:
            if x < xc < x + 70:
                reward = -1  # Punition
                running = False
                game_loop(q_table, epsilon, alpha, gamma)
            elif x < xc + tcar < x + 70:
                reward = -1  # Punition
                running = False
                game_loop(q_table, epsilon, alpha, gamma)
            elif x < xc + tcar / 2 < x + 70:
                reward = -1  # Punition
                running = False
                game_loop(q_table, epsilon, alpha, gamma)
        else:
            reward = 1  # Récompense si la voiture n'a pas perdu

        # Si le score est atteint, on augmente la vitesse
        if score == ssuivant:
            speedcar += 0.05

        screen.blit(background_img, (-200, 0))

        # Affichage du score actuel
        show_score(score - 1)

        # Affichage du meilleur score
        show_best_score(best_score)

        pygame.draw.rect(screen, carcolors, (xc, yc, tcar, tcar))
        screen.blit(car_img, (x, y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and keys[pygame.K_l]:
            pygame.quit()
            import launcharles as launcharles

        if yc < HEIGHT:
            yc += speedcar
        else:
            xc = x
            tcar = randint(30, 90)
            yc = 0 - tcar
            score += 1

        # Mise à jour de la Q-table
        next_state = int(x)
        update_q_table(q_table, state, action, reward, next_state, actions, alpha, gamma)

        # Mise à jour du meilleur score si nécessaire
        if score > best_score:
            best_score = score

        state = next_state

        pygame.display.update()
        clock.tick(60)


# Paramètres d'entraînement de l'IA
actions = [-5, 0, 5]  # Déplacement à gauche, au centre, à droite
epsilon = 0.1  # Taux d'exploration (probabilité d'explorer de nouvelles actions)
alpha = 0.1    # Taux d'apprentissage
gamma = 0.9    # Facteur de réduction (importance des récompenses futures)

# Initialisation de la Q-table
q_table = initialize_q_table(actions)

# Lancer le jeu et l'entraînement de l'IA
game_loop(q_table, epsilon, alpha, gamma)

pygame.quit()
