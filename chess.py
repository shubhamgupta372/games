#!/usr/bin/env python3
"""
Interactive CLI-based Chess Game
Player (White) vs CPU (Black)
"""

import random
from enum import Enum
from typing import List, Tuple, Optional


class PieceType(Enum):
    PAWN = "P"
    ROOK = "R"
    KNIGHT = "N"
    BISHOP = "B"
    QUEEN = "Q"
    KING = "K"


class Piece:
    def __init__(self, piece_type: PieceType, is_white: bool):
        self.type = piece_type
        self.is_white = is_white
    
    def __str__(self):
        char = self.type.value
        return char if self.is_white else char.lower()
    
    def __repr__(self):
        return self.__str__()


class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self._setup_board()
    
    def _setup_board(self):
        """Initialize standard chess starting position"""
        # Black pieces (top)
        self.board[0][0] = Piece(PieceType.ROOK, False)
        self.board[0][1] = Piece(PieceType.KNIGHT, False)
        self.board[0][2] = Piece(PieceType.BISHOP, False)
        self.board[0][3] = Piece(PieceType.QUEEN, False)
        self.board[0][4] = Piece(PieceType.KING, False)
        self.board[0][5] = Piece(PieceType.BISHOP, False)
        self.board[0][6] = Piece(PieceType.KNIGHT, False)
        self.board[0][7] = Piece(PieceType.ROOK, False)
        
        for i in range(8):
            self.board[1][i] = Piece(PieceType.PAWN, False)
        
        # White pieces (bottom)
        for i in range(8):
            self.board[6][i] = Piece(PieceType.PAWN, True)
        
        self.board[7][0] = Piece(PieceType.ROOK, True)
        self.board[7][1] = Piece(PieceType.KNIGHT, True)
        self.board[7][2] = Piece(PieceType.BISHOP, True)
        self.board[7][3] = Piece(PieceType.QUEEN, True)
        self.board[7][4] = Piece(PieceType.KING, True)
        self.board[7][5] = Piece(PieceType.BISHOP, True)
        self.board[7][6] = Piece(PieceType.KNIGHT, True)
        self.board[7][7] = Piece(PieceType.ROOK, True)
    
    def display(self):
        """Display the board"""
        print("\n    a b c d e f g h")
        print("  ┌─────────────────┐")
        for i in range(8):
            print(f"{8-i} │", end="")
            for j in range(8):
                piece = self.board[i][j]
                if piece:
                    print(f" {piece}", end="")
                else:
                    print(" .", end="")
            print(" │" + str(8-i))
        print("  └─────────────────┘")
        print("    a b c d e f g h\n")
    
    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None
    
    def move_piece(self, from_row: int, from_col: int, to_row: int, to_col: int) -> bool:
        """Move a piece and return True if successful"""
        piece = self.get_piece(from_row, from_col)
        if not piece:
            return False
        
        if not self._is_valid_move(piece, from_row, from_col, to_row, to_col):
            return False
        
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        return True
    
    def _is_valid_move(self, piece: Piece, from_row: int, from_col: int, 
                       to_row: int, to_col: int) -> bool:
        """Check if a move is valid"""
        target = self.get_piece(to_row, to_col)
        
        # Can't capture own piece
        if target and target.is_white == piece.is_white:
            return False
        
        # Check piece-specific movement rules
        if piece.type == PieceType.PAWN:
            return self._is_valid_pawn_move(piece, from_row, from_col, to_row, to_col)
        elif piece.type == PieceType.ROOK:
            return self._is_valid_rook_move(from_row, from_col, to_row, to_col)
        elif piece.type == PieceType.KNIGHT:
            return self._is_valid_knight_move(from_row, from_col, to_row, to_col)
        elif piece.type == PieceType.BISHOP:
            return self._is_valid_bishop_move(from_row, from_col, to_row, to_col)
        elif piece.type == PieceType.QUEEN:
            return self._is_valid_queen_move(from_row, from_col, to_row, to_col)
        elif piece.type == PieceType.KING:
            return self._is_valid_king_move(from_row, from_col, to_row, to_col)
        
        return False
    
    def _is_valid_pawn_move(self, piece: Piece, from_row: int, from_col: int,
                            to_row: int, to_col: int) -> bool:
        target = self.get_piece(to_row, to_col)
        direction = -1 if piece.is_white else 1
        start_row = 6 if piece.is_white else 1
        
        # Forward move
        if from_col == to_col:
            if from_row + direction == to_row and not target:
                return True
            if from_row == start_row and from_row + 2 * direction == to_row and not target:
                if not self.get_piece(from_row + direction, from_col):
                    return True
        
        # Capture diagonally
        if abs(to_col - from_col) == 1 and from_row + direction == to_row and target:
            return True
        
        return False
    
    def _is_valid_rook_move(self, from_row: int, from_col: int, 
                            to_row: int, to_col: int) -> bool:
        if from_row != to_row and from_col != to_col:
            return False
        return self._is_path_clear(from_row, from_col, to_row, to_col)
    
    def _is_valid_knight_move(self, from_row: int, from_col: int,
                              to_row: int, to_col: int) -> bool:
        dr = abs(to_row - from_row)
        dc = abs(to_col - from_col)
        return (dr == 2 and dc == 1) or (dr == 1 and dc == 2)
    
    def _is_valid_bishop_move(self, from_row: int, from_col: int,
                              to_row: int, to_col: int) -> bool:
        if abs(to_row - from_row) != abs(to_col - from_col):
            return False
        return self._is_path_clear(from_row, from_col, to_row, to_col)
    
    def _is_valid_queen_move(self, from_row: int, from_col: int,
                             to_row: int, to_col: int) -> bool:
        if from_row == to_row or from_col == to_col:
            return self._is_path_clear(from_row, from_col, to_row, to_col)
        if abs(to_row - from_row) == abs(to_col - from_col):
            return self._is_path_clear(from_row, from_col, to_row, to_col)
        return False
    
    def _is_valid_king_move(self, from_row: int, from_col: int,
                            to_row: int, to_col: int) -> bool:
        return abs(to_row - from_row) <= 1 and abs(to_col - from_col) <= 1
    
    def _is_path_clear(self, from_row: int, from_col: int,
                       to_row: int, to_col: int) -> bool:
        """Check if path is clear between two positions"""
        dr = 0 if to_row == from_row else (1 if to_row > from_row else -1)
        dc = 0 if to_col == from_col else (1 if to_col > from_col else -1)
        
        r, c = from_row + dr, from_col + dc
        while (r, c) != (to_row, to_col):
            if self.board[r][c] is not None:
                return False
            r += dr
            c += dc
        
        return True
    
    def get_all_valid_moves(self, is_white: bool) -> List[Tuple[int, int, int, int]]:
        """Get all valid moves for a player"""
        moves = []
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.is_white == is_white:
                    for to_i in range(8):
                        for to_j in range(8):
                            if self._is_valid_move(piece, i, j, to_i, to_j):
                                moves.append((i, j, to_i, to_j))
        return moves


class ChessAI:
    def __init__(self, board: ChessBoard):
        self.board = board
    
    def get_best_move(self) -> Optional[Tuple[int, int, int, int]]:
        """Get the best move for CPU (Black)"""
        valid_moves = self.board.get_all_valid_moves(is_white=False)
        
        if not valid_moves:
            return None
        
        # Simple AI: prioritize capturing pieces
        capture_moves = []
        for from_r, from_c, to_r, to_c in valid_moves:
            if self.board.get_piece(to_r, to_c):
                capture_moves.append((from_r, from_c, to_r, to_c))
        
        if capture_moves:
            return random.choice(capture_moves)
        
        return random.choice(valid_moves)


class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.ai = ChessAI(self.board)
        self.is_white_turn = True
    
    def parse_move(self, move_str: str) -> Optional[Tuple[int, int, int, int]]:
        """Parse chess notation like 'e2e4'"""
        move_str = move_str.strip().lower()
        if len(move_str) != 4:
            return None
        
        from_col = ord(move_str[0]) - ord('a')
        from_row = 8 - int(move_str[1])
        to_col = ord(move_str[2]) - ord('a')
        to_row = 8 - int(move_str[3])
        
        if not (0 <= from_col < 8 and 0 <= from_row < 8 and
                0 <= to_col < 8 and 0 <= to_row < 8):
            return None
        
        return (from_row, from_col, to_row, to_col)
    
    def play(self):
        """Main game loop"""
        print("=" * 50)
        print("        CHESS GAME")
        print("=" * 50)
        print("\nYou are White (bottom)")
        print("CPU is Black (top)")
        print("\nMove notation: e2e4 (from square to square)")
        print("Type 'q' to quit, 'h' for help\n")
        
        while True:
            self.board.display()
            
            if self.is_white_turn:
                while True:
                    move_input = input("Your move (e.g., e2e4): ").strip()
                    
                    if move_input.lower() == 'q':
                        print("Thanks for playing!")
                        return
                    
                    if move_input.lower() == 'h':
                        print("Enter moves in the format: [from_square][to_square]")
                        print("Squares are labeled a-h (columns) and 1-8 (rows)")
                        print("Example: e2e4 moves piece from e2 to e4")
                        continue
                    
                    move = self.parse_move(move_input)
                    if not move:
                        print("Invalid format. Use: e2e4")
                        continue
                    
                    from_r, from_c, to_r, to_c = move
                    if self.board.move_piece(from_r, from_c, to_r, to_c):
                        break
                    else:
                        print("Invalid move. Try again.")
                
                self.is_white_turn = False
            else:
                print("CPU is thinking...")
                import time
                time.sleep(1)
                
                move = self.ai.get_best_move()
                if not move:
                    print("Checkmate! You win!")
                    return
                
                from_r, from_c, to_r, to_c = move
                piece = self.board.get_piece(from_r, from_c)
                to_col_char = chr(ord('a') + to_c)
                to_row_num = 8 - to_r
                print(f"CPU moves {piece} to {to_col_char}{to_row_num}")
                
                self.board.move_piece(from_r, from_c, to_r, to_c)
                self.is_white_turn = True


def main():
    game = ChessGame()
    game.play()


if __name__ == "__main__":
    main()
