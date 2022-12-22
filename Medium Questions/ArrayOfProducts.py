# SOLUTION 1

# def arrayOfProducts(array):
#     i = 0
#     result = []

#     while i < len(array):
#         tmp = 1

#         for j in range(len(array)):
#             if i != j:
#                 tmp *= array[j]

#         result.append(tmp)
#         i += 1

#     return result


#-----------------------------#
#---------SOLUTION------------#
#-----------------------------#

def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    # calculate left products
    leftRunningProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    # calculate right products
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    # update final products array with left & right products
    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]

    return products