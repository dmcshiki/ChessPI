import chess

def EndGame(board):
    return board.is_checkmate(
    ) or board.is_stalemate(
    ) or board.is_insufficient_material(
    ) or board.is_game_over()
  
def score(points, board):    
  if EndGame(board):
    #Pontuação chequeMate
    if(board.is_checkmate()):
      if(board.turn):
        points += 10000 
      else:
        points -= 10000 
    else:
      #Pontuação Empate
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
     
  return points

def TransformList(board):
  moves = str(board.legal_moves)
  moves = moves.replace(",","")
  startingMoves = int(moves.index("("))
  endingMoves = int(moves.index(")"))
  movementList = list(moves[startingMoves + 1:endingMoves].split(" "))
  return list(movementList)
  
def MinMax_AlphaBeta(nodes, player, depth = 8, alpha = float("-inf"), beta = float("inf")):
  mov = nodes
  
  if(depth == 0 or EndGame(nodes)):
    return score(0, nodes), nodes

  if player:
    for no in CopyBoard(nodes):
      value, mov = MinMax_AlphaBeta(no, False, depth - 1, alpha, beta)
      alpha = max(value, alpha)
      if beta <= alpha:
        break
      return alpha, no
  else:
    for no in CopyBoard(nodes):
      value, mov = MinMax_AlphaBeta(no, True, depth - 1, alpha, beta)
      beta = min(value, beta)
      if beta <= alpha:
        break
      return beta, no

def FindMovement():
  #so I find wicth moviment will make this score
  value, mov =  MinMax_AlphaBeta(board, True)
  print("\n",value,"\n",mov,"\n")
  
  for i in CopyBoard(board):
    boardCopy = chess.Board(board.fen())
    print(TransformList(board))
    boardCopy.push_san(movements[i])
    if mov == boardCopy:
      movement = movements[i]
      print(movement)
      
  l = input()
  
def CopyBoard(board):
    boardList = [] 
    movements = TransformList(board)
    for i in range(len(movements)):
        boardCopy = chess.Board(board.fen())
        boardCopy.push_san(movements[i])
        boardList.append(boardCopy)
    return boardList
         
def InicialMoves(move):
  #if move == 1:
  #  board.push_san("e5")
  #elif move == 2:
  #  board.push_san("Nf6")
  #elif move == 3:
  #  board.push_san("Bc5")
  #elif move == 4:
  #  board.push_san("d6")
  #else:
    FindMovement()

#def jogadas():
  #print(TransformList(board))
  #movement = input("\n Digite sua jogada IA: ")
  #board.push_san(movement)

def Play(movimentos):    
    if not EndGame(board):
      if board.is_check():
        print("-----------Check--------------")
        
      if not board.turn:
        #try:
          InicialMoves(movimentos)
          movimentos += 1
        #except:
          #print('\n Movimento invalido IA, tente novamente.')
      else:
        try:
          print(TransformList(board))
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
board = chess.Board("K7/3r4/8/8/3kr3/8/8/8 w - - 4 45")
movimentos = 1
Play(movimentos)
