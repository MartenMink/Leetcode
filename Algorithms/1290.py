"""
1290. Convert Binary Number in a Linked List to Integer
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head):

        return int(('0b' + ''.join(map(str, head))), 2)

list_node = ListNode()

s = Solution()
print(s.getDecimalValue([1,0,1]))
