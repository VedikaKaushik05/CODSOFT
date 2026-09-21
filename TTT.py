board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def show_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner():
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return True

    return False

def check_draw():
    return " " not in board


print("===== TIC TAC TOE =====")
print("Player 1 = X")
print("Player 2 = O")

player = "X"

while True:

    show_board()

    choice = input("Player " + player + ", choose position (1-9): ")

    if not choice.isdigit() or int(choice) < 1 or int(choice) > 9:
        print("Please enter a number from 1 to 9.")
        continue

    position = int(choice) - 1

    if board[position] != " ":
        print("That position is already taken!")
        continue

    board[position] = player

    if check_winner():
        show_board()
        print("🎉 Player", player, "WINS!")
        break

    if check_draw():
        show_board()
        print("🤝 It's a DRAW!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
