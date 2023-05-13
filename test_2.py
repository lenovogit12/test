# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def printM(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print("")
        

def rotateMatrix(matrix):
    n = len(matrix)
    # reverse each column
    for i in range(n):
        for j in range (int(n/2)):
            temp = matrix[n-j-1][i]
            print(matrix[n-j-1][i], matrix[j][i])
            matrix[n-j-1][i] = matrix[j][i]
            matrix[j][i] = temp
    #printM(matrix)
    for i in range(n):
        for j in range(i,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


# driver program
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotateMatrix(matrix)
printM(matrix)

