def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell!=" " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid position! Try again.")
                continue

            if board[row][col] !=" ":
                print("Cell already occupied! Try again.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉Player {current_player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player =="X" else "X"

        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    tic_tac_toe()