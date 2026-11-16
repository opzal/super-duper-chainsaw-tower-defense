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

    def draw(self, surface):
        pygame.draw.circle(surface, (220, 50, 50), (int(self.x), int(self.y)), 15)

class BasicEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, health=10, speed=100, damage=100)


class FastEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, health=5, speed=80, damage=80)


class HeavyEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, health=20, speed=120, damage=150)