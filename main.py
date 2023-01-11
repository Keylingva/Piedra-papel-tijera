import pygame
import random

# Inicializar Pygame
pygame.init()

# Establecer las dimensiones de la pantalla
size = (700, 500)
screen = pygame.display.set_mode(size)

# Establecer el título de la ventana
pygame.display.set_caption("Piedra, Papel o Tijera")

# Variables para guardar las imágenes
rock_image = pygame.image.load("piedra.png")
paper_image = pygame.image.load("papel.png")
scissors_image = pygame.image.load("tijera.png")

# Variables para guardar la elección del jugador y la del computador
player_choice = ""
computer_choice = ""

# Bucle principal
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.unicode == 'p':
                player_choice = "piedra"
            elif event.unicode == 'a':
                player_choice = "papel"
            elif event.unicode == 't':
                player_choice = "tijera"
            elif event.unicode == 'c':
                done = True

    # Elección aleatoria de la computadora
    computer_choice = random.choice(["piedra", "papel", "tijera"])

    # Determinar el ganador
    if player_choice != "":
        if player_choice == computer_choice:
            winner = "tie"
        elif (player_choice == "piedra" and computer_choice == "tijera") or (player_choice == "papel" and computer_choice == "piedra") or (player_choice == "tijera" and computer_choice == "papel"):
            winner = "player"
        else:
            winner = "computer"

    # Dibujar el fondo de la pantalla
    screen.fill((0, 0, 0))

    # Dibujar la elección del jugador
    if player_choice != "":
        if player_choice == "piedra":
            screen.blit(rock_image, (200, 200))
        elif player_choice == "papel":
            screen.blit(paper_image, (200, 200))
        elif player_choice == "tijera":
            screen.blit(scissors_image, (200, 200))

    # Dibujar la elección de la computadora
    if computer_choice != "":
        if computer_choice == "        piedra":
            screen.blit(rock_image, (450, 200))
        elif computer_choice == "papel":
            screen.blit(paper_image, (450, 200))
        elif computer_choice == "tijera":
            screen.blit(scissors_image, (450, 200))

    # Mostrar el resultado
    if player_choice != "" and computer_choice != "":
        if winner == "tie":
            result = "Empate!"
        elif winner == "player":
            result = "Ganaste!"
        else:
            result = "Perdiste!"
        font = pygame.font.Font(None, 30)
        text = font.render(result, True, (255, 255, 255))
        screen.blit(text, (320, 50))

        # Preguntar si el usuario desea continuar
        font = pygame.font.Font(None, 24)
        text = font.render("Presiona Enter para continuar, otra tecla para salir", True, (255, 255, 255))
        screen.blit(text, (200, 450))
        pygame.display.update()
        player_choice = ""
        computer_choice = ""
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key != pygame.K_RETURN:
                        done = True

    # Actualizar la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()

