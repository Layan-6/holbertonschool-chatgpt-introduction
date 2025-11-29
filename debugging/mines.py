#!/usr/bin/env python3
import random

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = mines
        self.mine_positions = set(random.sample(range(width * height), mines))
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flagged = [[False for _ in range(width)] for _ in range(height)]
        
        # Initialize mine counts
        for y in range(height):
            for x in range(width):
                if (y * width + x) in self.mine_positions:
                    self.board[y][x] = -1  # -1 represents a mine
                else:
                    self.board[y][x] = self.count_surrounding_mines(x, y)
    
    def count_surrounding_mines(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mine_positions:
                        count += 1
        return count
    
    def print_board(self, show_all=False):
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if show_all or self.revealed[y][x]:
                    if self.board[y][x] == -1:
                        print('*', end=' ')
                    elif self.board[y][x] == 0:
                        print('.', end=' ')
                    else:
                        print(self.board[y][x], end=' ')
                elif self.flagged[y][x]:
                    print('F', end=' ')
                else:
                    print('#', end=' ')
            print()
    
    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        
        if self.revealed[y][x] or self.flagged[y][x]:
            return True
        
        self.revealed[y][x] = True
        
        if self.board[y][x] == -1:
            return False  # Hit a mine
        
        if self.board[y][x] == 0:
            # Reveal surrounding cells recursively for empty cells
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx] and not self.flagged[ny][nx]:
                            self.reveal(nx, ny)
        return True
    
    def has_won(self):
        # Check if all non-mine cells have been revealed
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != -1 and not self.revealed[y][x]:
                    return False
        return True
    
    def play(self):
        print("Welcome to Minesweeper!")
        print("Enter coordinates to reveal cells.")
        
        while True:
            self.print_board()
            
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                
                if not self.reveal(x, y):
                    print("Game Over! You hit a mine.")
                    self.print_board(show_all=True)
                    break
                
                if self.has_won():
                    print("Congratulations! You've won the game.")
                    self.print_board(show_all=True)
                    break
                    
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid coordinates.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
