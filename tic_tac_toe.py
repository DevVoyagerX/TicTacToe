from random import choice

board = [
    ['_','_','_'],
    ['_','_','_'], ['_','_','_'], ] 

humanPlayer = 'x'
aiplayer = 'o'

def checkwin(option):
    for i in range(0,3):
        

        if all(cell == option for cell in board[i]) or all(board[j][i] == option for j in range(0,3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == option or board[0][2] == board[1][1] == board[2][0] == option:
        return True
    

def makemove(row,col,player):
    if is_move_valid:
        board[row][col] = player


def isGameover():


    return checkwin(option='x') or checkwin(option='o') or all("_" not in row for row in board)



def minmax(depth,maximizing_player):
    if checkwin(humanPlayer):
       return -1
    elif checkwin(aiplayer):
       return 1
    elif isGameover():
        return 0
    elif maximizing_player:
        best_score = float('-inf')
        for row in range(0,3):
            for col in range(0,3):
                    if is_move_valid(row,col):
                        board[row][col] = 'o'
                        score = minmax(depth+1,False)
                        board[row][col] = '_'
                        best_score = max(score,best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(0,3):
            for col in range(0,3):
                    if is_move_valid(row,col):
                        board[row][col] = 'x'
                        score = minmax(depth+1,True)
                        board[row][col] = '_'
                        best_score = min(score,best_score)
        return best_score


def is_move_valid(row,col):
    return board[row][col] == '_'


def findbestmove():
    bestScore = float('-inf') 
    bestmove = None 
    for row in range(0,3):
        for col in range(0,3):
            if is_move_valid(row,col):
                board[row][col] = 'o'
                score = minmax(0,False)
                board[row][col] = '_'
                if score > bestScore:
                    bestScore = score
                    bestmove = (row,col)
    return bestmove



        

def play_game() -> None:
    current_player = 'x'
    print(*board,sep='\n')
    while not isGameover():
        if current_player == 'x':
            row,col = map(int,input('Enter row and column').split(','))
            row,col = row-1,col-1
        
        else:
            row,col = findbestmove()
            print('AI playing')
        if is_move_valid(row,col):
            makemove(row,col,current_player)
            print(*board,sep='\n')
            if checkwin(current_player):
                print(f'{current_player} winns')
                break

            current_player = 'o' if current_player == "x" else "x"
        else:
            print('Invalid move')
    else:
        print('Draw')

play_game()