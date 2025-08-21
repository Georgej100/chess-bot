import chess
import src.evaluation as evaluation
import src.opening as opening

class Bot: 
    def __init__(self, opening_table_bounds: int, opening_table: str) -> None:
        self.posistions_searched = 0
        self.opening_table_bounds = opening_table_bounds
        self.opening_table = opening_table

    def think(self, board: chess.Board, depth: int) -> chess.Move:
        if len(board.move_stack) < self.opening_table_bounds:
            return opening.get_move_from_table(board, self.opening_table)            


        moves = iter(board.generate_legal_moves())

        best_move: chess.Move = chess.Move.null()
        best_score: float = -1000

        for move in moves:
            board.push(move)
            score: float = -self.search(board, (depth-1))
            board.pop()

            if score > best_score:
                best_score = score
                best_move = move

        print(self.posistions_searched)
        return best_move

    def search(self, board: chess.Board, depth: int) -> float:
        self.posistions_searched += 1

        if depth == 0:
            return evaluation.evaluate(board)

        if board.is_game_over():
            return evaluation.evaluate(board)

        best_score: float = -1000
    
        moves = iter(board.generate_legal_moves())

        for move in moves:
            board.push(move)
            score: float = -self.search(board, (depth - 1))
            board.pop()

            if score > best_score:
                best_score = score
    
        return best_score


