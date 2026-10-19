# Tower Defense - Clase 2
# El bucle del juego y el camino ya están hechos.
# Tu trabajo: la clase Enemigo (busca los TODO).
import pygame

ANCHO = 800
ALTO = 600
FPS = 60

# El camino que siguen los enemigos: una lista de puntos (x, y).
# Los enemigos van del primero al último, en orden.
CAMINO = [
    (0, 100),
    (600, 100),
    (600, 300),
    (200, 300),
    (200, 500),
    (800, 500),
]


class Enemigo:
    def __init__(self):
        # TODO 1: el enemigo empieza en el primer punto del CAMINO.
        # Pista: ¿cómo sacas el primer elemento de una lista?
        self.x = 0
        self.y = 0 
        self.velocidad = 2

        # TODO 3: ¿cómo sabe el enemigo hacia qué punto va ahora?
        # Piensa qué número tendrías que guardar.

    def mover(self):
        # TODO 2: mueve el enemigo hacia el siguiente punto del camino.
        # Empieza con algo fácil: que vaya hacia la derecha.
        pass

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, (220, 50, 50), (int(self.x), int(self.y)), 15)


def dibujar_camino(pantalla):
    pygame.draw.lines(pantalla, (180, 150, 100), False, CAMINO, 40)


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Tower Defense")
    reloj = pygame.time.Clock()

    enemigo = Enemigo()

    jugando = True
    while jugando:
        # 1. Eventos: ¿qué ha hecho el jugador?
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False

        # 2. Actualizar: mover las cosas
        enemigo.mover()

        # 3. Dibujar: pintar todo de nuevo
        pantalla.fill((40, 120, 40))
        dibujar_camino(pantalla)
        enemigo.dibujar(pantalla)
        pygame.display.flip()

        reloj.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
