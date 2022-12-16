def smallestDifference(arrayOne, arrayTwo):
    ans = []
    diff = 1000
    i,j = 0,0

    # sort both arrays
    arrayOne.sort()
    arrayTwo.sort()
    
    while i < len(arrayOne) and j < len(arrayTwo):
        absDiff = abs(arrayOne[i] - arrayTwo[j])

        # compare the calculated difference with the previous diff. 
        # Swap values if the calculated difference is closer to 0.
        if absDiff < diff:
            diff = absDiff
            ans = [arrayOne[i], arrayTwo[j]]


        if arrayOne[i] > arrayTwo[j]:
            j +=1
        else:
            i += 1

    return ans