import chess
import src.bot as bot

def main():
    print("Chess Bot V1.0")
    board = chess.Board()
    chess_bot = bot.Bot(6, "data/polyglot/codekiddy.bin")

    print(board)
    
    while (board.is_game_over() == False):
        if board.turn == chess.WHITE:
            user_play(board)
        else:
            board.push(chess_bot.think(board, 4))
        print(f"{board}\n")



def user_play(board: chess.Board) -> None:
    try:
        move = input("Move to play: ")
        board.push_san(move)
    except chess.IllegalMoveError:
        print("IllegalMoveError: Try again\n")
    except chess.InvalidMoveError:
        print("InvalidMoveError: Try again\n")
        user_play(board)

    

if __name__ == "__main__":
    main()
