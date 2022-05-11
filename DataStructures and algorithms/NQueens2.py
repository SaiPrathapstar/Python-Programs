def initialise():
    board['queen'] = {}
    board['row'] = {}
    board['col']={}
    board['dd'] = {}
    board['du'] = {}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(-(n-1) , n):
        board['dd'][i] = 0
    for i in range(2*n - 1):
        board['du'][i] = 0
def printboard():
    for i in range(n):
        print("-----"*n)
        for j in range(n):
            if ((j < board['queen'][i]) or (j > board['queen'][i])):
                print("    |",end="")
            if board['queen'][i] == j:
                print("  ",end="")
                print(board['queen'][i] + 1,end="")
                print(" |",end="")
        print()
    print("-----"*n)
def printboard2():
    for row in sorted(board['queen'].keys()):
        print(board['queen'][row] + 1 , end = "  ")
    print()
def free(i,j):
    return(board['row'][i] == 0 and board['col'][j] == 0 and board['dd'][j-i] == 0 and board['du'][i+j] == 0)
def addqueen(i,j):
    board['queen'][i] = j
    board['row'][i] = 1
    board['col'][j] = 1
    board['dd'][j-i] = 1
    board['du'][j+i ] = 1
def undoqueen(i,j):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['dd'][j-i] = 0
    board['du'][j+i] = 0
def placequeen(i):
    global count
    global n
    for j in range(n):
        if free(i,j):
            addqueen(i, j)
            if i == n-1:
                count+=1
                #printboard2()
                #The above line prints the solutions numericlly
                printboard()
                #The above line prints the solutions pictorially
            else:
                placequeen(i+1)
                #printboard()
                #uncomment the above line to see the problem solving
            undoqueen(i,j)
board = {}
count = 0
n = int(input("How many queens?  "))
initialise()
placequeen(0)
print(f"Total solutions = {count}")