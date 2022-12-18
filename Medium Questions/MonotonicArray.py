def isMonotonic(array):
    if len(array) <= 2:
        return True

    isTrendingUp = True
    isTrendingDown = True

    for i in range(1, len(array)):

        if array[i] < array[i - 1]:
            isTrendingUp = False
        elif array[i] > array[i - 1]:
            isTrendingDown = False

    return isTrendingUp or isTrendingDown
