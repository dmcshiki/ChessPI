import chess

def endGame():
    return not board.is_checkmate(
      ) or not board.is_stalemate(
      ) or not board.is_insufficient_material(
      ) or not board.is_game_over()

def transformList():
  moves = str(board.legal_moves)
  startingMoves = int(moves.index("("))
  endingMoves = int(moves.index(")"))
  movementList = list(moves[startingMoves + 1:endingMoves].split(" "))
  print('\n Jogadas disponiveis: ')
  for move in movementList:
      print(move)

def botTurn():
    if(chess.BLACK):
        return True
    
def minmax(nodes, depth, alpha, beta, player):
    if(depth == 0 or endGame(board)):
        return nodes
    elif(botTurn()):
        float('-inf')
        #for(node in nodes)

def Play():
    
    while (endGame()):
        transformList()
        movement = input("\n Digite sua jogada: ")
        try:
            board.push_san(movement)
            print('\n', board)
          
        except:
            print('\n Movimento invalido, tente novamente.')
            Play()
        
board = chess.Board()
Play()
