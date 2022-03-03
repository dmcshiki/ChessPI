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
  print('Jogadas disponiveis: ')
  for move in movementList:
      print(move)


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
