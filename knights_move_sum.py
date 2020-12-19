"""
File:         knights_move_sum.py
Author:       Vu Nguyen
Date:         10/9/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs create a random grids from 0-100
              and ask the user for the starting value within
              the grid. Finally, it adds up all the number
              that locate in a horse pattern from the starting
              user inputted value.

"""
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == "__main__":

    the_matrix = []

    # This loop makes 2d list for the_matrix
    for i in range(4):
        row = []
        for j in range(4):
            row.append(randint(0, 100))
        the_matrix.append(row)

    start_col = int(input("What is the column you want to start at? ").strip())
    start_row = int(input("What is the row you want to start at? ").strip())

    # Error Checking for Row and Column that's within the inclusive range of 0-3
    while ((start_row and start_col) > 3) or ((start_row and start_col) < 0 ):
        print("The value for row and column must be within the range of 0-3, inclusive!")
        start_col = int(input("What is the column you want to start at? ").strip())
        start_row = int(input("What is the row you want to start at? ").strip())

    print(the_matrix[start_col][start_row])

    # This loop print out the table of matrix number
    for section in the_matrix:
        for number in section:
            print(number, end=' ')
        print()

    chess_sum = 0
    new_col = 0
    new_row = 0

    # This condition find the columns number
    if start_col < 2:
        new_col = start_col + 2

        # These conditions locate each row in order to add the number into the chess_sum.
        if start_row == 3:
            chess_sum += the_matrix[new_col][start_row - 1]
        elif (start_row == 2) or (start_row == 1):
            chess_sum += (the_matrix[new_col][start_row + 1] + the_matrix[new_col][start_row - 1])
        else:
            chess_sum += the_matrix[new_col][start_row + 1]
    else:
        new_col = start_col - 2

        # These conditions locate number in each row, in order to add the number into the chess_sum.
        if start_row == 3:
            chess_sum += the_matrix[new_col][start_row - 1]
        elif (start_row == 2) or (start_row == 1):
            chess_sum += (the_matrix[new_col][start_row + 1] + the_matrix[new_col][start_row - 1])
        else:
            chess_sum += the_matrix[new_col][start_row + 1]

    # This condition find the row number
    if start_row < 2:
        new_row = start_row + 2

        # These conditions locate number in each column, in order to add the number into the chess_sum.
        if start_col == 3:
            chess_sum += the_matrix[start_col - 1][new_row]
        elif (start_col == 2) or (start_col == 1):
            chess_sum += (the_matrix[start_col + 1][new_row] + the_matrix[start_col - 1][new_row])
        else:
            chess_sum += the_matrix[start_col + 1][new_row]
    else:
        new_row = start_row - 2

        # These conditions locate number in each column, in order to add the number into the chess_sum.
        if start_col == 3:
            chess_sum += the_matrix[start_col - 1][new_row]
        elif (start_col == 2) or (start_col == 1):
            chess_sum += (the_matrix[start_col + 1][new_row] + the_matrix[start_col - 1][new_row])
        else:
            chess_sum += the_matrix[start_col + 1][new_row]

    print("The sum of the chess move is", chess_sum)


