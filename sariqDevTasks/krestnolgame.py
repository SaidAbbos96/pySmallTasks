game_board = [" "," "," "," "," "," "," "," "," "]
combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def print_state(state):
    for i, c in enumerate(state):
        if (i+1) % 3 == 0:
            print(f"{c}")
        else:
            print(f"{c}|", end="")

# print_state(game_board)

def get_winner(state, combinations):
    for (x, y,z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == "x" or state[x] == "o"):
            return state[x]
        else:
            return ''

def play_game(game_board):
    gamer = "x"
    while (get_winner(game_board, combinations) == ""):
        position = int(input(f"Janob {gamer} qayerga belgi qo'yishni istaysiz ?")) - 1
        game_board[position] = gamer
        print_state(game_board)
        winner = get_winner(game_board, combinations)
        if winner != "":
            print(f"Janob {gamer} siz yutdiz !")
        
        gamer = "x" if gamer == "o" else "o"

play_game(game_board)
