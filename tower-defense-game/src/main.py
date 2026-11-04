import pygame
from game.enemy import Enemy
from game.tower import Tower
from game.player import Player
from game.level import Level
from settings import FPS, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tower Defense Game")
    clock = pygame.time.Clock()

    player = Player()
    level = Level()
    enemies = [Enemy() for _ in range(level.current_wave)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state
        for enemy in enemies:
            enemy.move()
        
        # Draw everything
        screen.fill(BACKGROUND_COLOR)
        level.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()