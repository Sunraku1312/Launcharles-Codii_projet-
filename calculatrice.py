import pygame
import sys

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 550
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Calculatrice")

BACKGROUND_COLOR = (28, 28, 28)
BUTTON_COLOR = (45, 45, 45)
BUTTON_HOVER_COLOR = (70, 70, 70)
TEXT_COLOR = (255, 255, 255)
BORDER_COLOR = (50, 50, 50)

font = pygame.font.SysFont('arial', 30)

current_input = ""
previous_input = ""
operation = ""

def draw_button(text, x, y, width, height, hover=False):
    button_rect = pygame.Rect(x, y, width, height)
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, button_rect)
    pygame.draw.rect(screen, BORDER_COLOR, button_rect, 3)
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    return button_rect

def draw_display():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, SCREEN_WIDTH, 100))
    display_text = font.render(current_input if current_input != "" else "0", True, TEXT_COLOR)
    screen.blit(display_text, (SCREEN_WIDTH // 2 - display_text.get_width() // 2, 50))

def calculate():
    global current_input, previous_input, operation
    if operation == "+":
        current_input = str(float(previous_input) + float(current_input))
    elif operation == "-":
        current_input = str(float(previous_input) - float(current_input))
    elif operation == "*":
        current_input = str(float(previous_input) * float(current_input))
    elif operation == "/":
        if current_input == "0":
            current_input = "Erreur"
        else:
            current_input = str(float(previous_input) / float(current_input))
    previous_input = ""
    operation = ""

def reset():
    global current_input, previous_input, operation
    current_input = ""
    previous_input = ""
    operation = ""

def main():
    global current_input, previous_input, operation

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        draw_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if button_1.collidepoint(mouse_pos):
                    current_input += "1"
                elif button_2.collidepoint(mouse_pos):
                    current_input += "2"
                elif button_3.collidepoint(mouse_pos):
                    current_input += "3"
                elif button_4.collidepoint(mouse_pos):
                    current_input += "4"
                elif button_5.collidepoint(mouse_pos):
                    current_input += "5"
                elif button_6.collidepoint(mouse_pos):
                    current_input += "6"
                elif button_7.collidepoint(mouse_pos):
                    current_input += "7"
                elif button_8.collidepoint(mouse_pos):
                    current_input += "8"
                elif button_9.collidepoint(mouse_pos):
                    current_input += "9"
                elif button_0.collidepoint(mouse_pos):
                    current_input += "0"
                elif button_plus.collidepoint(mouse_pos):
                    previous_input = current_input
                    current_input = ""
                    operation = "+"
                elif button_minus.collidepoint(mouse_pos):
                    previous_input = current_input
                    current_input = ""
                    operation = "-"
                elif button_multiply.collidepoint(mouse_pos):
                    previous_input = current_input
                    current_input = ""
                    operation = "*"
                elif button_divide.collidepoint(mouse_pos):
                    previous_input = current_input
                    current_input = ""
                    operation = "/"
                elif button_equal.collidepoint(mouse_pos):
                    if previous_input != "":
                        calculate()
                elif button_clear.collidepoint(mouse_pos):
                    reset()

        button_1 = draw_button("1", 50, 150, 80, 80)
        button_2 = draw_button("2", 150, 150, 80, 80)
        button_3 = draw_button("3", 250, 150, 80, 80)
        button_4 = draw_button("4", 50, 250, 80, 80)
        button_5 = draw_button("5", 150, 250, 80, 80)
        button_6 = draw_button("6", 250, 250, 80, 80)
        button_7 = draw_button("7", 50, 350, 80, 80)
        button_8 = draw_button("8", 150, 350, 80, 80)
        button_9 = draw_button("9", 250, 350, 80, 80)
        button_0 = draw_button("0", 50, 450, 80, 80)
        button_plus = draw_button("+", 350, 150, 80, 80)
        button_minus = draw_button("-", 350, 250, 80, 80)
        button_multiply = draw_button("*", 350, 350, 80, 80)
        button_divide = draw_button("/", 350, 450, 80, 80)
        button_equal = draw_button("=", 150, 450, 80, 80)
        button_clear = draw_button("C", 250, 450, 80, 80)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()

main()
