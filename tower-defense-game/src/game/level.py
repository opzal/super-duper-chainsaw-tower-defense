import time
import random
import game.enemy as enemy 

class Level:

    def __init__(self, waves):
        self.waves = waves
        self.current_wave = 1
        self.enemy_amount = 6
        self.ENEMIES = []

        self.BASIC_ENEMY_PROB = 20
        self.HEAVY_ENEMY_PROB = 15
        self.FAST_ENEMY_PROB = 5
        
    def start_wave(self):
        if self.current_wave < 7:
            self.wave_filler()
        else:
            self.reset()    
    
    def wave_filler(self):
        for _ in range(self.enemy_amount):
            spawn_chance = random.randint(1, 100)
            if spawn_chance <= self.FAST_ENEMY_PROB:
                self.ENEMIES.append(enemy.FastEnemy())
            elif spawn_chance <= self.HEAVY_ENEMY_PROB:
                self.ENEMIES.append(enemy.HeavyEnemy())
            else:
                self.ENEMIES.append(enemy.BasicEnemy())
            
            espera = random.randint(1, 4)
            time.sleep(espera)
                
    def is_wave_complete(self):
        if len(self.ENEMIES) == 0:
            self.current_wave += 1
            if self.current_wave % 2 == 0:
                self.enemy_amount += 1
            #cambiar probablidades de spawn de enemigos
            self.start_wave()
            return True
        return False
    
    def reset(self):
        self.current_wave = 0

