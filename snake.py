#!/usr/bin/env python3
"""
Interactive CLI-based Snake Game
Player vs No AI (Simple obstacle-free mode)
"""

import curses
import random
import time
from enum import Enum
from collections import deque


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


def get_direction_char(current_dir):
    """Get snake head character based on direction"""
    if current_dir == Direction.UP:
        return '▲'
    elif current_dir == Direction.DOWN:
        return '▼'
    elif current_dir == Direction.LEFT:
        return '◀'
    elif current_dir == Direction.RIGHT:
        return '▶'
    return '◉'


def get_body_connector(prev_pos, curr_pos, next_pos):
    """Determine body character based on direction of travel"""
    # Calculate directions
    prev_dir = (curr_pos[0] - prev_pos[0], curr_pos[1] - prev_pos[1])
    next_dir = (next_pos[0] - curr_pos[0], next_pos[1] - curr_pos[1])
    
    # Normalize to get actual directions
    prev_dir = (min(max(prev_dir[0], -1), 1), min(max(prev_dir[1], -1), 1))
    next_dir = (min(max(next_dir[0], -1), 1), min(max(next_dir[1], -1), 1))
    
    # Straight line
    if prev_dir == next_dir:
        if prev_dir[0] != 0:  # Vertical
            return '║'
        else:  # Horizontal
            return '═'
    
    # Turn
    return '●'


class SnakeGame:
    def __init__(self, height=20, width=60):
        self.height = height
        self.width = width
        self.score = 0
        self.high_score = 0
        
        # Initialize snake in the middle
        start_row = height // 2
        start_col = width // 2
        self.snake = deque([(start_row, start_col)])
        
        # Random initial food position
        self.food = self._generate_food()
        
        # Starting direction
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        
        self.game_over = False
        self.game_won = False
        
    def _generate_food(self):
        """Generate food at a random position not occupied by snake"""
        while True:
            food = (random.randint(0, self.height - 1), 
                   random.randint(0, self.width - 1))
            if food not in self.snake:
                return food
    
    def update(self):
        """Update game state"""
        if self.game_over or self.game_won:
            return
        
        # Update direction
        self.direction = self.next_direction
        
        # Calculate new head position
        head_row, head_col = self.snake[0]
        dr, dc = self.direction.value
        new_row = head_row + dr
        new_col = head_col + dc
        
        # Check wall collision
        if (new_row < 0 or new_row >= self.height or 
            new_col < 0 or new_col >= self.width):
            self.game_over = True
            return
        
        # Check self collision
        if (new_row, new_col) in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.appendleft((new_row, new_col))
        
        # Check food collision
        if (new_row, new_col) == self.food:
            self.score += 10
            self.food = self._generate_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def change_direction(self, direction):
        """Change direction (prevents reversing into itself)"""
        # Prevent reversing
        if (direction == Direction.UP and self.direction != Direction.DOWN) or \
           (direction == Direction.DOWN and self.direction != Direction.UP) or \
           (direction == Direction.LEFT and self.direction != Direction.RIGHT) or \
           (direction == Direction.RIGHT and self.direction != Direction.LEFT):
            self.next_direction = direction


def run_game(stdscr):
    """Main game loop"""
    # Setup curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    # Initialize colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)      # Snake head
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)       # Snake body
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)        # Food
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)     # Border
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)      # Text
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)    # Score
    
    # Get terminal dimensions
    max_height, max_width = stdscr.getmaxyx()
    game_width = min(60, max_width - 4)
    game_height = min(20, max_height - 6)
    
    game = SnakeGame(game_height, game_width)
    
    # Start game loop
    while not game.game_over and not game.game_won:
        # Handle input
        key = stdscr.getch()
        if key == ord('q'):
            return
        elif key == ord('w') or key == curses.KEY_UP:
            game.change_direction(Direction.UP)
        elif key == ord('s') or key == curses.KEY_DOWN:
            game.change_direction(Direction.DOWN)
        elif key == ord('a') or key == curses.KEY_LEFT:
            game.change_direction(Direction.LEFT)
        elif key == ord('d') or key == curses.KEY_RIGHT:
            game.change_direction(Direction.RIGHT)
        
        # Update game
        game.update()
        
        # Draw
        stdscr.clear()
        
        # Draw border
        for i in range(game_width + 2):
            stdscr.addch(0, i, '#', curses.color_pair(4) | curses.A_BOLD)
            stdscr.addch(game_height + 1, i, '#', curses.color_pair(4) | curses.A_BOLD)
        for i in range(game_height + 2):
            stdscr.addch(i, 0, '#', curses.color_pair(4) | curses.A_BOLD)
            stdscr.addch(i, game_width + 1, '#', curses.color_pair(4) | curses.A_BOLD)
        
        # Draw snake
        snake_list = list(game.snake)
        for idx, (row, col) in enumerate(snake_list):
            if idx == 0:
                # Head with directional character
                head_char = get_direction_char(game.direction)
                stdscr.addch(row + 1, col + 1, head_char, curses.color_pair(1) | curses.A_BOLD)
            elif idx == len(snake_list) - 1:
                # Tail
                stdscr.addch(row + 1, col + 1, '○', curses.color_pair(2))
            else:
                # Body segments with connectors
                prev_pos = snake_list[idx - 1]
                next_pos = snake_list[idx + 1]
                body_char = get_body_connector(prev_pos, (row, col), next_pos)
                stdscr.addch(row + 1, col + 1, body_char, curses.color_pair(2))
        
        # Draw food
        food_row, food_col = game.food
        stdscr.addch(food_row + 1, food_col + 1, '★', curses.color_pair(3) | curses.A_BOLD)
        
        # Draw score
        score_text = f"Score: {game.score}"
        stdscr.addstr(game_height + 3, 1, score_text, curses.color_pair(6) | curses.A_BOLD)
        
        # Draw instructions
        info_text = "Controls: WASD or Arrow Keys | Q to quit"
        stdscr.addstr(game_height + 4, 1, info_text, curses.color_pair(5))
        
        stdscr.refresh()
    
    # Game over screen
    stdscr.clear()
    
    # Draw decorative border
    border_char = '═'
    for i in range(1, max_width - 1):
        stdscr.addch(max_height // 2 - 4, i, border_char, curses.color_pair(4) | curses.A_BOLD)
        stdscr.addch(max_height // 2 + 5, i, border_char, curses.color_pair(4) | curses.A_BOLD)
    
    for i in range(max_height // 2 - 4, max_height // 2 + 6):
        stdscr.addch(i, 0, '║', curses.color_pair(4) | curses.A_BOLD)
        stdscr.addch(i, max_width - 1, '║', curses.color_pair(4) | curses.A_BOLD)
    
    # Title
    title = "GAME OVER"
    stdscr.addstr(max_height // 2 - 3, max_width // 2 - len(title) // 2, title, curses.color_pair(3) | curses.A_BOLD)
    
    # Score information
    snake_length = len(game.snake)
    score_line = f"Final Score: {game.score}"
    length_line = f"Snake Length: {snake_length}"
    food_eaten = game.score // 10
    food_line = f"Food Eaten: {food_eaten}"
    
    stdscr.addstr(max_height // 2, max_width // 2 - len(score_line) // 2, score_line, curses.color_pair(6) | curses.A_BOLD)
    stdscr.addstr(max_height // 2 + 1, max_width // 2 - len(length_line) // 2, length_line, curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(max_height // 2 + 2, max_width // 2 - len(food_line) // 2, food_line, curses.color_pair(3) | curses.A_BOLD)
    
    # Exit instruction
    exit_msg = "Press any key to exit..."
    stdscr.addstr(max_height // 2 + 4, max_width // 2 - len(exit_msg) // 2, exit_msg, curses.color_pair(5))
    
    stdscr.refresh()
    stdscr.getch()


def main():
    print("=" * 50)
    print("        SNAKE GAME")
    print("=" * 50)
    print("\nInstructions:")
    print("  - Use WASD or Arrow Keys to move")
    print("  - Eat food (*) to grow and gain points")
    print("  - Avoid hitting walls and yourself")
    print("  - Press Q to quit at any time\n")
    input("Press Enter to start...")
    
    try:
        curses.wrapper(run_game)
    except KeyboardInterrupt:
        print("Game interrupted")


if __name__ == "__main__":
    main()
