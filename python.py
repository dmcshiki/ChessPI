import chess
import chess.engine


def EndGame():
    return board.is_checkmate(
    ) or board.is_stalemate(
    ) or board.is_insufficient_material(
    ) or board.is_game_over()
  
def score(points):    
  if EndGame():
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
  return list(movementList)
    
def Minmax(nodes, depth, alpha, beta, player):
    if(depth == 0 or EndGame(board)):
        return nodes
    elif(player):
        melhorvalor = float('-inf')
      
        for no in nodes:
          valor = Minmax(no, depth - 1, alpha, beta, False)
          melhorvalor = max(melhorvalor, valor)
          alpha = max(melhorvalor, valor)
      
        if(beta <= alpha):
          valor = 0
    print('\n Jogadas disponiveis: ')
    for move in transformList():
      print(move)

def minmax(nodes, depth, alpha, beta, player):
    if(depth == 0 or EndGame(board)):
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
        valor = Minmax(no, depth - 1, alpha, beta, True)
        melhorvalor = min(melhorvalor, valor)
        beta = min(beta, melhorvalor)
<<<<<<< HEAD
        if(beta <= alpha):
          valor = 0
      return valor
=======
        
        if(beta <= alpha):
          return 0
          
    return valor
>>>>>>> 268d7f663784de8c5ef8432732d61c320dc40afd
      
def CopyBoard(board):
    boardCopy = chess.Board(board.fen())
    boardList = [] 
    movements = transformList()
    for i in range(len(movements)):
        boardCopy = chess.Board(board.fen())
        boardList.append(boardCopy)
        boardList[0] = 
    return boardList
         
def InicialMoves(move):
  moves = str(board.legal_moves)
  startingMoves = int(moves.index("("))
  endingMoves = int(moves.index(")"))
  movementList = list(moves[startingMoves + 1:endingMoves].split(" "))
  
  if(move == 1):
    board.push_san("e5")
  elif(move == 2):
    board.push_san("Nc6")
    print(board)
  else:
    movementList[1]

def copyBoard(fen):
  board = chess.Board(fen)
          
def jogadas(movimentos):
  transformList()
  movement = input("\n Digite sua jogada IA: ")
  board.push_san(movement)

def Play(movimentos):  
    print(score(points))
  
    if(not EndGame()):
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