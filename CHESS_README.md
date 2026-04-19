# Chess Game ♔

An interactive CLI-based Chess game where you play as White against a CPU opponent (Black). Test your chess skills in a terminal-based interface!

## Features

- **Single Player vs CPU**: Play against an AI opponent
- **Full Chess Rules**: Standard chess piece movements and captures
- **Board Display**: Clear terminal-based board visualization
- **Move Validation**: Automatic validation of legal moves
- **CPU AI**: Simple AI that prioritizes capturing pieces
- **Algebraic Notation**: Move using standard chess notation (e2e4)

## Requirements

- Python 3.6+
- Any terminal with Python support

## Installation

1. Ensure you have Python 3.6+ installed:
   ```bash
   python3 --version
   ```

2. No additional packages required (uses Python standard library only)

## How to Run

### macOS / Linux / Windows

```bash
python3 chess.py
```

## How to Play

### Board Layout

The board is displayed with:
- **Rows**: 8 (top) to 1 (bottom)
- **Columns**: a (left) to h (right)
- **Uppercase letters**: Your pieces (White)
- **Lowercase letters**: CPU pieces (Black)

```
    a b c d e f g h
  ┌─────────────────┐
8 │ r n b q k b n r │ 8
7 │ p p p p p p p p │ 7
6 │ . . . . . . . . │ 6
5 │ . . . . . . . . │ 5
4 │ . . . . . . . . │ 4
3 │ . . . . . . . . │ 3
2 │ P P P P P P P P │ 2
1 │ R N B Q K B N R │ 1
  └─────────────────┘
    a b c d e f g h
```

### Piece Symbols

| Symbol | Piece | Movement |
|--------|-------|----------|
| **K/k** | King | One square in any direction |
| **Q/q** | Queen | Any number of squares horizontally, vertically, or diagonally |
| **R/r** | Rook | Any number of squares horizontally or vertically |
| **B/b** | Bishop | Any number of squares diagonally |
| **N/n** | Knight | L-shaped: 2 squares in one direction, 1 square perpendicular |
| **P/p** | Pawn | Forward 1 square (2 on first move); capture diagonally forward |

### Move Input

Enter moves using **algebraic notation**: `[from_square][to_square]`

**Examples:**
- `e2e4` - Move pawn from e2 to e4 (classic opening move!)
- `g1f3` - Move knight from g1 to f3
- `e7e5` - Move pawn from e7 to e5

### In-Game Commands

| Command | Action |
|---------|--------|
| Move notation (e.g., `e2e4`) | Make a move |
| **h** | Display help/instructions |
| **q** | Quit the game |

## Gameplay Tips

### Opening Moves

Classic opening moves to try:

```
White: e2e4 (Pawn to e4)
Black: CPU responds...
White: g1f3 (Knight to f3)
```

### Strategy

1. **Control the Center**: Try to place pieces in the center squares (d4, e4, d5, e5)
2. **Develop Your Pieces**: Move knights and bishops to useful squares early
3. **Protect Your King**: Castle early for king safety (when you're ready to implement castling!)
4. **Watch for Captures**: The CPU prioritizes capturing your pieces
5. **Plan Ahead**: Think 2-3 moves ahead to avoid losing pieces

### Common Mistakes to Avoid

- ❌ Leaving your king unprotected
- ❌ Moving the same piece multiple times while undeveloped
- ❌ Ignoring undefended pieces
- ❌ Making moves without checking for captures

## Example Game Session

```
    a b c d e f g h
  ┌─────────────────┐
8 │ r n b q k b n r │
7 │ p p p p p p p p │
6 │ . . . . . . . . │
5 │ . . . . . . . . │
4 │ . . . . P . . . │
3 │ . . . . . . . . │
2 │ P P P P . P P P │
1 │ R N B Q K B N R │
  └─────────────────┘

Your move (e.g., e2e4): g1f3
CPU is thinking...
CPU moves N to f6
```

## Game Ending

The game ends when:
- You have no valid moves and your king is in check (Checkmate - You lose)
- You quit by pressing 'q'
- An error occurs

## Current Limitations

- No castling move
- No en passant capture
- No pawn promotion
- No draw detection
- No undo functionality

These features can be added in future versions!

## Troubleshooting

### "Invalid move. Try again."
- Make sure the move follows chess rules
- Verify the square notation (a-h for columns, 1-8 for rows)
- Check that you're not moving an opponent's piece

### "Invalid format. Use: e2e4"
- Enter exactly 4 characters: `[from_col][from_row][to_col][to_row]`
- Use lowercase letters for columns (a-h)
- Use numbers for rows (1-8)

### Terminal looks corrupted
- Resize your terminal window
- Try clearing the screen with `clear` command

## Future Enhancements

- [ ] Better AI with minimax algorithm
- [ ] Difficulty levels (Easy, Medium, Hard)
- [ ] Move history/replay functionality
- [ ] Castling and en passant
- [ ] Pawn promotion
- [ ] Checkmate detection
- [ ] Draw by repetition/insufficient material
- [ ] Save and load games
- [ ] Move undo functionality

## Chess Resources

To improve your game:
- [Chess.com](https://www.chess.com) - Learn tactics and play online
- [Lichess.org](https://lichess.org) - Free chess platform
- Classic opening moves to learn: Italian Game, French Defense, Sicilian Defense

## License

Free to use and modify!

## Author

Created as part of interactive CLI games collection
