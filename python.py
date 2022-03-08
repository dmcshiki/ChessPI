import chess

def endGame():
    return board.is_checkmate(
    ) or board.is_stalemate(
    ) or board.is_insufficient_material(
    ) or board.is_game_over()

def score(board):
  points = 0
  
  #Pontuação peão
  points = len(board.pieces(chess.PAWN, chess.BLACK)) - len(board.pieces(chess.PAWN, chess.WHITE))
  #Pontuação cavalo
  points += 3 * (len(board.pieces(chess.KNIGHT, chess.BLACK)) - len(board.pieces(chess.KNIGHT, chess.WHITE)))
  #Pontuação bispo
  points += 3 * (len(board.pieces(chess.BISHOP, chess.BLACK)) - len(board.pieces(chess.BISHOP, chess.WHITE)))
  #Pontuação torre
  points += 5 * (len(board.pieces(chess.ROOK, chess.BLACK)) - len(board.pieces(chess.ROOK, chess.WHITE)))
  #Pontuação rainha
  points += 9 * (len(board.pieces(chess.QUEEN, chess.BLACK)) - len(board.pieces(chess.QUEEN, chess.WHITE)))
  #Pontuação rei
  points += 100000000 * (len(board.pieces(chess.KING, chess.BLACK)) - len(board.pieces(chess.KING, chess.WHITE)))

  return points

def transformList():
  moves = str(board.legal_moves)
  startingMoves = int(moves.index("("))
  endingMoves = int(moves.index(")"))
  return list(moves[startingMoves + 1:endingMoves].split(" "))

    
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

  transformList()
  movement = input("\n Digite sua jogada IA: ")
  board.push_san(movement)
  print(board)

def Play(movimentos, IA):
  
    print(score(board))
  
    if(not endGame()):
      if(board.is_check()):
        print("---------Check---------")
        
      if(IA):
        try:
          jogadas(movimentos)
          IA = False
        except:
          Play(movimentos, IA)
      else:
        try:
          print('\n Jogadas disponiveis: ')
          move = transformList()
          for move in movementList:
            print(move) 
          movement = input("\n Digite sua jogada: ")
          board.push_san(movement)
          movimentos += 1
          IA = True
        except:
            print('\n Movimento invalido, tente novamente.')
          
      print(board)
      Play(movimentos, IA)    
    else:
      print("---------Check - Mate---------")


board = chess.Board()
movimentos = 0

Play(movimentos, False)
