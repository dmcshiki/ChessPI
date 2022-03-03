import chess

def endGame():
    
    if(not board.is_checkmate() or not board.is_stalemate() 
    or not board.is_insufficient_material()
    or not board.is_game_over()):    
        return false
    else: 
        return true

def Play():

    while(endGame()):
        moves = str(board.legal_moves)
        startingMoves = int(moves.index("(")) 
        endingMoves = int(moves.index(")"))
        movementList = list(moves[startingMoves+1:endingMoves].split(" "))
        print('Jogadas disponiveis: ')
        for move in movementList:
            print(move)
        movement = input ("Digite sua jogada: ")
        try:
            board.push_san(movement)
            print(board)
        except:
            print('Movimento invalido, tente novamente.')
            Play(board)

def Play():

    while (endGame()):
          transformList()
      movement = input("Digite sua jogada: ")
      try:
        board.push_san(movement)
        print(" ")
        print(board)
          
      except:
        print('Movimento invalido, tente novamente.')
        Play(board)
        
board = chess.Board()
Play()
