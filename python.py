import chess

def endGame():
    return board.is_checkmate(
    ) or board.is_stalemate(
    ) or board.is_insufficient_material(
    ) or board.is_game_over()

def transformList():
  moves = str(board.legal_moves)
  startingMoves = int(moves.index("("))
  endingMoves = int(moves.index(")"))
  movementList = list(moves[startingMoves + 1:endingMoves].split(" "))
  print('\n Jogadas disponiveis: ')
  for move in movementList:
      print(move) 
    
def minmax(nodes, depth, alpha, beta, player):
    if(depth == 0 or endGame(board)):
        return nodes
      
    elif(player):
        melhorvalor = float('-inf')
      
        for no in nodes:
          valor = minmax(no, depth - 1, alpha, beta, False)
          melhorvalor = max(melhorvalor, valor)
          alpha = max(melhorvalor, valor)
      
        if(beta <= alpha):
          valor = 0
    else:
      valor = float('inf')

      for no in nodes:
        valor = minmax(no, depth - 1, alpha, beta, True)
        melhorvalor = min(melhorvalor, valor)
        beta = min(beta, melhorvalor)
        if(beta <= alpfa):
          valor = 0
      return valor
      
def copyBoard(fen):
  board = chess.Board(fen)
  
        
def jogadas(movimentos):
  moves = str(board.legal_moves)
  startingMoves = int(moves.index("("))
  endingMoves = int(moves.index(")"))
  movementList = list(moves[startingMoves + 1:endingMoves].split(" "))
  
  if(movimentos == 1):
    print(board.fen())
    board.push_san("e5")
    print(board.fen())
    print(board)
  elif(movimentos == 2):
    board.push_san("Nc6")
    print(board)
  else:
    movementList[1]

def Play(movimentos):
  
  
    if(not endGame()):
      if(board.is_check()):
        print("---------Check---------")

      try:
        transformList()
        movement = input("\n Digite sua jogada: ")
        board.push_san(movement)
        print(board)
        if(movimentos == 3):
          print(board.fen())
        if(movimentos == 5):
          print("Atual: ", board.fen())
      
        movimentos += 1
        print(movimentos)
        jogadas(movimentos)
        Play(movimentos)
        
      except:
          print('\n Movimento invalido, tente novamente.')
          Play(movimentos)
    else:
      #fim de jogo
      print(board)


board = chess.Board()
movimentos = 0

Play(movimentos)
