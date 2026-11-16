import pygame

class Enemy:
    def __init__(x, y, self, health, speed, damage):
        self.health = health
        self.speed = speed
        self.damage = damage
        self.x = x 
        self.y = y

    def move(self, target_point):
        destino_x, destino_y = target_point
        dx = destino_x - self.x
        dy = destino_y - self.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        if distancia <= self.speed:
            # Llegamos al punto: nos colocamos encima y pasamos al siguiente
            self.x, self.y = destino_x, destino_y
        else:
            # Avanzamos 'velocidad' píxeles en la dirección del destino
            self.x += dx / distancia * self.speed
            self.y += dy / distancia * self.speed

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            return True
        else: 
            return False

class BasicEnemy:
    def __init__(self, x, y, vida, velocidad):
        self.x = x
        self.y = y
        self.vida = vida
        self.velocidad = velocidad

    def draw(self, pantalla):
        """Dibuja al enemigo básico como un círculo rojo."""
        pygame.draw.circle(pantalla, (255, 0, 0), (int(self.x), int(self.y)), 10)


class HeavyEnemy:
    def __init__(self, x, y, vida, velocidad):
        self.x = x
        self.y = y
        self.vida = vida
        self.velocidad = velocidad

    def draw(self, pantalla):
        """Dibuja al enemigo pesado como un círculo azul."""
        pygame.draw.circle(pantalla, (0, 0, 255), (int(self.x), int(self.y)), 15)


class FastEnemy:
    def __init__(self, x, y, vida, velocidad):
        self.x = x
        self.y = y
        self.vida = vida
        self.velocidad = velocidad

    def draw(self, pantalla):
        """Dibuja al enemigo rápido como un círculo verde."""
        pygame.draw.circle(pantalla, (0, 255, 0), (int(self.x), int(self.y)), 8)