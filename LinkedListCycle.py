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
