import pygame
import pygame_gui

pygame.init()

# Definir algunas constantes
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SQUARE_SIZE = 50

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurar la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Moviendo un cuadrado')

# Crear un gestor de eventos
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# Crear una entrada de texto para ingresar la cantidad de píxeles a mover
text_entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((150, 10), (100, 30)),
    manager=manager
)

# Crear un botón para mover el cuadrado
move_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((150, 50), (100, 50)),
    text='Mover Cuadrado',
    manager=manager
)

# Variables para la posición del cuadrado y la cantidad de píxeles a mover
square_x = (SCREEN_WIDTH - SQUARE_SIZE) // 2
square_y = (SCREEN_HEIGHT - SQUARE_SIZE) // 2
pixels_to_move = 0

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Procesar eventos con el gestor de eventos de Pygame GUI
        manager.process_events(event)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                # Si se presiona el botón, mover el cuadrado según la cantidad ingresada
                if event.ui_element == move_button:
                    try:
                        pixels_to_move = int(text_entry.get_text())
                        square_x += pixels_to_move
                    except ValueError:
                        print("Por favor, ingrese un número válido.")

    screen.fill(WHITE)

    # Dibujar el cuadrado
    pygame.draw.rect(screen, RED, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))

    # Actualizar el gestor de eventos de Pygame GUI
    manager.update(time_delta)

    # Dibujar el gestor de eventos de Pygame GUI
    manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()
