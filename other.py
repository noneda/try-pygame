import pygame

# Inicializar Pygame
pygame.init()

# Crear una ventana de 800x600 píxeles
screen = pygame.display.set_mode((800, 600))
# Definir el cuadrado principal
cuadrado_principal = pygame.Rect(200, 200, 400, 200)

# Definir los cuadrados arriba y abajo dentro del cuadrado principal
cuadrado_arriba = pygame.Rect(200, 100, 400, 100)
cuadrado_abajo = pygame.Rect(200, 300, 400, 100)
# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    # Dibujar los cuadrados
    pygame.draw.rect(screen, (40, 42, 54), cuadrado_principal)
    pygame.draw.rect(screen, (218, 247, 166), cuadrado_arriba)
    # pygame.draw.rect(screen, (0, 0, 255), cuadrado_abajo)

    # Actualizar la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
