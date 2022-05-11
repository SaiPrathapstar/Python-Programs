def initialize(board , n):
    board['queen']={}
    board['row'] = {}
    board['col'] = {}
    board['Down'] = {}
    board['Up'] = {}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(-(n-1) , n):
        board['Down'][i] = 0
    for i in range(2*n - 1):
        board['Up'][i] = 0
def printboard(board):
    for row in sorted(board['queen'].keys()):
        print(board['queen'][row] + 1 , end = "  ")
def free(i,j,board):
    return (board['row'][i] == 0 and board['col'][j] == 0 and board['Down'][j-i] == 0 and board['Up'][i+j] == 0)
def addqueen(i,j,board):
    board['queen'][i] = j
    board['row'][i] = 1
    board['col'][j] = 1
    board['Down'][j-i] = 1
    board['Up'][j+i] = 1
def undoqueen(i,j,board):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['Down'][j-i] = 0
    board['Up'][i+j] = 0
def placequeen(i,board):
    n = len(board['queen'].keys())
    for j in range(n):
        if free(i,j,board):
            addqueen(i, j, board)
            if i == n-1:
                return (True)
            else:
                extendsoln = placequeen(i+1, board)
            if extendsoln:
                return (True)
            else:
                undoqueen(i, j, board)
    else:
        return (False)
board = {}
n = int(input("How many Queens?  "))
initialize(board, n)
if placequeen(0, board):
    printboard(board)