# Pokémon Lite Project

## Overview
Pokémon Lite is a simplified, lightweight implementation of the Pokémon game mechanics. The project features core functionalities such as Pokémon data, battles, and a modular structure, offering an easily extensible and interactive experience for developers and enthusiasts.

## Features
- **Comprehensive Pokémon Database:** Includes statistics, types, and base experience for various Pokémon.
- **Battle System:** Implements battle mechanics between Pokémon, calculating outcomes based on statistics and types.
- **Modular Design:** Separate modules for Pokémon data, battle logic, display, and factory pattern for Pokémon creation.

## File Structure
The project is organized into the following modules:

### 1. `api_manager.py`
Handles interactions between different modules, serving as the central communication hub.

### 2. `battle.py`
Implements battle mechanics. This includes:
- Turn-based system.
- Calculations for damage based on Pokémon statistics and types.
- Outcome determination.

### 3. `game.py`
Acts as the entry point for the project, orchestrating gameplay and interactions between modules.

### 4. `pokemon.json`
Contains detailed Pokémon data, including:
- Base statistics: Health Points, Attack, Defense, Special Attack, Special Defense, and Speed.
- Types: Single or dual types for each Pokémon.
- Base experience values for leveling.

### 5. `pokemon.py`
Defines the Pokémon class with attributes and methods to manage Pokémon objects.

### 6. `pokemon_display.py`
Handles the presentation layer, providing a user-friendly way to view Pokémon statistics and battle results.

### 7. `pokemon_factory.py`
Implements the factory pattern to create Pokémon instances dynamically from the JSON database.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/pokemon-lite.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pokemon-lite
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the game:
   ```bash
   python game.py
   ```
2. Follow the prompts to:
   - Select Pokémon.
   - Initiate battles.
   - View results and statistics.

## Pokémon Data
Pokémon data is stored in `pokemon.json`, structured as:
```json
{
    "name": "bulbasaur",
    "base_statistics": {
        "health_points": 45,
        "attack": 49,
        "defense": 49,
        "special_attack": 65,
        "special_defense": 65,
        "speed": 45
    },
    "base_experience": 64,
    "types": ["grass", "poison"]
}
```
- **Attributes:** Name, base stats, types, and base experience.
- **Extensibility:** Add more Pokémon by appending to the JSON file in the same format.

## Battle System
### Mechanics
- **Damage Calculation:**
  ```
  Damage = (Attack / Defense) * Modifier
  ```
  where `Modifier` depends on type matchups (e.g., super effective, not effective).
- **Turn Order:** Determined by the Speed stat.

### Example
Bulbasaur vs. Charmander:
- Bulbasaur (Grass/Poison) has base stats `HP=45`, `Attack=49`, `Defense=49`.
- Charmander (Fire) has base stats `HP=39`, `Attack=52`, `Defense=43`.
- Grass is weak to Fire, so Charmander deals increased damage.

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments
- Pokémon data inspired by the Pokémon franchise.
- Developers and contributors who helped bring this project to life.

