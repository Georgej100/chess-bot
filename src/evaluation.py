import chess

piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9
}

def evaluate(board: chess.Board) -> float:
    evaluation: float = 0.00

    if board.is_checkmate():
        return -2000
    if board.is_check():
        evaluation -= 10

    return evaluation

def count_matieral_difference(board: chess.Board) -> int:
    black_matieral: int = 0
    white_matieral: int = 0

    for piece_type in piece_values:
        black_matieral += len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
        white_matieral += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type] 

    difference: int = white_matieral - black_matieral
    if board.turn == chess.BLACK:
        difference *= -1

    return difference
