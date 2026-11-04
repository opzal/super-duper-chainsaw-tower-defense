class Player:
    def __init__(self, health=100, resources=100):
        self.health = health
        self.resources = resources

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def gain_resources(self, amount):
        self.resources += amount

    def spend_resources(self, amount):
        if amount <= self.resources:
            self.resources -= amount
            return True
        return False

    def is_alive(self):
        return self.health > 0