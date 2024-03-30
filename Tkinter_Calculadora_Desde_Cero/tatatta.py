import pygame
import pygame_gui
import tkinter as tk
from tkinter import messagebox

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)

class Carro:
    def __init__(self, x, y, ancho, alto, color=ROJO):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = color

    def draw(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)

def main():
    pygame.init()

    # Configuración de la pantalla
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Carro con Botón")

    # Configuración del carro
    pos_car = [100,300]
    carro = Carro(pos_car[0], pos_car[1], 60, 40)

    clock = pygame.time.Clock()

    # Crear ventana Tkinter
    tk_root = tk.Tk()
    tk_root.withdraw()  # Ocultar la ventana de Tkinter

    # Función para iniciar Pygame
    def iniciar_pygame():
        pos_car[0] += int(entry_tkinter.get())
        print(pos_car[0])

    # Configurar Pygame GUI
    manager = pygame_gui.UIManager((800, 600))
    boton_tkinter = tk.Button(tk_root, text="Iniciar Pygame", command=iniciar_pygame)
    boton_tkinter.pack()

    entry_tkinter = tk.Entry(tk_root, text="Iniciar Pygame")
    entry_tkinter.pack()

    # Integrar el botón de Tkinter en la ventana de Pygame
    botones = pygame_gui.elements.UIButton(pygame.Rect(10, 10, 150, 50), "Botón Tkinter", manager)
    Entry = pygame_gui.elements.UITextEntryBox(pygame.Rect(200, 10, 150, 50), "Entry Tkinter", manager)
    boton_tkinter.tkinter_widget = botones
    boton_tkinter.toplevel = tk_root

    entry_tkinter.tkinter_widget = Entry
    entry_tkinter.toplevel = tk_root

    # Bucle principal del juego
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.process_events(event)

        # Lógica del juego

        # Dibujo en la pantalla
        pantalla.fill(BLANCO)
        carro.draw(pantalla)

        # Actualizar GUI de Pygame
        manager.update(time_delta)
        manager.draw_ui(pantalla)

        pygame.display.flip()

    pygame.quit()
    #sys.exit()

if __name__ == "__main__":
    main()
