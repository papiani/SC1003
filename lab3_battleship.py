# this is basically the battleship game

# build boards
    # 10x10 board, tuple is (depth0,depth1)
def build_board():
    board = []
    print("building board")
    for i in range(10):
        board.append([])
        for x in range(10):
            board[i].append(('0','0'))
    return board

# prettyprint for board
def show_board(board):
    line = ""
    for row in board:
        print(row)
def censorprint(board):
    tempy = []
    rowindex = -1
    for i in range(10):
        tempy.append([])
    for row in board:
        rowindex+=1
        for item in row:
            i,j = item
            if i in ['x','0']:
                pass
            else:
                i='0'
            if j in ['x','0']:
                pass
            else:
                j='0'
            tempy[rowindex].append((i,j))
    show_board(tempy)
            
        

# def moves
    # def shoot
        #changes value of "slot" from S for submarine or C for carrier to X
def shoot(board,row,column):
    print("shots fired")
    i,j=board[row][column]
    if i is not '0':
        board[row][column] = ('x',j)
        return True
    elif j is not '0':
        board[row][column] = (i,'x')
    else:
        board[row][column] = ('x','x')

    # def place
def place(board, ori, row, column,obj,depth):
    (depth0,depth1)=board[row][column]
    if obj == 's':
        length = 3
    elif obj =='c':
        length = 4
    if ori == "u":
        for i in range(length):
            (x,y) = board[row+i][column]
            if depth == 0:
                x = obj
                board[row+i][column]=(x,y)
            if depth == 1:
                y = obj
                board[row+i][column]=(x,y)
    if ori == "d":
        for i in range(length):
            (x,y) = board[row-i][column]
            if depth == 0:
                x = obj
                board[row+i][column]=(x,y)
            if depth == 1:
                y = obj
                board[row+i][column]=(x,y)
    if ori == "l":
        for i in range(length):
            (x,y) = board[row][column-i]
            if depth == 0:
                x = obj
                board[row][column-i] = (x,y)
            if depth == 1:
                y = obj
                board[row][column-i] = (x,y)
    if ori == "r":
        for i in range(length):
            (x,y) = board[row][column+i]
            if depth == 0:
                x = obj
                board[row][column+i] = (x,y)
            if depth == 1:
                y = obj
                board[row][column+i] = (x,y)




    # plan placement of object

# def checkover
    #iterate through both board and see if any 'S'or 'C' are still left
    # if a board has none,print(board has lost),return True
def checkover(board):
    for row in board:
        for i,j in row:
            if i in ['s','c']:
                return False
            elif j in ['s','c']:
                return False
    else:
        return True

def play_turn(boardself,boardopp):
    # if board is empty, prompt for placement of subs and carriers
    empty = checkover(boardself)
    if empty:
        print("LETS PLACE SOME PIECES ON THE BOARD")
        x = "continue"
        while x is not "exit":
            ui = input('enter s to place submarine, c for carrier')
            row = int(input("which row?")) # add this stuff later
            column = int(input("which column?"))
            depth = int(input("what depth?"))
            place(boardself,ui,row,column,depth)
    else:
        print('my board')
        show_board(boardself)
        print('target board')
        censorprint(boardopp)

    # shoot coords
    # hit/miss feedback
    # return board
# following code is to demnstrate board
board = build_board()
show_board(board)
place(board,'r',5,5,'s',1)
show_board(board)
shoot(board,5,5)
shoot(board,1,1)
censorprint(board)
# main game
    # initialise players
        # build boards for players
    # player 1's turn to place submarines and ships
        # use input() and get user input
        # use place(obj,row,column,player_1_board) to place objcts
    # repeat for player2 or randomise for computer
    # game_over=False
    # While game_over is not True:
        #game_over = checkover([board1,board2])
        #play_turn(player1)
        #play_turn(player2)

