#rat and maze problem

def ratMaze(maze):
    n = len(maze)
    sol = [[0 for i in range(n)] for j in range(n)]
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist")
        return False
    printSolution(sol)
    return True

def solveMazeUtil(maze, x, y, sol):
    n = len(maze)
    if x == n-1 and y == n-1:
        sol[x][y] = 1
        return True
    if isSafe(maze, x, y) == True:
        sol[x][y] = 1
        if solveMazeUtil(maze, x+1, y, sol) == True:
            return True
        if solveMazeUtil(maze, x, y+1, sol) == True:
            return True
        sol[x][y] = 0
        return False
    
def isSafe(maze, x, y):
    n = len(maze)
    if x >= 0 and x < n and y >= 0 and y < n and maze[x][y] == 1:
        return True
    return False

def printSolution(sol):
    n = len(sol)
    for i in range(n):
        for j in range(n):
            print(sol[i][j], end = " ")
        print()

if __name__ == "__main__":
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]
    ratMaze(maze)

    