# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        answer = ListNode(None)
        pointer: ListNode = answer
        carry = 0
        summation = 0

        while l1 is not None or l2 is not None:
            summation = carry
            if l1 != None:
                summation += l1.val
                l1 = l1.next

            if l2 != None:
                summation += l2.val
                l2 = l2.next

            carry = int(summation / 10)
            pointer.next = ListNode(summation % 10)
            pointer = pointer.next

        if carry > 0:
            pointer.next = ListNode(carry)

        return answer.next
