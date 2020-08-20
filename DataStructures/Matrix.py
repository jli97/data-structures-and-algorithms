
def transpose(A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)] 

        for i in range(C):
            for j in range(R):
                ans[i][j] = A[j][i]

        return ans

def inPlaceTranspose(matrix): # Must be a square matrix
    l = len(matrix)
    
    if(len(matrix) != len(matrix[0])):
        print('Only works on square matrix')
        return None
        
    for i in range(l):
        for j in range(i, l): #range(i, l) makes it so that we only travese the first diagonal half of the matrix
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

def printMatrix(A):
    for row in A:
        print(row)

def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9],[8,9,8]]
    print('Original Matrix')
    printMatrix(matrix)

    transposed = transpose(matrix)
    print('Transposed Matrix')
    printMatrix(transposed)

if __name__ == "__main__":
    main()