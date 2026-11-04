# Tower Defense Game

## Overview
This is a tower defense game built using Pygame. Players will strategically place towers to defend against waves of enemies. The game features various tower types, enemy behaviors, and level progression.

## Project Structure
```
tower-defense-game
├── assets
│   ├── fonts
│   ├── sounds
│   └── sprites
├── src
│   ├── main.py
│   ├── game
│   │   ├── __init__.py
│   │   ├── enemy.py
│   │   ├── tower.py
│   │   ├── player.py
│   │   └── level.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── settings.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd tower-defense-game
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Execution
To run the game, execute the following command:
```
python src/main.py
```

## Assets
- Fonts: Place .ttf font files in the `assets/fonts` directory.
- Sounds: Add sound effects and music files to the `assets/sounds` directory.
- Sprites: Include sprite images for towers, enemies, and UI elements in the `assets/sprites` directory.

## Contribution
Feel free to fork the repository and submit pull requests for any improvements or features.