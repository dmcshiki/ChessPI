import asyncio
import chess
import chess.engine


def EndGame():
    return board.is_checkmate(
    ) or board.is_stalemate(
    ) or board.is_insufficient_material(
    ) or board.is_game_over()

def MovementList():
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
    else:
      valor = float('inf')

      for no in nodes:
        valor = Minmax(no, depth - 1, alpha, beta, True)
        melhorvalor = min(melhorvalor, valor)
        beta = min(beta, melhorvalor)
        if(beta <= alpha):
          valor = 0
      return valor
      
def CopyBoard(board):
    boardCopy = chess.Board(board.fen())
    boardList = [] 
    movements = MovementList()
    for i in range(len(movements)):
        boardList.append(boardCopy)
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


    

def Play(board, move):
    
    listBoards = CopyBoard(board)
    print(listBoards)
    
    if(not EndGame()):
      if(board.is_check()):
        print("---------Check---------")

      try:
        move += 1
        MovementList()
        movement = input("\n Digite sua jogada: ")
        board.push_san(movement)
        print(board)
        InicialMoves(move)
        Play(board, move)
        
      except:
          print('\n Movimento invalido, tente novamente.')
          Play(board, move)
    else:
      #fim de jogo
      print(board)


board = chess.Board()
move = 0

Play(board, move)