def printMatrix(matrix):
    print("")
    print("Matrix:")
    for row in matrix:
        print("[%i] [%i] [%i]" % (row[0], row[1], row[2]))
    print("")
        

def rotateMatrix(matrix):
    print("Matrix length: " + str(len(matrix)))
    moduloOne = True if len(matrix) % 2 else False

    for length in range(len(matrix)-1, 1, -1):
        print("Length: " + str(length))
        
        if length != 1 and moduloOne:
            for start in range(length):
                save = matrix[start-start][start]

                matrix[start-start][start] = matrix[start][length]
                matrix[start][length] = matrix[length][length-start]
                matrix[length][length-start] = matrix[length-start][start-start]
                matrix[length-start][start-start] = save

    return matrix

if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [8,9,4],
        [7,6,5]
    ]

    # matrix = [
    #     [1, 2, 3, 4],
    #     [12,13,14,5],
    #     [11,16,15,6],
    #     [10,9, 8, 7]
    # ]

    printMatrix(matrix)

    matrix = rotateMatrix(matrix)

    printMatrix(matrix)