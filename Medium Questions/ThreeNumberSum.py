def threeNumberSum(array, targetSum):
    ans = []
    array.sort()
    
    for curNum in range(len(array)):
        left = curNum + 1
        right = len(array) - 1

        while left < right:
            curSum = array[curNum] + array[left] + array[right]

            if curSum > targetSum:
                right -= 1
            elif curSum < targetSum:
                left += 1
            else:
                ans.append([array[curNum], array[left], array[right]])
                right -= 1
                left += 1       
    return ans