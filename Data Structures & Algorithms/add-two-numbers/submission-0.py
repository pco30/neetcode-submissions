# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        str1 = ""
        str2 = ""

        while curr1 is not None:
            str1 = str1 + str(curr1.val)
            curr1 = curr1.next
        
        while curr2 is not None:
            str2 = str2 + str(curr2.val)
            curr2 = curr2.next

        ans = str(int(str1[::-1]) + int(str2[::-1]))[::-1]
        dummy = ListNode(0)
        curr = dummy

        for char in ans:
            curr.next = ListNode(char)
            curr = curr.next

        return dummy.next