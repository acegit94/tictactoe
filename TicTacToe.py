"""Game board"""
BOARD_SIZE = 9

def display_game_board(game_board: list):
    """Displays game board"""
    for square in range(0, len(game_board), 3):
        print(f"|{game_board[square]}|{game_board[square + 1]}|{game_board[square + 2]}|")


def validate_position(position: str) -> bool:
    """Check if user input is a number between 1, 10"""
    return position.isdigit() and 1 <= int(position) <= BOARD_SIZE

def update_position(position: str, player_symbol: str, game_board:list) -> bool:
    """Add X or O to player selected position
    return True if successfully added
    otherwise return False"""
    if validate_position(position=position):
        position = int(position)
        if game_board[position - 1] == " ":
            game_board[position-1] = player_symbol
            return True
    print("Invalid position! Please try again")
    return False

def x_or_o():
    """Player selects between X or O"""
    player_one_choice = input("Player one please select X or O \n").strip().upper()
    if player_one_choice == "O":
        return "O", "X"
    return "X", "O"

def check_horizontal(game_board:list, player_one_symbol: str, player_two_symbol: str) -> bool:
    """Check rows for winner"""
    rows = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8)
    ]
    for a, b, c in rows:
        if game_board[a] == game_board[b] == game_board[c]:
            if game_board[a] == player_one_symbol:
                print("Player one wins!")
                return True
            if game_board[a] == player_two_symbol:
                print("Player two wins!")
                return True
    return False

def check_vertical(game_board:list, player_one_symbol: str, player_two_symbol: str) -> bool:
    """Check columns for winner"""
    columns = [
        (0,3,6),
        (1,4,7),
        (2,5,8)
    ]
    for a,b,c in columns:
        if game_board[a] == game_board[b] == game_board[c]:
            if game_board[a] == player_one_symbol:
                print("Player one wins!")
                return True
            if game_board[a] == player_two_symbol:
                print("Player two wins!")
                return True
    return False

def check_diagonal(game_board:list, player_one_symbol: str, player_two_symbol: str) -> bool:
    """Check diagonals for winner"""
    diagonals = [
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in diagonals:
        if game_board[a] == game_board[b] == game_board[c]:
            if game_board[a] == player_one_symbol:
                print("Player one wins")
                return True
            if game_board[a] == player_two_symbol:
                print("Player two wins")
                return True
        return False

def check_winner(player_one_symbol,
                 player_two_symbol,
                 game_board):
    """Check if there is a winner"""
    if check_horizontal(game_board=game_board, player_one_symbol=player_one_symbol,
                        player_two_symbol=player_two_symbol) or check_vertical(
                        game_board=game_board, player_one_symbol=player_one_symbol,
                        player_two_symbol=player_two_symbol) or check_diagonal(
                        game_board=game_board, player_one_symbol=player_one_symbol,
                        player_two_symbol=player_two_symbol):
        return False
    return True

def game_logic():
    """Game logic"""
    playing = True
    player_one_turn = True
    game_board = [" "] * BOARD_SIZE
    player_one_symbol, player_two_symbol = x_or_o()
    display_game_board(game_board=game_board)
    while playing:
        if player_one_turn:
            player_choice = input("Player1 select a position between 1 to 9 \n")
            if update_position(player_choice, player_one_symbol, game_board=game_board):
                player_one_turn = False
        else:
            player_choice = input("Player2 select a position between 1 to 9 \n")
            if update_position(player_choice, player_two_symbol, game_board=game_board):
                player_one_turn = True
        playing = check_winner(game_board=game_board, player_one_symbol=player_one_symbol,
                                   player_two_symbol=player_two_symbol,
                                   )
        display_game_board(game_board=game_board)
game_logic()
