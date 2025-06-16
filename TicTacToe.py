"""Game game_board"""
game_board = [" "] * 9


def display_game_board():
    """Displays game board"""
    for square in range(0, len(game_board), 3):
        print(f"|{game_board[square]}|{game_board[square + 1]}|{game_board[square + 2]}|")

def update_position(position: int, turn_one: bool, player_pick: str) -> bool:
    """Add X or O to player selected position
    return True if successfully added
    otherwise return False"""
    if game_board[position - 1] == " ":
        if turn_one:
            game_board[position-1] = player_pick
        else:
            game_board[position-1] = player_pick
        return True
    return False

def x_or_o():
    """Player selects between X or O"""
    player_one_choice = input("Player one please select X or O \n")
    if player_one_choice == "O":
        return "O", "X"
    return "X", "O"


def game_logic():
    """Game logic"""
    playing = True
    player_one_turn = True
    player_one_pick, player_two_pick = x_or_o()
    while playing:
        display_game_board()
        if player_one_turn:
            player_choice = int(input("Player1 select a position between 1 to 9 \n"))
            player_one_turn = update_position(player_choice,
                                              player_one_turn, player_one_pick)
        else:
            player_choice = int(input("Player2 select a position between 1 to 9 \n"))
            player_one_turn = update_position(player_choice,
                                              player_one_turn, player_two_pick)
game_logic()
