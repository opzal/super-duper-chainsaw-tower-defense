class Enemy:
    def __init__(self, health, speed, damage):
        self.health = health
        self.speed = speed
        self.damage = damage
        self.position = (0, 0)

    def move(self):
        # Logic to move the enemy towards the target
        pass

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        # Logic to handle enemy destruction
        pass

    def draw(self, surface):
        # Logic to draw the enemy on the given surface
        pass