import chess

def endGame():
    return board.is_checkmate(
    ) or board.is_stalemate(
    ) or board.is_insufficient_material(
    ) or board.is_game_over()

def score(points):    
  if endGame():
    if(board.is_checkmate()):
      if(board.turn):
        points += 10000 
      else:
        points -= 10000 
    else:
      points -= 5000 
  else:
    #Pontuação peão
    points += len(board.pieces(chess.PAWN, chess.BLACK)) - len(board.pieces(chess.PAWN, chess.WHITE))
    #Pontuação cavalo
    points += 3 * (len(board.pieces(chess.KNIGHT, chess.BLACK)) - len(board.pieces(chess.KNIGHT, chess.WHITE)))
    #Pontuação bispo
    points += 3 * (len(board.pieces(chess.BISHOP, chess.BLACK)) - len(board.pieces(chess.BISHOP, chess.WHITE)))
    #Pontuação torre
    points += 5 * (len(board.pieces(chess.ROOK, chess.BLACK)) - len(board.pieces(chess.ROOK, chess.WHITE)))
    #Pontuação rainha
    points += 9 * (len(board.pieces(chess.QUEEN, chess.BLACK)) - len(board.pieces(chess.QUEEN, chess.WHITE)))
    #Pontuação chequeMate
     
  return points

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
        return 0
        
    else:
      valor = float('inf')

      for no in nodes:
        valor = minmax(no, depth - 1, alpha, beta, True)
        melhorvalor = min(melhorvalor, valor)
        beta = min(beta, melhorvalor)
        
        if(beta <= alpfa):
          return 0
          
    return valor
      
def copyBoard(fen):
  board = chess.Board(fen)
          
def jogadas(movimentos):
  transformList()
  movement = input("\n Digite sua jogada IA: ")
  board.push_san(movement)

def Play(movimentos):  
    print(score(points))
  
    if(not endGame()):
      if(board.is_check()):
        print("-----------Check--------------")
        
      if(not board.turn):
        try:
          jogadas(movimentos)
        except:
          print('\n Movimento invalido, tente novamente.')
      else:
        try:
          transformList()
          movement = input("\n Digite sua jogada: ")
          board.push_san(movement)
          movimentos += 1
        except:
            print('\n Movimento invalido, tente novamente.')
          
      print(board)
      Play(movimentos)    
    else:
      if board.is_checkmate():
        print("-----------Check Mate---------")
      else:
        print("-----------Game Over----------")

points = 0
board = chess.Board()
movimentos = 0
Play(movimentos)
