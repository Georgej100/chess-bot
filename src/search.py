import chess
import src.evaluation as evaluation 

def think(board: chess.Board, depth: int) -> chess.Move:
    moves = iter(board.generate_legal_moves())

    best_move: chess.Move = chess.Move.null()
    best_score: float = -100

    for move in moves:
        board.push(move)
        score: float = -search(board, (depth - 1))
        board.pop()

        if score > best_score:
            best_score = score
            best_move = move


    return best_move


def search(board: chess.Board, depth: int) -> float:
    if depth == 0:
        return evaluation.evaluate(board)

    if board.is_game_over():
        return evaluation.evaluate(board)

    best_score: float = -100
    
    moves = iter(board.generate_legal_moves())

    for move in moves:
        board.push(move)
        score: float = -search(board, (depth - 1))
        board.pop()

        if score > best_score:
            best_score = score
    
    return best_score


