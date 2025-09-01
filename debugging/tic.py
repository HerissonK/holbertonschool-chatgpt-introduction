def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Gestion des entrées invalides
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in [0,1,2] or col not in [0,1,2]:
                print("Invalid input. Row and column must be 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        # Vérifier si le joueur actuel a gagné
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Vérifier si le plateau est plein → match nul
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Changer de joueur
        player = "O" if player == "X" else "X"

tic_tac_toe()
