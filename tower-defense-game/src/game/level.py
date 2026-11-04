class Level:
    def __init__(self, number, waves):
        self.number = number
        self.waves = waves
        self.current_wave = 0

    def start_wave(self):
        if self.current_wave < len(self.waves):
            wave = self.waves[self.current_wave]
            # Logic to spawn enemies for the wave
            self.current_wave += 1
            return wave
        return None

    def is_wave_complete(self):
        # Logic to check if the current wave is complete
        pass

    def reset(self):
        self.current_wave = 0
        # Logic to reset level state if needed