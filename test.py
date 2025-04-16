
if __name__ == "__main__":

    def print_board(board):
        for row in board:
            print(" ".join(row))
        print()

    def check_win(board, row, col, player):
        directions = [(0,1), (1,0), (1,1), (1,-1)]
        for dx, dy in directions:
            count = 1
            # Check forward
            x, y = row + dx, col + dy
            while 0 <= x < 15 and 0 <= y < 15 and board[x][y] == player:
                count += 1
                x, y = x + dx, y + dy
            # Check backward
            x, y = row - dx, col - dy
            while 0 <= x < 15 and 0 <= y < 15 and board[x][y] == player:
                count += 1
                x, y = x - dx, y - dy
            if count >= 5:
                return True
        return False

    def play_gomoku():
        # Initialize empty 15x15 board
        board = [["."] * 15 for _ in range(15)]
        players = ["X", "O"]
        current = 0
        
        while True:
            print_board(board)
            player = players[current]
            print(f"Player {player}'s turn")
            
            try:
                row = int(input("Enter row (0-14): "))
                col = int(input("Enter column (0-14): "))
                
                if not (0 <= row < 15 and 0 <= col < 15):
                    print("Invalid position! Try again.")
                    continue
                    
                if board[row][col] != ".":
                    print("Position already taken! Try again.")
                    continue
                
                board[row][col] = player
                
                if check_win(board, row, col, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                    
                # Check for draw
                if all(cell != "." for row in board for cell in row):
                    print_board(board)
                    print("It's a draw!")
                    break
                
                current = (current + 1) % 2
                
            except ValueError:
                print("Invalid input! Please enter numbers.")
                continue
            except KeyboardInterrupt:
                print("\nGame ended by user.")
                break

    print("\nWelcome to Gomoku (Five in a Row)!")
    print("Players take turns placing X and O on the board.")
    print("First to get 5 in a row (horizontal, vertical, or diagonal) wins!")
    play_gomoku()
