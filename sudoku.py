import numpy as np

#gets your sudoku and prints solved sudoku

#print grid in sudoku way
def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-'*19)
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('|', end='')
            if j == 8:
                print(grid[i][j])
            else:
                print(grid[i][j], end=' ')
            
        
    
#checks if is possible to put n in row i column j
def isPossible(i, j, n):

    #column checker
    for row in range(9):
        if grid[row][j] == n:
            return False

    #row checker
    for column in range(9):
        if grid[i][column] == n:
            return False

    #block checker
    x0 = (i//3)*3
    y0 = (j//3)*3
    for x in range(3):
        for y in range(3):
            if grid[x0 + x][y0 + y] == n:
                return False

    return True


#solves a sudoku
def solve():

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if isPossible(i, j, n):
                        grid[i][j] = n 
                        solve() 
                        grid[i][j] = 0
                return
    
    print_grid(grid)                   

     
grid = list()
print("Enter your sudoku puzzle row by row, by entering numbers of nth row in nth line separated by space and for empty places enter 0\n")
#getting sudoku puzzle
for i in range(9):
    grid.append(list(map(int, input().split())))
print('\n')
solve()              
