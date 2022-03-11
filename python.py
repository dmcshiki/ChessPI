import chess

def EndGame(board):
    return board.is_checkmate(
    ) or board.is_stalemate(
    ) or board.is_insufficient_material(
    ) or board.is_game_over()
  
def score(points, board):    
  if EndGame(board):
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

def max(x, y):
    if x > y:
        return x
    else:
        return y
      
def min(x, y):
    if x < y:
        return x
    else:
        return y

def transformList(board):
  moves = str(board.legal_moves)
  moves = moves.replace(",","")
  startingMoves = int(moves.index("("))
  endingMoves = int(moves.index(")"))
  movementList = list(moves[startingMoves + 1:endingMoves].split(" "))
  return list(movementList)
    
def minmax(nodes, depth, alpha, beta, player):
    boardList = CopyBoard(nodes)
    if(depth == 0 or EndGame(nodes)):
      return score(0, nodes)
      
    elif(player):
      melhorvalor = float('-inf')
            
      for no in boardList:
        valor = minmax(no, depth - 1, alpha, beta, False)
        melhorvalor = max(melhorvalor, valor)
        alpha = max(alpha, melhorvalor)
      return valor
      
    else:
      melhorvalor = float('inf')

      for no in boardList:
        valor = minmax(no, depth - 1, alpha, beta, True)
        melhorvalor = min(melhorvalor, valor)
        beta = min(beta, melhorvalor)
        
        if(beta <= alpha):
          return 0
          
      return valor
      
def CopyBoard(board):
    boardList = [] 
    movements = transformList(board)
    for i in range(len(movements)):
        boardCopy = chess.Board(board.fen())
        boardCopy.push_san(movements[i])
        boardList.append(boardCopy)
    return boardList
         
def InicialMoves(move):
  if(move == 1):
    board.push_san("e5")
  elif(move == 2):
    board.push_san("Nc6")
  elif(move == 5):
    CopyBoard(board)
  else:
    newBoard = minmax(board, 2, 0, 0, True)
    print(newBoard)
    l = input()

def Play(movimentos):    
  
    if(not EndGame(board)):
      if(board.is_check()):
        print("-----------Check--------------")
        
      if(not board.turn):
        try:
          movimentos += 1
          InicialMoves(movimentos)
        except:
          print('\n Movimento invalido IA, tente novamente.')
      else:
        try:
          print(transformList(board))
          movement = input("\n Digite sua jogada: ")
          board.push_san(movement)
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
