def printMatrix(matrix):
    print("")
    for row in matrix:
        str = ""
        for item in row:
            str += "[%i] " % (item)
        print(str)
    print("")
        

def rotateMatrixLeft(matrix):
    layer = 0
    for length in range(len(matrix) - 1, 1, -1):
        for startPoint in range(layer, length, 1):
            save = matrix[startPoint - startPoint + layer][startPoint]

            matrix[startPoint - startPoint + layer][startPoint] = matrix[startPoint][length]
            matrix[startPoint][length] = matrix[length][length - startPoint + layer]
            matrix[length][length - startPoint + layer] = matrix[length - startPoint + layer][startPoint - startPoint + layer]
            matrix[length - startPoint + layer][startPoint - startPoint + layer] = save
        
        layer += 1

    return matrix

if __name__ == "__main__":
    matrices = [
        [
            [1,2,3],
            [8,9,4],
            [7,6,5]
        ],
        [
            [1, 2, 3, 4],
            [12,13,14,5],
            [11,16,15,6],
            [10,9, 8, 7]
        ],
        [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ],
        [
            [ 1,  2,  3,  4,  5, 6],
            [20, 21, 22, 23, 24, 7],
            [19, 32, 33, 34, 25, 8],
            [18, 31, 36, 35, 26, 9],
            [17, 30, 29, 28, 27, 10],
            [16, 15, 14, 13, 12, 11]
        ],
    ]

    number = 1
    
    for matrix in matrices:
        print("Matrix %i:" % (number))
        printMatrix(matrix)

        matrix = rotateMatrixLeft(matrix)

        printMatrix(matrix)
        number +=1
