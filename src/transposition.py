import chess

def transposition_scanner(func):
    def wrapper(board: chess.Board, depth: int):
        
        evaluation = func(board, depth)

        return evaluation
    return wrapper
