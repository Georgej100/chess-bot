from re import search
import chess 


def main():
    print("Chess Bot V1.0")
    board = chess.Board()

    print(board)
    
    while (board.is_game_over() == False):
        if board.turn == chess.WHITE:
            move = input("White to play: ")
            board.push_san(move)
        else:
            board.push(think(board), 3)
        print(f"{board}\n")

def think(board: chess.Board, depth: int) -> chess.Move:
    moves = iter(board.generate_legal_moves())

    bestMove: chess.Move = chess.Move.null()
    bestScore: float = 0

    for move in moves:
        board.push(move)
        score: float = -search(board, (depth - 1))
        board.pop()

        if score > bestScore:
            bestScore = score
            bestMove = move


    return bestMove


def search(board: chess.Board, depth: int) -> float:
    if depth == 0:
        return evaluatePos(board)

    if board.is_game_over():
        return evaluatePos(board)

    bestScore: float = 0
    
    moves = iter(board.generate_legal_moves())

    for move in moves:
        board.push(move)
        score: float = -search(board, (depth - 1))
        board.pop()

        if score > bestScore:
            bestScore = score
    
    return bestScore





def evaluatePos(board: chess.Board) -> float:
    return 0 

    

if __name__ == "__main__":
    main()
