"""Game board"""
BOARD_SIZE = 9
WIN_PATTERNS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]

def display_game_board(game_board: list):
    """Displays game board"""
    for square in range(0, len(game_board), 3):
        print(f"|{game_board[square]}|{game_board[square + 1]}|{game_board[square + 2]}|")


def validate_position(position: str) -> bool:
    """Check if user input is a number between 1, 10"""
    return position.isdigit() and 1 <= int(position) <= BOARD_SIZE

def update_position(position: str,
                    player_symbol: str,
                    game_board:list) -> bool:
    """Add X or O to player selected position
    return True if successfully added
    otherwise return False"""
    if validate_position(position):
        position = int(position)
        if game_board[position - 1] == " ":
            game_board[position-1] = player_symbol
            return True
    print("Invalid position! Please try again")
    return False

def x_or_o_choice(user_input: str) -> tuple[str, str]:
    """Player selects between X or O"""
    if user_input == "O":
        return "O", "X"
    return "X", "O"

def check_winner(game_board: list,
                 player_one_symbol: str,
                 player_two_symbol: str) -> str:
    """Return false is player has one, True otherwise to continue game"""
    symbol_to_player = {player_one_symbol: "Player one", player_two_symbol: "Player two"}

    for a, b, c in WIN_PATTERNS:
        if game_board[a] == game_board[b] == game_board[c] != " ":
            return  symbol_to_player[game_board[a]]
    return None

def board_full(game_board: list) -> bool:
    return " " in game_board

def game_logic():
    """Game logic"""
    game_board = [" "] * BOARD_SIZE
    game_running = True
    player_one_turn = True

    player_one_symbol, player_two_symbol = x_or_o_choice(input("Player1 select X or O \n"))
    display_game_board(game_board)

    while game_running:
        if player_one_turn:
            player_choice = input("Player1 select a position between 1 to 9 \n")
            if update_position(player_choice, player_one_symbol, game_board):
                player_one_turn = False
        else:
            player_choice = input("Player2 select a position between 1 to 9 \n")
            if update_position(player_choice, player_two_symbol, game_board):
                player_one_turn = True

        winner = check_winner(game_board, player_one_symbol, player_two_symbol)
        if winner:
            print(f"{winner} wins!")
            game_running = False

        if not board_full(game_board):
            print("Draw")
            game_running = False

        display_game_board(game_board)
game_logic()
