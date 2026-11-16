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
            enemy.take_damage(self.damage)

    def is_in_range(self, enemy):
        dx = self.x - enemy.x
        dy = self.y - enemy.y
        distance = (dx ** 2 + dy ** 2) ** 0.5  
        return distance <= self.range


class BasicTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, damage=10, range=100, cost=100, fire_rate=20)


class FastTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, damage=5, range=80, cost=80, fire_rate=10)


class HeavyTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, damage=20, range=120, cost=150, fire_rate=60)