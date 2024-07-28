# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        output = None
        while head is not None:
            temp = head
            head = head.next
            temp.next = output
            output = temp
        return output
        