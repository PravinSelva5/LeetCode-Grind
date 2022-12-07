# Easy Questions - NeetCode

Tags: Questions

# Week 6: October 17 - October 24

1. Contains Duplicate
    
    ![Untitled](https://user-images.githubusercontent.com/25359882/206073971-febab953-6233-4384-9fa9-8866dbdd8ad1.png)
    
    ```python
    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            occurences = {}
            
            for num in nums:
                if num not in occurences:
                    occurences[num] = 0
                occurences[num] += 1
            
            for num, key in occurences.items():
                if key > 1:
                    return True
        
            return False
    ```
    
    - Utilized a hash table to count the number of occurences of an integer
    - Time Complexity: O(N)
    - Space Complexity: O(N)
2. Valid Anagram
    
    ![Untitled 1](https://user-images.githubusercontent.com/25359882/206073996-7a69b86f-5e02-476b-8090-68d252a7ecaa.png)
    
    - We’re running 3 for loops, which would mean 3N time. Therefore, Time Complexity is O(N)
    - Because I’m storing a the letters of a string in a dictionary the Space Complexity is O(N)
        
        ```python
        class Solution:
            def isAnagram(self, s: str, t: str) -> bool:
                occurences = {}
                
                # loop through string s and count occurences of each letter
                for letter in s:
                    if letter not in occurences:
                        occurences[letter] = 0
                    occurences[letter] += 1
                
                # loop through string t and check if each letter is present in string s
                for char in t:
                    if char not in occurences or occurences[char] == 0:
                        return False
                    
                    elif char in occurences:
                        occurences[char] -= 1
                
                # Check if any key in occurrences has a non-zero value
                for key, value in occurences.items():
                    if value != 0:
                        return False
                
                return True
        ```
        
3. Two Sum
    
    ![Untitled 2](https://user-images.githubusercontent.com/25359882/206074044-10ae3f44-81fc-4fb2-8c4d-e42128a5d9be.png)
    
    - The solution was accepted but the final if statement to find the indexes is too complex
    - The below algorithms time complexity is O(N)
    - The space comlexity is O(N)
        
        ```python
        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                
                sums = {}
                output = []
                
                for num in range(len(nums)):
                    targetInteger = target - nums[num]
                    sums[nums[num]] = [targetInteger, num]
                
                # Finding index of second integer
                for count, num in enumerate(nums):
                    if sums[num][0] in nums and count != sums[sums[num][0]][1]:
                        output.append(sums[sums[num][0]][1])
                        output.append(count)
                        break
                
                return output
        ```
        
    - The below code is a cleaner way to answer the question. We would maintain a hashmap which will contain the current number we’re looking at as the key and its index as its value
        - we’ll check to see if the complement integer is in the hashmap
            - if it is, we’ll return the current index and the index stored in teh hashmap
            - else, add the current number and index
        
        ```python
        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                
                hashmap = {}
                
                for i in range(len(nums)):
                    targetInt = target - nums[i]
                    
                    if targetInt in hashmap:
                        return [i, hashmap[targetInt]]
                    
                    hashmap[nums[i]] = ish
        ```
        
4. Valid Palindrome
    
    ![Untitled 3](https://user-images.githubusercontent.com/25359882/206074097-da850458-c4ca-45c7-81ef-408e52dc1298.png)
    
    - Time Complexity: O(N)
    - Space Complexity: O(N)
    - I needed to search google to look at the list comprehension syntax and the `isalnum()` method to convert the input string to a list of ONLY alphanuermic  characters
    
    ```python
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            
            letters = [x.lower() for x in s if x.isalnum()]
    
            start = 0
            end = len(letters) - 1
            print(letters)
            while (start < end):
                if letters[start] == letters[end]:
                    start += 1
                    end -= 1
                else:
                    return False
                
                
            return True
    ```
    
5. Best Time to Buy and Sell Stock
    
    ![Untitled 4](https://user-images.githubusercontent.com/25359882/206074154-234cb063-9889-4cc7-b21e-8af9d57d54c6.png)
    
    - Time Complexity: O(N)
    - Space Complexity: O(1)
        - Due to the fact that you can’t go back in time to sell a stock to see profit. The while loop will end once the sell pointer exceeds the length of the input array
        
        ```python
        class Solution:
            def maxProfit(self, prices: List[int]) -> int:
                
                maxProfit = 0
                currentProfit = 0
                buy, sell = 0, 1
                
                while sell < len(prices):
                    
                    if prices[buy] <= prices[sell]:
                        currentProfit = prices[sell] - prices[buy]
                        sell += 1
                        
                    elif prices[buy] > prices[sell]:
                        buy = sell
                        sell += 1
                    
                    maxProfit = max(maxProfit, currentProfit)
                
                return maxProfit
        ```
        
6. Valid Parenthesis
    
    ![Untitled 5](https://user-images.githubusercontent.com/25359882/206074183-fbfcb0d3-aeba-4f22-8655-3473f1e0fc3d.png)
    
    - Unfortunately had a hard time with this question. The solution has a time complexity of O(N)
        
        > Key: Make sure to verify the stack is non-empty. If the current bracket is a closed one and the stack is empty, the algorithm should automatically return `False` .
        > 
        
        ```python
        class Solution:
            def isValid(self, s: str) -> bool:
                closeToOpen = {
                    '}' : '{',
                    ')' : '(',
                    ']' : '['
                }
                
                stack = []
                
                for bracket in s:
                    
                    if bracket in closeToOpen:
                        if stack and stack[-1] == closeToOpen[bracket]:
                            stack.pop()
                        else:
                            return False
                    else:
                        stack.append(bracket)
                
                
                return True if not stack else False
        ```
        
    
    # Week 7: October 24 - October 30
    
    1. Binary Search
        
        ![Untitled 6](https://user-images.githubusercontent.com/25359882/206074199-bc6af2ff-a63c-47c3-9322-4a00c84b82e8.png)
        
        - Implemened Binary Search with Python, time complexity is O(N)
            
            ```python
            class Solution:
                def search(self, nums: List[int], target: int) -> int:
                    start = 0 
                    end = len(nums) - 1
                    
                    while (start <= end):
                        middleIndex = (start + end) // 2
                        
                        if nums[middleIndex] == target:
                            return middleIndex
                        
                        elif nums[middleIndex] > target:
                            end = middleIndex - 1
                        
                        else:
                            start = middleIndex + 1
                    
                    return -1
            ```
            

2. Reverse Linked List

    ![Untitled 7](https://user-images.githubusercontent.com/25359882/206074221-998fe4fb-36a5-4e97-9b64-67a85be3f040.png)

- The key to this solution is to remember that you need have a two pointers and a temporary variable to save the current variable so when the change in next reference, current node isn’t lost
    
    ```python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
            currentNode = head
            prevNode = None
            
            while currentNode != None:
                tempNode = currentNode
                currentNode = currentNode.next
                tempNode.next = prevNode
                prevNode = tempNode
            
            
            return prevNode
    ```
    

1. Merge Two Sorted Lists
    
    ![Untitled 8](https://user-images.githubusercontent.com/25359882/206074257-8eaf255d-7136-4ae8-a35b-8173d7e13682.png)
    

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        mergedList = ListNode()
        finalList = mergedList
        list1_ptr, list2_ptr = list1, list2
        
        while list1_ptr and list2_ptr:
            
            if list1_ptr.val <= list2_ptr.val:
                mergedList.next = list1_ptr
                list1_ptr = list1_ptr.next 
            else:
                mergedList.next = list2_ptr
                list2_ptr = list2_ptr.next
            
            mergedList = mergedList.next
        
        if list1_ptr is not None:
            mergedList.next = list1_ptr
        
        if list2_ptr is not None:
            mergedList.next = list2_ptr
    
        return finalList.next
```

- Neetcode Notes
    
    ```python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def mergeTwoLists(self, list1, list2):
            dummy = ListNode()
            tail = dummy
    
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
    
            if list1:
                tail.next = list1 
            if list2:
                tail.next = list2 
    
        return dummy.next
    ```
    

1. Linked List Cycle
    
    ![Untitled 9](https://user-images.githubusercontent.com/25359882/206074304-0909997a-8b7e-46c6-bced-3882f5e5d422.png)
    
    - Time Complexity: O(N)
    - Space Complexity: O(1)
    
    ```python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution:
        def hasCycle(self, head: Optional[ListNode]) -> bool:
            if head is None:
                return False
            
            slow_ptr = head
            fast_ptr = head.next
            
            while fast_ptr and fast_ptr.next:
                
                if slow_ptr == fast_ptr:
                    return True
                else:
                    slow_ptr = slow_ptr.next 
                    fast_ptr = fast_ptr.next.next
            
            
            return False
    ```
    
    - The solution takes advantage of The Tortoise and the Hare technqiue, also known as ******************Floyd’s Algorithm******************
        - Circular lists differ in that there is no last node that points to null. Instead, there is a node somewhere that points back to a previous node, therefore making its traversal infinite.

1. Invert Binary Tree
    
    ![Untitled 10](https://user-images.githubusercontent.com/25359882/206074341-2ec612a0-b490-466c-a475-9ae18431db62.png)
    
    - Take the root node, swap the children
        - recusively invert the left sub tree
        - recursively invert the right sub tree
    
    ```python
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    # DFS recursive solution
    class Solution:
        def invertTree(self, root):
            if not root:
                return None
            
            # swap children nodes
            tempNode = root.left 
            root.left = root.right
            root.right = tempNode
            
            # recursively call invertTree for left and right
            self.invertTree(root.left)
            self.invertTree(root.right)
        
            return root
    ```
