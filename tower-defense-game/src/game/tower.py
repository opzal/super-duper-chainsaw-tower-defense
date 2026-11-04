class Tower:
    def __init__(self, x, y, damage, range, cost):
        self.x = x
        self.y = y
        self.damage = damage
        self.range = range
        self.cost = cost

    def attack(self, enemy):
        if self.is_in_range(enemy):
            enemy.take_damage(self.damage)

    def is_in_range(self, enemy):
        distance = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
        return distance <= self.range


class BasicTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, damage=10, range=100, cost=100)


class FastTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, damage=5, range=80, cost=80)


class HeavyTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, damage=20, range=120, cost=150)