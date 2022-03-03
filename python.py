import chess

def botTurn():
    if(chess.BLACK):
        return True

def minmax(nodes, depth, alpha, beta, player):
    if(depth == 0 or endGame(board)):
        return nodes
    elif(botTurn()):
        float('-inf')
        for(node in nodes)
        
        

def endGame(board):
    if(not board.is_checkmate() or not board.is_stalemate() 
    or not board.is_insufficient_material()
    or not board.is_game_over()):    
        return False
    else: 
        return True

def Play(board):

    while(not endGame(board)):
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

board = chess.Board()
Play(board)

