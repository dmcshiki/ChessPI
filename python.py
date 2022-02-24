import chess

def Movement(board):
    

 if(not board.is_checkmate() or not board.is_stalemate() 
    or not board.is_insufficient_material()
    or not board.is_game_over()):
    print('Jogadas disponiveis: ', board.legal_moves)
    move = input ("Digite sua jogada: ")

    try:
        board.push_san(move)
        print(board)
    except:
        Movement()




board = chess.Board()
Movement(board)