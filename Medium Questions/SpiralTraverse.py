def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        # move right
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # move down
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # move left
        for col in reversed(range(startCol, endCol)):
            # we need to handle the edge case when there is a single row in the middle of the matrix
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        # move up
        for row in reversed(range(startRow + 1, endRow)):
            # we need to handle the edge case when there is a single column in the middle of the matrix
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1

    return result