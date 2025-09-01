#!/usr/bin/python3

def print_board(board):
    """Affiche le plateau de jeu."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Séparateur plus proportionnel

def check_winner(board):
    """Vérifie si un joueur a gagné.
    
    Returns:
        str: "X" ou "O" si un joueur a gagné, None sinon.
    """
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Vérifie les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """Vérifie si le plateau est rempli.
    
    Returns:
        bool: True si toutes les cases sont occupées, False sinon.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Fonction principale du jeu Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Boucle de saisie sécurisée pour la ligne
        while True:
            try:
                row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
                if row not in [0, 1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 0, 1, or 2.")

        # Boucle de saisie sécurisée pour la colonne
        while True:
            try:
                col = int(input(f"Enter column (0, 1, 2) for player {player}: "))
                if col not in [0, 1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 0, 1, or 2.")

        # Vérifie si la case est libre
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Change de joueur
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()