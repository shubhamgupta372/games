# Snake Game 🐍

An interactive CLI-based Snake game built in Python. Eat food to grow and score points while avoiding walls and colliding with yourself!

## Features

- **Interactive Gameplay**: Real-time snake movement with keyboard controls
- **Food System**: Eat food to grow longer and gain points
- **Score Tracking**: Keep track of your current score
- **Collision Detection**: Game ends if you hit walls or yourself
- **Terminal-based Graphics**: Works in any terminal with Python

## Requirements

- Python 3.6+
- Unix-like terminal with `curses` support (Linux, macOS)
- For Windows: Windows Terminal or WSL recommended

## Installation

1. Ensure you have Python 3.6+ installed:
   ```bash
   python3 --version
   ```

2. No additional packages required (uses Python standard library `curses` module)

## How to Run

### macOS / Linux

```bash
python3 snake.py
```

### Windows (with WSL or Windows Terminal)

```bash
python3 snake.py
```

## Controls

| Key | Action |
|-----|--------|
| **W** or **↑** | Move Up |
| **S** or **↓** | Move Down |
| **A** or **←** | Move Left |
| **D** or **→** | Move Right |
| **Q** | Quit Game |

## Gameplay Rules

1. **Objective**: Eat as much food (*) as possible to grow and increase your score
2. **Movement**: The snake continuously moves in the direction you specify
3. **Growth**: Each food eaten adds one segment to the snake and gives 10 points
4. **Collision**: 
   - Hitting walls ends the game
   - Hitting yourself ends the game
5. **Winning**: Try to eat as many food items as possible!

## Game Elements

- **@** - Your snake's head
- **o** - Snake's body
- **\*** - Food
- **#** - Walls/Boundaries

## Tips & Strategies

1. Plan your moves ahead to avoid getting trapped
2. Try to create patterns that allow efficient food collection
3. Don't corner yourself - maintain escape routes
4. Take your time - the game doesn't have a time limit

## Example Gameplay

```
    ############
    #  *       #
    #o@o       #
    #          #
    ##########
    Score: 20
```

## Troubleshooting

### "ImportError: No module named 'curses'" (Windows)
- Use Windows Subsystem for Linux (WSL) or Windows Terminal
- Or play the Chess game instead!

### Terminal looks corrupted
- Try resizing your terminal window
- Ensure your terminal is at least 70x30 characters

### Game won't start
- Make sure you're using `python3` (not `python` which might be Python 2)
- Ensure you're running from the correct directory

## Future Enhancements

- [ ] Obstacles on the map
- [ ] Multiple difficulty levels
- [ ] Speed increases as you score more
- [ ] High score persistence
- [ ] Leaderboard system

## License

Free to use and modify!

## Author

Created as part of interactive CLI games collection
