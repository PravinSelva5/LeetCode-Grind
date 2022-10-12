# Easy Questions
#### Week 1 - Week 5

# Week 1: September 12 - 18

1. Two Number Sum
    1. this question provides an array and a target sum. One of the solutions is to use a hashTable to track the difference between the targetSum and current integer that the for loop is pointing to.
        1. Check if target integer is present in the hash table, if not add the integer to the hash table.
2. Validate Subsequence
    1. you’re given two non-empty arrays, you need to write a function that checks whether the second array is a subsequence of the first one
        1. **order matters in this question**
        2. we will need to traverse both arrays
        3. use two pointers tracking the subsequence and array
        4. traversing main array and comparing values with subsequene array would be the conditional statement
            1. only need to traverse the large array once
            
3. Sorted Squared Array
    1. Write a function that takes in a non-empty array of integers that are sorted
      in ascending order and returns a new array of the same length with the squares
      of the original integers also sorted in ascending order.
        1. this question can be answered with a single for loop, where each integer is squared
        2. once the for loop ends, you can use the sort method from python so that the new list is in ascending order
        
        ```python
        def sortedSquaredArray(array):
         # Time complexity: nlog(n)
         # Space complexity: log(n)
        
            for num in range(len(array)):
        
                array[num] = array[num] ** 2
        
            array.sort()
        
            return array
        ```
        
        > When given a question with a sorted array, it is a hint that the question can be solved with ***linear time or a better time than the brute force approach.***
        > 
        
        ```python
        # This is a solution that has a linear run time solution.
        def sortedSquaredArray(array):
            sorted_squares = [0 for _ in array]
            smaller_val_ptr = 0
            larger_val_ptr = len(array) - 1
        
            for i in reversed(range(len(array))):
                smaller_value = array[smaller_val_ptr]
                larger_value = array[larger_val_ptr]
        
                if abs(smaller_value) > abs(larger_value):
                    sorted_squares[i] = smaller_value ** 2
                    smaller_val_ptr += 1
                else:
                    sorted_squares[i] = larger_value ** 2
                    larger_val_ptr -= 1
        
            return sorted_squares
        ```
        
4. Tournament Winner
    1. Below is the question
    
    ![Untitled](https://user-images.githubusercontent.com/25359882/195224075-017464c9-21d8-4b0b-bf2c-fd1e05f83e8b.png)

    
    - Below is the solution I used that passed all 10 test cases but time complexity is n**2
    
    ```python
    def tournamentWinner(competitions, results):
        # Write your code here.
        scores = {}
        counter = 0
    
        for match in competitions:
            for team in range(len(match)):
    
                if match[team] not in scores:
                    scores[match[team]] = 0
                
                if results[counter] == 1 and team == 0:
                    scores[match[team]] += 3
    
                if results[counter] == 0 and team == 1:
                    scores[match[team]] += 3
            counter += 1
    
        winner = max(scores, key=scores.get)
    
        print(scores)
        return winner
    ```
    
    - Solution from explanation
        - time complexity O(n)
        - space complexity O(k), where k is the number of teams competing
    
    ```python
    HOME_TEAM_WON = 1
    
    def tournamentWinner(competitions, results):
        # Write your code here.
        current_best_team = ""
        scores = {current_best_team: 0}
    
        for i, competition in enumerate(competitions):
            result = results[i]
            home_team, away_team = competition
    
            winning_team = home_team if result == HOME_TEAM_WON else away_team
    
            updateScores(winning_team, 3, scores)
    
            if scores[winning_team] > scores[current_best_team]:
                current_best_team = winning_team
        
        return current_best_team
    
    def updateScores(team, points, scores):
        if team not in scores:
            scores[team] = 0
    
        scores[team] += points
    ```
    
    1. Non-Constructible Change
        1. The pattern for this question is that if the current coin is greater than the current change + 1, then change+1 is the minimum change that we can’t make with the coins we have.
        
        ![Untitled 1](https://user-images.githubusercontent.com/25359882/195224168-8651b500-ad1e-46fe-b207-85ccfe5bb68e.png)

        
        ```python
        def nonConstructibleChange(coins):
            # O(nlogn) time complexity
            # O(1) space complexity (sorting is in-place)
            coins.sort()
        
            current_change_created = 0
        
            for coin in coins:
        
                if coin > current_change_created + 1:
                    return current_change_created + 1
                else:
                    current_change_created += coin
        
            return current_change_created + 1
        ```
        
    2. Find Closest Value in BST
    
    ![Untitled 2](https://user-images.githubusercontent.com/25359882/195224225-4e416646-4d7d-4ecb-aeb6-2d393240f093.png)
    
    ```python
    # Average time complexity: O(logn)
    # Average space complexity: O(logn) because of the frames we use up in the call stack.
    def findClosestValueInBst(tree, target):
        closest_value = 1000000
    
        while tree != None:
            if abs(target-closest_value) > abs(target-tree.value):
                closest_value = tree.value
    
            if target < tree.value:
                tree = tree.left
            else:
                tree = tree.right
    
        return closest_value
    
    # This is the class of the input tree. Do not edit.
    class BST:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    ```
    
    1. Branch Sums
        
        ![Untitled 3](https://user-images.githubusercontent.com/25359882/195224260-d372b56c-45ff-4594-8fed-ed0cbfcd8ebe.png)
        
        ```python
        # This is the class of the input root. Do not edit it.
        class BinaryTree:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
        
        # O(n) time
        # O(n) space
                # the length of sums is typically the number of leaf nodes, n/2 which becomes O(n) in space complexity
        def branchSums(root):
            sums = []
            calculateBranchSums(root, 0, sums)
            return sums
        
        def calculateBranchSums(node, runningSum, sums):
            if node is None:
                return 
                
            new_running_sum = runningSum + node.value
            if node.left is None and node.right is None:
                sums.append(new_running_sum)
                return
        
            calculateBranchSums(node.left, new_running_sum, sums)
            calculateBranchSums(node.right, new_running_sum, sums)
        ```
        
    
    # Week 2: September 19 - 25
    
    1. Node Depths
        
        ![Untitled 4](https://user-images.githubusercontent.com/25359882/195224281-3f4851e6-f75c-47c0-b363-04e784bb7da2.png)
        
        - Iterative Approach
        
        ```python
        def nodeDepths(root):
            # Iterative Algo
            sumOfDepths = 0
            node_stack = [{"node": root, "depth": 0}]
        
            while len(node_stack) > 0:
                nodeInfo = node_stack.pop()
                node, depth = nodeInfo["node"], nodeInfo["depth"]
                if node is None:
                    continue
                sumOfDepths += depth
                node_stack.append({"node": node.left, "depth": depth + 1})
                node_stack.append({"node": node.right, "depth": depth + 1})
            
            return sumOfDepths
                
        
        # This is the class of the input binary tree.
        class BinaryTree:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
        ```
        
        - Recursive Approach
        
        ```python
        def nodeDepths(root, depth = 0):
            # Recursive Algo
        
            # Handle base case of recursion
            if root is None:
                return 0
            
            return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
        
        # This is the class of the input binary tree.
        class BinaryTree:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
        ```
        
    
    # Week 3: September 26 - October 2
    
    - Spent time on SCRIMBA
    - Got caught up with work wednesday - friday, couldn’t average 1-2 questions per day.
    - Going to get back to regular schedule this week.
    
    # Week 4: October 3 - October 9
    
    1. Binary-First Search
        
        ![Untitled 5](https://user-images.githubusercontent.com/25359882/195224304-1b2e6a57-7400-4fea-a36a-e2944b58bcd4.png)
        
        - The solution to this question does not take many lines of code.
        - Because the output array should be in the order we traverse the tree
            - each time we arrive at a node, we append the value to the arrary
            - we call the depthFirstSearch function again on the children nodes of the current node untill theres none.
        
        ```python
        class Node:
            def __init__(self, name):
                self.children = []
                self.name = name
        
            def addChild(self, name):
                self.children.append(Node(name))
                return self
        
            def depthFirstSearch(self, array):
                # Write your code here.
                array.append(self.name)
                for child in self.children:
                    child.depthFirstSearch(array)
        
                return array
        ```
        
    
    1. Minimum Waiting Time
        
        ![Untitled 6](https://user-images.githubusercontent.com/25359882/195224321-e78592a9-f913-49b7-ac52-01f5b7cdf894.png)
        
        ```python
        def minimumWaitingTime(queries):
            # sort queries in ascending order
            queries.sort()
            min_waiting_time = 0
            waiting_time = []
            
            for num in range(1, len(queries)):
                min_waiting_time += queries[num - 1] 
                waiting_time.append(min_waiting_time)
        
            #print(sum(waiting_time))
        
            return sum(waiting_time)
        ```
        
        - sorting the input array in ascending array, makes it so we execute the longest query last, making this a greedy algorithm approach
            - Greedy Algorithm?
                
                > Greedy algorithm makes greedy choices at each step to ensure that the objective function is optimized. The Greedy algorithm has only one shot to compute the optimal solution so that it never goes back and reverses the decision.
                > 
        - Time Complexity: O(nlogn) because we are sorting the area as the first step.
        - Space Complexity:O(1) because we are sorting in-place
        
        ```python
        # Another solution
        # O(nLogn) time | O(1) space
        def minimumWaitingTime(queries):
            queries.sort()
            
            totalWaitingTime = 0
        
            for index, duration in enumerate(queries):
                queriesLeft = len(queries) - (index + 1)
                totalWaitingTime += duration * queriesLeft
        
            return totalWaitingTime
        ```
        
    2. Class Photos
        
        ![Untitled 7](https://user-images.githubusercontent.com/25359882/195224343-6c920e09-0c03-4965-b964-a8426435b41e.png)

        
        - in my solution, because the arrays are of the same length and the back row students need to be taller than the student infront of them
            - I sorted both arrays in ascending order (nlogN time)
            - Checked which group had the shortest student to determine which group would have to stand at the back
            - Looped through both arrays to see if the height criteria is met.
            
            ```python
            # O(NlogN) time complexity - sorting inplace
            # O(1) space complexity
            def classPhotos(redShirtHeights, blueShirtHeights):
                redGroup = False
                blueGroup = False
            
                # sort both groups from shortest to tallest
                redShirtHeights.sort()
                blueShirtHeights.sort()
            
                # Check which group has the shortest student
                if redShirtHeights[0] > blueShirtHeights[0]:
                    # Red Group will be at the back
                    redGroup = True
                else:
                    blueGroup = True
            
                # Loop through arrays to verify if conditions can be met
            
                for num in range(len(redShirtHeights)):
                    if redGroup and redShirtHeights[num] > blueShirtHeights[num]:
                        continue
                    elif blueGroup and blueShirtHeights[num] > redShirtHeights[num]:
                        continue
                    else: 
                        return False
                
                return True
            ```
            
        - In the instructor’s solution:
            
            ```python
            def classPhotos(redShirtHeights, blueShirtHeights):
                redShirtHeights.sort(reverse=True)
                blueShirtHeights.sort(reverse=True)
            
                shirtColourInFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
            
                for height in range(len(redShirtHeights)):
                    redShirtHeight = redShirtHeights[height]
                    blueShirtHeight = blueShirtHeights[height]
            
                    if shirtColourInFirstRow == 'RED':
                        if redShirtHeight >= blueShirtHeight:
                            return False
                    else:
                        if blueShirtHeight >= redShirtHeight:
                            return False
            
                return True
            ```
            

1. Tandem Bicycle

![Untitled 8](https://user-images.githubusercontent.com/25359882/195224372-1024dc1d-bfb6-4a02-91a8-e0ca0838858e.png)

```python
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):

    # variables
    total_speed_max = 0
    total_speed_min = 0
    list_len = len(redShirtSpeeds)
    index = 0
    end = list_len - 1

    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=True)
    # Loop through both lists
    while (index < list_len and end >= 0):
        if fastest == True:
            total_speed_max += max(redShirtSpeeds[index], blueShirtSpeeds[index])
        else:
            total_speed_min += max(redShirtSpeeds[end], blueShirtSpeeds[index])
            end -= 1
        index += 1

    if fastest:
        return total_speed_max
    else:
        return total_speed_min
```

- Solution from Tim Ruscica

```python
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # sorting lists
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        reverseArrayInPlace(redShirtSpeeds)

    totalSpeed = 0

    for index in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[index]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - index - 1]
        totalSpeed += max(rider1, rider2)

    return totalSpeed

def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
```

1. Remove Duplicates From Linked List

![Untitled 9](https://user-images.githubusercontent.com/25359882/195224390-cb3d5e63-010c-4fb8-b753-77ad384d20dd.png)

- The linked list is sorted, which allow you to make changes in-place without needing to create another data structure

```python
# O(n) time | O(n) space

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList

    while currentNode != None:
        nextNode = currentNode.next

        while nextNode is not None and nextNode.value == currentNode.value:
            nextNode = nextNode.next

        currentNode.next = nextNode
        currentNode = nextNode

    return linkedList
```

# Week 5: October 10 - October 16

1. Nth fibonacci

![Untitled 10](https://user-images.githubusercontent.com/25359882/195224402-37820c0a-1cc0-4d8a-aed6-1bea69179fe4.png)

- For fibonacci sequences, the first two integers are always 0 and 1.
- I initialized an arry with the first two terms. Then ran a for loop from 2 to the input number that was provided.
- In the loop, ran the sum of the n-2 and n-1 number in the array to find the next fib sequence number
    
    ```python
    # In this solution: Time O(N) | Space O(N)
    def getNthFib(n):
        fibNumberArray = [0, 1] 
    
        for num in range(2, n):
            fibNumberArray.append(fibNumberArray[num-2] + fibNumberArray[num-1])
    
        return fibNumberArray[n-1]
    ```
    
- Recursive solution
    
    ```python
    # O(2^n) time | O(n) space
    def getNthFib(n):
        if n == 2:
            return 1
        elif n == 1:
            return 0
        else:
            return getNthFib(n - 1) + getNthFib(n - 2)
    ```
    
1. Product Sum
    
    ![Untitled 11](https://user-images.githubusercontent.com/25359882/195224443-aab543b4-cab4-4ef5-94ee-31c5ed76fffa.png)
   
    - When reading this question, a special array is an array with integers or other sub-arrays within it. It is important to recognize the solution will need some form of recursion in the algorithm
        - T*he question I asked myself first is, “If I were to loop the array, how can I tell if the element is an integer or an array?”*
            - Python has a `type` method that can be used to check if the element is an integer or a list
            
            > Example of how the `type` method can be used
            > 
            > 
            > ![Untitled 12](https://user-images.githubusercontent.com/25359882/195224476-3f2dc53f-9c6e-43ee-ade7-9f42f97183ab.png)
            > 
    
    ```python
    # O(n) time complexity, where N represents all the elements in the array, including all the elements in the sub-arrays
    # O(d) space complexity, where D represents the largest depth of the sum
    def productSum(array, multiplier = 1):
        sum = 0
    
        for element in array:
            if type(element) is list:
                sum += productSum(element, multiplier + 1)
            else:
                sum += element
    
        return sum * multiplier
    ```
    
2. Binary Search
    
    ![Untitled 13](https://user-images.githubusercontent.com/25359882/195224494-e221f76d-b0c2-49d7-9cd8-85be930ab2e9.png)
    
    ```python
    # O(logn) time | O(1) space complexity
    def binarySearch(array, target):
        start = 0
        end = len(array) - 1
        
        while start <= end:
    				# Use two slashes in python to round value down to get an integer answer
            mid = (end + start) // 2
            if array[mid] == target:
                return mid
                
            elif array[mid] > target:
                end = mid - 1
    
            else:
                start = mid + 1
    
        return -1
    ```
    
    > *When a question gives you a list that is sorted. Ask yourself if Binary Search can be used to solve the question*
    > 
    - Recursive solution
    
    ```python
    # O(log(n)) time | O(log(n)) space because of the recursive calls to the stack
    def binarySearch(array, target):
        return binarySearchHelper(array, target, 0, len(array) - 1)
    
    def binarySearchHelper(array, target, left, right):
    
        if left > right:
            return -1
    
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            return binarySearchHelper(array, target, left, middle - 1)
        else:
            return binarySearchHelper(array, target, middle + 1, right)
    ```
    
3. Find Three Largest Numbers
    
    ![Untitled 14](https://user-images.githubusercontent.com/25359882/195224509-dd1fa03c-0f82-4a47-b093-161847b4e26a.png)
    
    ```python
    # O(n) time complexity | O(1) space complexity
    def findThreeLargestNumbers(array):
        outputArray = [-10000, -10000, -10000]
        tmp, tmp2 = 0, 0
    
        for num in array:
    
            if num >= outputArray[2]:
                tmp = outputArray[2]
                tmp2 = outputArray[1]
                outputArray[2] = num
                outputArray[1] = tmp
                outputArray[0] = tmp2
                
            elif num >= outputArray[1]:
                tmp = outputArray[1]
                outputArray[1] = num
                outputArray[0] = tmp
    
            elif num >= outputArray[0]:
                outputArray[0] = num
    
            print(outputArray)
    
        return outputArray
    ```
    
    - The solution by instructor abstracts the iterative operations that is updating the largest number and shifting the values into two different functions. These makes the code cleaner and easier to read.
    
    ```python
    # O(n) time | O(1) space
    def findThreeLargestNumbers(array):
        threeLargest = [None, None, None]
    
        for num in array:
            updateLargest(threeLargest, num)
        return threeLargest
    
    def updateLargest(threeLargest, num):
        if threeLargest[2] is None or num > threeLargest[2]:
            shiftAndUpdate(threeLargest, num, 2)
        elif threeLargest[1] is None or num > threeLargest[1]:
            shiftAndUpdate(threeLargest, num, 1)
        elif threeLargest[0] is None or num > threeLargest[0]:
            shiftAndUpdate(threeLargest, num, 0)
    
    def shiftAndUpdate(array, num, index):
        for i in range(index + 1):
            if i == index:
                array[i] = num
            else:
                array[i] = array[i + 1 ]
    ```
    
4. pending..
5.
