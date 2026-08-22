# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr1 = list1
        curr2 = list2

        while curr1 is not None:
            arr.append(curr1.val)
            curr1 = curr1.next
        
        while curr2 is not None:
            arr.append(curr2.val)
            curr2 = curr2.next        

        arr.sort()
        dummy = ListNode(0)
        curr3 = dummy

        for val in arr:
            curr3.next = ListNode(val)
            curr3 = curr3.next

        head = dummy.next
        return head