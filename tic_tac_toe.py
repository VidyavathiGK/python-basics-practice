def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[cell] == player for cell in condition) for condition in win_conditions)

def play_tic_tac_toe():
    board = [str(i + 1) for i in range(9)]
    current_player = "X"
    turns = 0
    
    print("Welcome to Tic-Tac-Toe!")
    
    while turns < 9:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue
            
        if move < 0 or move > 8 or board[move] in ["X", "O"]:
            print("Invalid move! Spot already taken or out of range.")
            continue
            
        board[move] = current_player
        turns += 1
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
            
        current_player = "O" if current_player == "X" else "X"
        
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    play_tic_tac_toe()
