import chess
import chess.polyglot

def get_move_from_table(board: chess.Board, path: str) -> chess.Move:
    best_move: chess.Move = chess.Move.null()
    best_weight = 0

    with chess.polyglot.open_reader(path) as reader:
        for entry in reader.find_all(board):
            if entry.weight > best_weight:
                best_weight = entry.weight
                best_move = entry.move
    
    print(f"Best book move: {best_move}")
    return best_move

