# Time Complexity: O(N)  & Space Complexity: O(N)
def firstDuplicateValue(array):
    duplicates = {}

    for num in array:
        if num not in duplicates:
            duplicates[num] = 0
        duplicates[num] += 1

        if duplicates[num] > 1:
            return num  
    return -1
        