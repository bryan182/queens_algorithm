def put_queen(board, row, start):

    for i in range(start):
        if board[row][i] == '*': #this meaning the algorith found a queen
            return False 

    #the queen starts in (0,0) for that reason we just check left side in search of queen
    #We are assuming there are no queens on right
    a = row
    b = start
    while a >= 0 and b >= 0:
        if board[a][b] == '*':
            return False
        a = a - 1 #If there is not a queen in the position, we move back one row
        b = b - 1 #If there is not a queen in the position, we move back one column

    c = row
    d = start
    while c < len(board) and d >= 0:
        if board[c][d] == '*':
            return False
        c = c + 1 #If there is not a queen in the position, we move one more row
        d = d - 1 #If there is not a queen in the position, we move back one column
    return True
            
def iteration_board(board, start, p_list):

    if start >= len(board):
        p_list.append([row.copy() for row in board]) #Copy of the board solution in my list
        return

    for item in range(len(board)):
        if put_queen(board, item, start):
            board[item][start] = '*'
            iteration_board(board, start + 1, p_list)
            board[item][start] = '·'

        
#Function for search all the posibilies of boards according the size
def posibilities(board, start):

    #list where we will store all the posibilities of board solutions
    posibilities_list = []

    iteration_board(board, start, posibilities_list)
    
    return posibilities_list    