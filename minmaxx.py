def print_board(board):
    for i in range(3):
        print(board[3*i], '|', board[3*i+1], '|', board[3*i+2])
        if i < 2:
            print('---------')

def check_winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for (i,j,k) in wins:
        if board[i] == board[j] == board[k] != ' ':
            return board[i]  # 'X' or 'O'
    if ' ' not in board:
        return 'Draw'
    return None  # Game is still ongoing

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [' ' for _ in range(9)]
    print("Welcome to Tic-Tac-Toe! You are 'O', AI is 'X'.")
    print("Positions are numbered 0 to 8 as follows:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")
    
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        # Human turn (O)
        try:
            human_move = int(input("Enter your move (0-8): "))
        except ValueError:
            print("Invalid input! Enter a number from 0 to 8.")
            continue
        
        if human_move < 0 or human_move > 8:
            print("Invalid position! Try again.")
            continue
        if board[human_move] != ' ':
            print("Position already taken! Try again.")
            continue

        board[human_move] = 'O'

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        # AI turn (X)
        move = best_move(board)
        board[move] = 'X'
        print(f"AI plays move {move}")

if __name__ == "__main__":
    play_game()

