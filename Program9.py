def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # row
            return True
        if all([board[j][i] == player for j in range(3)]):  # column
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for _ in range(9):
        print_board(board)
        player = players[turn % 2]
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter col (0-2): "))

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"🎉 Player {player} wins!")
                return
            turn += 1
        else:
            print("Cell already taken, try again.")

    print_board(board)
    print("It's a tie!")

tic_tac_toe()
