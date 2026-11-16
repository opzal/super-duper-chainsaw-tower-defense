import pygame
from game.enemy import Enemy
from game.tower import Tower
from game.player import Player
from game.level import Level
from settings import FPS, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
# Tower Defense - Clase 2
# El bucle del juego y el camino ya están hechos.
# Tu trabajo: la clase Enemigo (busca los TODO).
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
        self.x, self.y = CAMINO[0]
        self.velocidad = 2
        self.siguiente = 1


    def mover(self):
        destino_x, destino_y = CAMINO[self.siguiente]
        dx = destino_x - self.x
        dy = destino_y - self.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        if distancia <= self.velocidad:
            # Llegamos al punto: nos colocamos encima y pasamos al siguiente
            self.x, self.y = destino_x, destino_y
            self.siguiente += 1
            if self.siguiente >= len(CAMINO):
                self.ha_llegado = True
        else:
            # Avanzamos 'velocidad' píxeles en la dirección del destino
            self.x += dx / distancia * self.velocidad
            self.y += dy / distancia * self.velocidad

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, (220, 50, 50), (int(self.x), int(self.y)), 15)


def dibujar_camino(pantalla):
    pygame.draw.lines(pantalla, (180, 150, 100), False, CAMINO, 40)


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
