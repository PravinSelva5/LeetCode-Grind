# This problem can be solved with the fast & slow pointers pattern

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr = head
        fast_ptr = head

        while slow_ptr and fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if fast_ptr == slow_ptr:
                return True

        return False
    
    

# # Attempt two, used a hashMap in this attempt   
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         hashMap = {}
        
#         while (head):
            
#             if head in hashMap:
#                 return True
#             hashMap[head] = 1
#             head = head.next
        
#         return False


# Attempt Three
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         slow, fast = head, head
        
#         # Checking if fast and where its pointing is NULL as it'll reach the end of the loop faster than the slow               pointer
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#             if slow == fast:
#                 return True
            
#         return False