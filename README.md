# Dungeon Crawler Game with Dynamic Soundtrack Generation

## Table of Contents

1. [Project Overview](#project-overview)
2. [Implemented Methods](#implemented-methods)
    - [Horizontal Re-sequencing](#horizontal-re-sequencing)
    - [Markov Chains](#markov-chains)
    - [Linear Soundtrack](#linear-soundtrack)
3. [Game Description](#game-description)
    - [Technologies](#technologies)
    - [Gameplay](#gameplay)
    - [Controls](#controls)
4. [Installation Instructions](#installation-instructions)


## Project Overview

This project focuses on dynamic soundtrack generation for a dungeon crawler game, where the music adapts to the state of the game. It implements two dynamic methods for soundtrack generation (Horizontal Re-sequencing and Markov Chains) as well as a linear soundtrack. The project is built using Python 3.12 and the PyGame library.

## Implemented Methods

### Horizontal Re-sequencing

Horizontal Re-sequencing is an adaptive method for soundtrack generation that alters the music based on the current game state. The game defines three states:

- **Exploration**
- **Approaching an Enemy**
- **Combat**

Each state is associated with a specific music track designed to enhance the player's experience in that situation. The music transitions between states using crossfading, ensuring that the soundtrack adapts dynamically.

### Markov Chains

Markov Chains were used to generate a generative soundtrack by modeling musical progressions. In this implementation, musical states are represented as chords, and transitions between these states are probabilistic.

The chords were generated using the music21 Python library, and the music was played using the Pygame sound module. The transitions between musical chords were defined in transition tables based on the player's proximity to enemies.

### Linear Soundtrack

In addition to dynamic methods, a linear soundtrack is played at the start of each level. This music is looped throughout the level.

## Game Description

### Technologies

The game was implemented using Python 3.12 and the PyGame library.

### Gameplay

The game is a Dungeon Crawler, where the player explores a maze-like environment, fights monsters, and finds keys to progress to the next level. The game features 4 levels, each with different difficulty:

- **Introductory levels (2 levels): Smaller and easier.**
- **Challenging levels (2 levels): Larger and tougher, with more enemies**

Enemies:

- **Base enemies: Simple AI that tracks the player.**
- **Ranged enemies: Attack from a distance.**
- **Boss enemy: A combination of the two, harder to defeat.**

The player can attack enemies using a sword or magic spells. Health and mana potions are scattered throughout the dungeon to help the player. The game uses dynamic state transitions based on the player's proximity to enemies and changes in game state (combat, exploration).

### Controls

- **W, A, S, D** – Move the player character  
- **Left Mouse Button (LMB)** – Attack in the direction of the cursor  
- **Spacebar** – Draw the sword

## Installation Instructions

To run the game locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/bartekuznik/Dungeon_crawler.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the game:

```
python main.py
```

Alternatively, you can use the pre-compiled executable (Windows .exe file in dist folder) to run the game without needing to install Python.