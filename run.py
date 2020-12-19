import sys

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

def rotate(matrix, leftRight):
    layer = 0
    for length in range(len(matrix) - 1, 1, -1):
        for startPoint in range(layer, length, 1):
            saveValue = swap(matrix, save = True, points = switch(leftRight, (startPoint - startPoint + layer), startPoint))
            # save = matrix[points[0]][points[1]]
            
            swap(matrix, points = switch(leftRight, (startPoint - startPoint + layer), startPoint, startPoint, length))
            swap(matrix, points = switch(leftRight, startPoint, length, length, (length - startPoint + layer)))
            swap(matrix, points = switch(leftRight, length, (length - startPoint + layer), (length - startPoint + layer), (startPoint - startPoint + layer)))

            # swap(matrix, save = saveValue, points = switch(leftRight, (length - startPoint + layer), (startPoint - startPoint + layer)))\
            points = switch(leftRight, (length - startPoint + layer), (startPoint - startPoint + layer))
            matrix[points[0]][points[1]] = saveValue
        
        layer += 1

    return matrix

def swap(matrix, **kwargs):
    points = kwargs.get("points")

    if "save" in kwargs:
        if kwargs.get("save") == True:
            return matrix[points[0]][points[1]]
        else:
            print(kwargs.get("save"))
            matrix[points[0]][points[1]] = kwargs.get("save")
    else:
        matrix[points[0]][points[1]] = matrix[points[2]][points[3]]

def switch(swap, *args):    
    if(len(args) == 2):
        if (swap):
            return args[1], args[0]
        return args[0], args[1]
    elif(len(args) == 4):
        if (swap):
            return args[1], args[0], args[3], args[2]
        return args[0], args[1], args[2], args[3]

    return False

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

    leftRight = False
    if len(sys.argv) > 1 and sys.argv[1].lower() == "right":
        leftRight = True

    number = 1
    
    for matrix in matrices:
        print("Matrix %i:" % (number))
        printMatrix(matrix)

        matrix = rotate(matrix, leftRight)

        printMatrix(matrix)
        number +=1
