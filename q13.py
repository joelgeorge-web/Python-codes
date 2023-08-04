#code for a 9*9 sudoku solver

import numpy as np
import time

#function to check if the number is valid in the given position
def isValid(board, row, col, num):
    #check if the number is present in the row
    for i in range(9):
        if(board[row][i] == num):
            return False
    #check if the number is present in the column
    for i in range(9):
        if(board[i][col] == num):
            return False
    #check if the number is present in the 3*3 box
    for i in range(3):
        for j in range(3):
            if(board[i + row - row%3][j + col - col%3] == num):
                return False
    return True

#function to solve the sudoku
def solveSudoku(board, row, col):
    #if the column is 9, move to the next row
    if(col == 9):
        col = 0
        row += 1
        #if the row is 9, the sudoku is solved
        if(row == 9):
            return True
    #if the current position is not empty, move to the next position
    if(board[row][col] != 0):
        return solveSudoku(board, row, col + 1)
    #try all the numbers from 1 to 9
    for i in range(1, 10):
        #if the number is valid, place it in the current position
        if(isValid(board, row, col, i)):
            board[row][col] = i
            #if the sudoku is solved, return True
            if(solveSudoku(board, row, col + 1)):
                return True
            #if the sudoku is not solved, backtrack
            board[row][col] = 0
    #if the sudoku is not solved, return False
    return False

#function to print the sudoku
def printSudoku(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = " ")
        print(board[i])

#main function
if __name__ == "__main__":
    #take the input
    board = []
    for i in range(9):
        board.append(list(map(int, input("Enter the values").split())))
    for i in range(9):
        print(board[i])
        print("\n")
    #start the timer
    start = time.time()
    #solve the sudoku
    if(solveSudoku(board, 0, 0)):
        #print the sudoku
        printSudoku(board)
    else:
        print("No solution exists")
    #end the timer
    end = time.time()
    #print the time taken
    print("Time taken: ", end - start)

