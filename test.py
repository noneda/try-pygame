import random, pygame

# Inicialización de Pygame
pygame.init()

tamaño_celdas = 50

# Definición de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Crear laberinto
laberinto = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 3],
    [1, 0, 4, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 4, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 2, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

# Creación de la pantalla y dibujar el laberinto
screen = pygame.display.set_mode(
    (len(laberinto[1]) * tamaño_celdas, len(laberinto) * tamaño_celdas)
)
pygame.display.set_caption("Laberinto")


# Dibujar el laberinto en pantalla
def draw_laberinto():
    for row in range(len(laberinto)):
        for col in range(len(laberinto[1])):
            if laberinto[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (
                        col * tamaño_celdas,
                        row * tamaño_celdas,
                        tamaño_celdas,
                        tamaño_celdas,
                    ),
                )
            elif laberinto[row][col] == 2:
                pygame.draw.rect(
                    screen,
                    GREEN,
                    (
                        col * tamaño_celdas,
                        row * tamaño_celdas,
                        tamaño_celdas,
                        tamaño_celdas,
                    ),
                )
            elif laberinto[row][col] == 3:
                pygame.draw.rect(
                    screen,
                    RED,
                    (
                        col * tamaño_celdas,
                        row * tamaño_celdas,
                        tamaño_celdas,
                        tamaño_celdas,
                    ),
                )
            elif laberinto[row][col] == 4:
                pygame.draw.rect(
                    screen,
                    BLUE,
                    (
                        col * tamaño_celdas,
                        row * tamaño_celdas,
                        tamaño_celdas,
                        tamaño_celdas,
                    ),
                )


# Función para mover a los enemigos
def move_enemies():
    global laberinto
    enemigos = []
    for row in range(len(laberinto)):
        for col in range(len(laberinto[0])):
            if laberinto[row][col] == 4:
                enemigos.append((row, col))

    for enemigo in enemigos:
        y_enemy, x_enemy = enemigo

        valid_moves = []

        # Revisar movimientos válidos para el enemigo
        if laberinto[y_enemy - 1][x_enemy] == 0:
            valid_moves.append("up")
        if laberinto[y_enemy + 1][x_enemy] == 0:
            valid_moves.append("down")
        if laberinto[y_enemy][x_enemy - 1] == 0:
            valid_moves.append("left")
        if laberinto[y_enemy][x_enemy + 1] == 0:
            valid_moves.append("right")

        # Revisar si puede matar al jugador
        if laberinto[y_enemy - 1][x_enemy] == 2:
            activo = False
        if laberinto[y_enemy + 1][x_enemy] == 2:
            activo = False
        if laberinto[y_enemy][x_enemy - 1] == 2:
            activo = False
        if laberinto[y_enemy][x_enemy + 1] == 2:
            activo = False

        # Elegir un movimiento aleatorio válido para el enemigo
        if valid_moves:
            new_direction = random.choice(valid_moves)

            # Actualizar la posición del enemigo en el laberinto
            laberinto[y_enemy][x_enemy] = 0
            if new_direction == "up":
                laberinto[y_enemy - 1][x_enemy] = 4
            elif new_direction == "down":
                laberinto[y_enemy + 1][x_enemy] = 4
            elif new_direction == "left":
                laberinto[y_enemy][x_enemy - 1] = 4
            elif new_direction == "right":
                laberinto[y_enemy][x_enemy + 1] = 4

            directions = ["up", "down", "right", "left"]


# Función para mover al jugador
def move_player(key):
    global activo
    x, y = get_player_position()
    if key == pygame.K_w:
        if laberinto[x - 1][y] == 0:
            laberinto[x][y] = 0
            laberinto[x - 1][y] = 2
            move_enemies()
        elif laberinto[x - 1][y] == 3:
            show_victory_screen()
        elif laberinto[x - 1][y] == 4:
            activo = False

    elif key == pygame.K_s:
        if laberinto[x + 1][y] == 0:
            laberinto[x][y] = 0
            laberinto[x + 1][y] = 2
            move_enemies()
        elif laberinto[x + 1][y] == 3:
            show_victory_screen()
        elif laberinto[x + 1][y] == 4:
            activo = False

    elif key == pygame.K_a:
        if laberinto[x][y - 1] == 0:
            laberinto[x][y] = 0
            laberinto[x][y - 1] = 2
            move_enemies()
        elif laberinto[x][y - 1] == 3:
            show_victory_screen()
        elif laberinto[x][y - 1] == 4:
            activo = False

    elif key == pygame.K_d:
        if laberinto[x][y + 1] == 0:
            laberinto[x][y] = 0
            laberinto[x][y + 1] = 2
            move_enemies()
        elif laberinto[x][y + 1] == 3:
            show_victory_screen()
        elif laberinto[x][y + 1] == 4:
            activo = False


# Obtener la pasicion del jugador
def get_player_position():
    for row in range(len(laberinto)):
        for col in range(len(laberinto[1])):
            if laberinto[row][col] == 2:
                return row, col


# Mostrar cuando se gana
def show_victory_screen():
    global running
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render("¡Has ganado!", True, BLACK)
    text_rect = text.get_rect(
        center=(
            (len(laberinto[1]) * tamaño_celdas) // 2,
            (len(laberinto) * tamaño_celdas) // 2,
        )
    )
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # Esperar 2 segundos antes de salir
    running = False


# El bucle principal
def main():
    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                move_player(event.key)

        screen.fill(WHITE)
        draw_laberinto()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
