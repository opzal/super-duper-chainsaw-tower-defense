import pygame

class Tower:
    def __init__(self, x, y, damage, range, cost, fire_rate):
        self.x = x
        self.y = y
        self.damage = damage
        self.range = range
        self.cost = cost
        self.fire_rate = fire_rate

    def attack(self, enemy):
        if self.is_in_range(enemy):
            return enemy.take_damage(self.damage)

    def is_in_range(self, enemy):
        dx = self.x - enemy.x
        dy = self.y - enemy.y
        distance = (dx ** 2 + dy ** 2) ** 0.5  
        return distance <= self.range


class BasicTower:
    def __init__(self, x, y, alcance, daño):
        self.x = x
        self.y = y
        self.alcance = alcance
        self.daño = daño

    def draw(self, pantalla):
        """Dibuja la torre básica como un círculo amarillo."""
        pygame.draw.circle(pantalla, (255, 255, 0), (self.x, self.y), 15)
        pygame.draw.circle(pantalla, (255, 255, 0), (self.x, self.y), self.alcance, 1)


class HeavyTower:
    def __init__(self, x, y, alcance, daño):
        self.x = x
        self.y = y
        self.alcance = alcance
        self.daño = daño

    def draw(self, pantalla):
        """Dibuja la torre pesada como un círculo gris."""
        pygame.draw.circle(pantalla, (100, 100, 100), (self.x, self.y), 20)
        pygame.draw.circle(pantalla, (100, 100, 100), (self.x, self.y), self.alcance, 1)


class FastTower:
    def __init__(self, x, y, alcance, daño):
        self.x = x
        self.y = y
        self.alcance = alcance
        self.daño = daño

    def draw(self, pantalla):
        """Dibuja la torre rápida como un círculo naranja."""
        pygame.draw.circle(pantalla, (255, 165, 0), (self.x, self.y), 10)
        pygame.draw.circle(pantalla, (255, 165, 0), (self.x, self.y), self.alcance, 1)