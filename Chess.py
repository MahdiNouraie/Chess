class bcolors:
    HEADER = '\033[95m' #بنفش
    OKBLUE = '\033[94m' #آبی
    OKCYAN = '\033[96m' # آبی فیروزه‌ای
    OKGREEN = '\033[92m' #سبز
    WARNING = '\033[93m' #زرد
    FAIL = '\033[91m' #قرمز
    ENDC = '\033[0m' #اتمام اعمال رنگ 
    BOLD = '\033[1m' # پررنگ 
    UNDERLINE = '\033[4m' # زیرخط دار

# lowercase for player black
# UPPERCASE for player white

def printHeader(color = bcolors.ENDC):
    print(color + " --- ", end='')

def printBox(iplusj = 0, marble = ' '):
    color = bcolors.ENDC
    if iplusj == 0:
        color = bcolors.OKBLUE
    if (marble <= 'z') and (marble >= 'a'):
        marble = chr(ord(marble) - ord('a') + ord('A'))
        print(color + "| "+ bcolors.ENDC + marble + color + " |", end= '') 
    else:
        print(color + "| "+ bcolors.OKBLUE + marble + color + " |", end= '')

def printChessBoard(board):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                printHeader(bcolors.OKBLUE)
            else:
                printHeader()
        print()
        for j in range(8):
            printBox((i + j) % 2, board[i][j])
        print()
        for j in range(8):
            if (i + j) % 2 == 0:
                printHeader(bcolors.OKBLUE)
            else:
                printHeader()
        print()

def startingPosition():
    print(bcolors.OKGREEN + "You are now choosing the starting position.")
    
    x = ""
    while True:
        print(bcolors.OKGREEN + "\tEnter the number of the row: ", end = '')
        x = input().strip()
        if not x.isdigit():
            print(bcolors.FAIL + "\tYour input is not a number! try again.")
            continue
        if int(x) > 8 or int(x) < 1:
            print(bcolors.FAIL + "\tYour number is out of the range of the board! try again.")
            continue
        break
    
    y = ""
    while True:
        print(bcolors.OKGREEN + "\tEnter the number of the column: ", end = '')
        y = input().strip()
        if not y.isdigit():
            print(bcolors.FAIL + "\tYour input is not a number! try again.")
            continue
        if int(y) > 8 or int(y) < 1:
            print(bcolors.FAIL + "\tYour number is out of the range of the board! try again.")
            continue
        break
    return [int(x) - 1, int(y) - 1]

def finishingPosition():
    print(bcolors.OKGREEN + "You are now choosing the finishing position.")
    
    x = ""
    while True:
        print(bcolors.OKGREEN + "\tEnter the number of the row: ", end = '')
        x = input().strip()
        if not x.isdigit():
            print(bcolors.FAIL + "\tYour input is not a number! try again.")
            continue
        if int(x) > 8 or int(x) < 1:
            print(bcolors.FAIL + "\tYour number is out of the range of the board! try again.")
            continue
        break
    
    y = ""
    while True:
        print(bcolors.OKGREEN + "\tEnter the number of the column: ", end = '')
        y = input().strip()
        if not y.isdigit():
            print(bcolors.FAIL + "\tYour input is not a number! try again.")
            continue
        if int(y) > 8 or int(y) < 1:
            print(bcolors.FAIL + "\tYour number is out of the range of the board! try again.")
            continue
        break
    return [int(x) - 1, int(y) - 1]

def player1(C):
    if C >= 'a' and C <= 'z':
        return True
    return False

def player2(C):
    if C >= 'A' and C <= 'Z':
        return True
    return False

def existIJ(x, y):
    if x > 7 or x < 0 or y > 7 or y < 0:
        return False
    return True

def rook(x, y, X, Y, board):
    for i in range(1, 8):
        if x + i == X and y == Y:
            return True
        if (not existIJ(x + i, y)) or board[x + i][y] != ' ':
            break

    for i in range(1, 8):
        if x == X and y + i == Y:
            return True
        if (not existIJ(x, y + i)) or board[x][y + i] != ' ':
            break

    for i in range(1, 8):
        if x - i == X and y == Y:
            return True
        if (not existIJ(x - i, y)) or board[x - i][y] != ' ':
            break

    for i in range(1, 8):
        if x == X and y - i == Y:
            return True
        if (not existIJ(x, y - i)) or board[x][y - i] != ' ':
            break
    
    return False

def bishop(x, y, X, Y, board):
    for i in range(1, 8):
        if x + i == X and y + i == Y:
            return True
        if (not existIJ(x + i, y + i)) or board[x + i][y + i] != ' ':
            break

    for i in range(1, 8):
        if x + i == X and y - i == Y:
            return True
        if (not existIJ(x + i, y - i)) or board[x + i][y - i] != ' ':
            break

    for i in range(1, 8):
        if x - i == X and y + i == Y:
            return True
        if (not existIJ(x - i, y + i)) or board[x - i][y + i] != ' ':
            break

    for i in range(1, 8):
        if x - i == X and y - i == Y:
            return True
        if (not existIJ(x - i, y - i)) or board[x - i][y - i] != ' ':
            break
    
    return False

def queen(x, y, X, Y, board):
    return bishop(x, y, X, Y, board) or rook(x, y, X, Y, board)

def knight(x, y, X, Y, board):
    if x + 2 == X and y + 1 == Y:
        return True
    if x + 2 == X and y - 1 == Y:
        return True
    if x - 2 == X and y + 1 == Y:
        return True
    if x - 2 == X and y - 1 == Y:
        return True
    
    if x + 1 == X and y + 2 == Y:
        return True
    if x + 1 == X and y - 2 == Y:
        return True
    if x - 1 == X and y + 2 == Y:
        return True
    if x - 1 == X and y - 2 == Y:
        return True

    return False

def check(x, y, board, turn):
    for i in range(8):
        for j in range(8):
            if (i == x and j == y) or (board[i][j] == ' ') or (turn == 1 and player1(board[i][j])) or (turn == 2 and player2(board[i][j])):
                continue

            if (board[i][j] == 'q' or board[i][j] == 'Q') and queen(i, j, x, y, board):
                return True
            
            if (board[i][j] == 'b' or board[i][j] == 'B') and bishop(i, j, x, y, board):
                return True
             
            if (board[i][j] == 'r' or board[i][j] == 'R') and rook(i, j, x, y, board):
                return True
            
            if (board[i][j] == 'n' or board[i][j] == 'N') and knight(i, j, x, y, board):
                return True
            
            if (board[i][j] == 'p' and x - i == -1 and abs(y - j) == 1) or (board[i][j] == 'P' and x - i == 1 and abs(y - j) == 1):
                return True
    
    return False

def checkmate(board, turn):
    x = y = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'k' and turn == 1:
                x = i
                y = j
            if board[i][j] == 'K' and turn == 2:
                x = i
                y = j
    
    if not check(x, y, board, turn):
        return False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if existIJ(x + i, y + j) and not ((turn == 1 and player1(board[x + i][y + j])) or (turn == 2 and player2(board[x + i][y + j]))) and not check(x + i, y + j, board, turn) and (board[x + i][y + j] != 'K' and board[x + i][y + j] != 'k'):
                return False
    
    pieces = 0
    PCBP = 0
    for i in range(8):
        for j in range(8):
            if (i == x and j == y) or (board[i][j] == ' ') or (turn == 1 and player1(board[i][j])) or (turn == 2 and player2(board[i][j])):
                continue

            if (board[i][j] == 'q' or board[i][j] == 'Q') and queen(i, j, x, y, board):
                pieces += 1
                if check(i, j, board, 3 - turn):
                    PCBP += 1
            
            if (board[i][j] == 'b' or board[i][j] == 'B') and bishop(i, j, x, y, board):
                pieces += 1
                if check(i, j, board, 3 - turn):
                    PCBP += 1
             
            if (board[i][j] == 'r' or board[i][j] == 'R') and rook(i, j, x, y, board):
                pieces += 1
                if check(i, j, board, 3 - turn):
                    PCBP += 1
            
            if (board[i][j] == 'n' or board[i][j] == 'N') and knight(i, j, x, y, board):
                pieces += 1
                if check(i, j, board, 3 - turn):
                    PCBP += 1
            
            if (board[i][j] == 'p' and x - i == -1 and abs(y - j) == 1) or (board[i][j] == 'P' and x - i == 1 and abs(y - j) == 1):
                pieces += 1
                if check(i, j, board, 3 - turn):
                    PCBP += 1
    if pieces == 0 or (pieces == 1 and PCBP == 1):
        return False
    return True

def ifPlayerXisChecked(board, turn):
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == 'k' and check(i, j, board, 1):
                if turn == 1:
                    return True
                if turn == 2:
                    return False
            if board[i][j] == 'K' and check(i, j, board, 2):
                if turn == 2:
                    return True
                if turn == 1:
                    return False
    return False

board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

firstMove = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

turn = 1

while True:
    printChessBoard(board)
    
    if checkmate(board, 1):
        print(bcolors.OKCYAN + "Checkmate!\nWinner ----> Black!\n")
        break
    if checkmate(board, 2):
        print(bcolors.OKCYAN + "Checkmate!\nWinner ----> White!\n")
        break
    
    posStart = []
    while True:
        posStart = startingPosition()
        x = posStart[0]
        y = posStart[1]
    
        if board[x][y] == ' ':
            print(bcolors.FAIL + "The selected cell is not occupied with any pieces! try again.")
            continue
    
        if board[x][y] <= 'Z' and board[x][y] >= 'A' and turn == 1:
            print(bcolors.FAIL + "Please only choose white pieces. so try another cell.")
            continue
        if board[x][y] <= 'z' and board[x][y] >= 'a' and turn == 2:
            print(bcolors.FAIL + "Please only choose black pieces. so try another cell.")
            continue
    
        break
    
    posFinish = []
    while True:
        posFinish = finishingPosition()
        x = posFinish[0]
        y = posFinish[1]

        if board[x][y] <= 'Z' and board[x][y] >= 'A' and turn == 2:
            if (board[x][y] == 'K' and board[posStart[0]][posStart[1]] == 'R') or (board[x][y] == 'R' and board[posStart[0]][posStart[1]] == 'K'):
                if firstMove[x][y] * firstMove[posStart[0]][posStart[1]] == 0 or ifPlayerXisChecked(board, turn):
                    print(bcolors.FAIL + "You can't castle!")
                    continue
                if y == 7 or posStart[1] == 7:
                    if not (board[7][6] == ' ' and board[7][5] == ' '):
                        print(bcolors.FAIL + "You can't castle!")
                        continue
                    else :
                        board[7][7] = ' '
                        board[7][6] = 'K'
                        board[7][5] = 'R'
                        board[7][4] = ' '
                        firstMove[7][4] = 0
                        firstMove[7][7] = 0
                        if ifPlayerXisChecked(board, turn):
                            board[7][7] = 'R'
                            board[7][6] = ' '
                            board[7][5] = ' '
                            board[7][4] = 'K'
                            firstMove[7][4] = 1
                            firstMove[7][7] = 1
                            print(bcolors.FAIL + "You can't castle!")
                            continue
                    castle = 1
                    break
                if y == 0 or posStart[1] == 0:
                    if not (board[7][1] == ' ' and board[7][2] == ' ' and board[7][3] == ' '):
                        print(bcolors.FAIL + "You can't castle!")
                        continue
                    else :
                        board[7][0] = ' '
                        board[7][1] = ' '
                        board[7][2] = 'K'
                        board[7][3] = 'R'
                        board[7][4] = ' '
                        firstMove[7][0] = 0
                        firstMove[7][4] = 0
                        if ifPlayerXisChecked(board, turn):
                            board[7][0] = 'R'
                            board[7][1] = ' '
                            board[7][2] = ' '
                            board[7][3] = ' '
                            board[7][4] = 'K'
                            firstMove[7][0] = 1
                            firstMove[7][4] = 1
                            print(bcolors.FAIL + "You can't castle!")
                            continue
                    castle = 1
                    break
            print(bcolors.FAIL + "Please only choose white pieces. so try another cell.")
            continue
        if board[x][y] <= 'z' and board[x][y] >= 'a' and turn == 1:
            if (board[x][y] == 'k' and board[posStart[0]][posStart[1]] == 'r') or (board[x][y] == 'r' and board[posStart[0]][posStart[1]] == 'k'):
                if firstMove[x][y] * firstMove[posStart[0]][posStart[1]] == 0 or ifPlayerXisChecked(board, turn):
                    print(bcolors.FAIL + "You can't castle!")
                    continue
                if y == 7 or posStart[1] == 7:
                    if not (board[0][6] == ' ' and board[0][5] == ' '):
                        print(bcolors.FAIL + "You can't castle!")
                        continue
                    else :
                        board[0][7] = ' '
                        board[0][6] = 'k'
                        board[0][5] = 'r'
                        board[0][4] = ' '
                        firstMove[0][4] = 0
                        firstMove[0][7] = 0
                        if ifPlayerXisChecked(board, turn):
                            board[0][7] = 'r'
                            board[0][6] = ' '
                            board[0][5] = ' '
                            board[0][4] = 'k'
                            firstMove[0][4] = 1
                            firstMove[0][7] = 1
                            print(bcolors.FAIL + "You can't castle!")
                            continue
                    castle = 1
                    break
                if y == 0 or posStart[1] == 0:
                    if not (board[0][1] == ' ' and board[0][2] == ' ' and board[0][3] == ' '):
                        print(bcolors.FAIL + "You can't castle!")
                        continue
                    else :
                        board[0][0] = ' '
                        board[0][1] = ' '
                        board[0][2] = 'k'
                        board[0][3] = 'r'
                        board[0][4] = ' '
                        firstMove[0][0] = 0
                        firstMove[0][4] = 0
                        if ifPlayerXisChecked(board, turn):
                            board[0][0] = 'r'
                            board[0][1] = ' '
                            board[0][2] = ' '
                            board[0][3] = ' '
                            board[0][4] = 'k'
                            firstMove[0][0] = 1
                            firstMove[0][4] = 1
                            print(bcolors.FAIL + "You can't castle!")
                            continue
                    castle = 1
                    break
            print(bcolors.FAIL + "Please only choose black pieces. so try another cell.")
            continue
    
        break
    
    if (board[posStart[0]][posStart[1]] == 'q' or board[posStart[0]][posStart[1]] == 'Q') and not queen(posStart[0], posStart[1], posFinish[0], posFinish[1], board):
        print(bcolors.FAIL + "Queen can not get to the finishing cell! try another cell.")
        continue
    
    if (board[posStart[0]][posStart[1]] == 'b' or board[posStart[0]][posStart[1]] == 'B') and not bishop(posStart[0], posStart[1], posFinish[0], posFinish[1], board):
        print(bcolors.FAIL + "Bishop can not get to the finishing cell! try another cell.")
        continue

    if (board[posStart[0]][posStart[1]] == 'r' or board[posStart[0]][posStart[1]] == 'R') and not rook(posStart[0], posStart[1], posFinish[0], posFinish[1], board):
        print(bcolors.FAIL + "Rook can not get to the finishing cell! try another cell.")
        continue

    if (board[posStart[0]][posStart[1]] == 'n' or board[posStart[0]][posStart[1]] == 'N') and not knight(posStart[0], posStart[1], posFinish[0], posFinish[1], board):
        print(bcolors.FAIL + "Knight can not get to the finishing cell! try another cell.")
        continue
    
    if (board[posStart[0]][posStart[1]] == 'k' or board[posStart[0]][posStart[1]] == 'K') and not ((abs(posFinish[0] - posStart[0]) <= 1) and (abs(posFinish[1] - posStart[1]) <= 1)):
        print(bcolors.FAIL + "King can not get to the finishing cell! try another cell.")
        continue

    if (board[posStart[0]][posStart[1]] == 'p' and not ((board[posFinish[0]][posFinish[1]] == ' ' and posFinish[1] - posStart[1] == 0 and ((firstMove[posStart[0]][posStart[1]] == 1 and posFinish[0] - posStart[0] == 2) or posFinish[0] - posStart[0] == 1)) or (board[posFinish[0]][posFinish[1]] != ' ' and abs(posFinish[1] - posStart[1]) == 1 and posFinish[0] - posStart[0] == 1))) or (board[posStart[0]][posStart[1]] == 'P' and not ((board[posFinish[0]][posFinish[1]] == ' ' and posFinish[1] - posStart[1] == 0 and ((firstMove[posStart[0]][posStart[1]] == 1 and posFinish[0] - posStart[0] == -2) or posFinish[0] - posStart[0] == -1)) or (board[posFinish[0]][posFinish[1]] != ' ' and abs(posFinish[1] - posStart[1]) == 1 and posFinish[0] - posStart[0] == -1))):
        print(bcolors.FAIL + "Pawn can not get to the finishing cell! try another cell.")
        continue
    
    Check = ifPlayerXisChecked(board, turn)
    C = board[posFinish[0]][posFinish[1]]
    board[posFinish[0]][posFinish[1]] = board[posStart[0]][posStart[1]]
    board[posStart[0]][posStart[1]] = ' '

    if Check == 1 and ifPlayerXisChecked(board, turn):
        print(bcolors.WARNING + "The selected move won't get you out of a checked positon so try another move!")
        board[posStart[0]][posStart[1]] = board[posFinish[0]][posFinish[1]] 
        board[posFinish[0]][posFinish[1]] = C
        continue

    if ifPlayerXisChecked(board, turn):
        print(bcolors.WARNING + "The selected move will get you in a checked positon so try another move!")
        board[posStart[0]][posStart[1]] = board[posFinish[0]][posFinish[1]] 
        board[posFinish[0]][posFinish[1]] = C
        continue
    
    if (board[posFinish[0]][posFinish[1]] == 'p' and posFinish[0] == 7) or (board[posFinish[0]][posFinish[1]] == 'P' and posFinish[0] == 0):
        print(bcolors.OKGREEN + "Now type a character denoting the piece you want to change with your Pawn:")
        while True:
            print(bcolors.WARNING + "   For Queen, Bishop, Knight, Rook type in order Q, B, K, R: ", end = '')
            C = input().strip()
            if len(C) > 1 or len(C) == 0:
                print(bcolors.FAIL + "Type a character!")
                continue
            if C == 'Q':
                if board[posFinish[0]][posFinish[1]] == 'p':
                    board[posFinish[0]][posFinish[1]] = 'q'
                else:
                    board[posFinish[0]][posFinish[1]] = 'Q'
            elif C == 'B':
                if board[posFinish[0]][posFinish[1]] == 'p':
                    board[posFinish[0]][posFinish[1]] = 'b'
                else:
                    board[posFinish[0]][posFinish[1]] = 'B'
            elif C == 'K':
                if board[posFinish[0]][posFinish[1]] == 'p':
                    board[posFinish[0]][posFinish[1]] = 'k'
                else:
                    board[posFinish[0]][posFinish[1]] = 'K'
            elif C == 'R':
                if board[posFinish[0]][posFinish[1]] == 'p':
                    board[posFinish[0]][posFinish[1]] = 'r'
                else:
                    board[posFinish[0]][posFinish[1]] = 'R'
            else:
                print(bcolors.FAIL + "Enter one of the given characters!")
                continue
            break
    
    turn = 3 - turn