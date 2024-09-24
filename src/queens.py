import pytest
from database import insert_boards, exist_solutions, solutions_count, get_boards
from algorithm import posibilities

#Set matrix with size giving for the user
def matriz_size():
    print("Eight Queen puzzle")
    size = int(input("What size do you want your board? "))
    print(f"Your board is: {size} X {size}")
    return size


#empty board creation
def board_generator(rows, columns):
    board = []

    for rows_index in range(rows):
        row = []
        for columns_index in range(columns):
            value = '·'
            row.append(value)
        board.append(row)
    return board


def print_board(board):
    for row in board:
        print(" | ".join(map(str, row))) #Convert element to text
        print("-" * (len(row) * 4 - 1 )) #lenght of separator


def boards_stored(rows_as_lists):
    for row_list in rows_as_lists:
        for row in row_list:
            print("\n")
            print_board(row)

def main():

    #Ask to the user board size
    size = matriz_size()
    
    #If the solution is in database already, It can't saved it 
    #we don't need execute all funtions if the solutions already exists
    if exist_solutions(size):
        print("This solution is stored in database!")  

        solutions = solutions_count(size)

        print(f"For that size there are: {solutions} solutions")       

        boards_stored(get_boards(size))

    else:
        #board generator according the size of parameter
        board = board_generator(size, size)

        #This function get a list of rows of the matrix and make a 
        #pretty print of the board
        print_board(board)

        #Initial position of queen
        start = 0
        #Execution of algorithm of queens, 
        #arguments are board and the initial position of queen
        list_p = posibilities(board, start)

        insert_boards(size, list_p)

        solutions = solutions_count(size)

        print(f"For that size there are: {solutions} solutions")    

        boards_stored(get_boards(size))


if __name__ == "__main__":
    pytest.main(["-v"])

    