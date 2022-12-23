def mergeOverlappingIntervals(intervals):
    output = []

    # sort input array
    intervals.sort()
    j = 0
    for interval in range(len(intervals)):
        if interval == 0:
            output.append(intervals[interval])
        
        # Compare current interval's starting time with the interval in the output array's ending time
        elif intervals[interval][0] <= output[j][1]:
            output[j][1] = max(intervals[interval][1], output[j][1])

        else:
            output.append(intervals[interval])
            j += 1

    return output