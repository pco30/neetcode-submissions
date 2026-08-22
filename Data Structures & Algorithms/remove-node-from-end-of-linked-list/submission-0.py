# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head

        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        
        arr.pop(-n)

        dummy = ListNode(0)
        curr1 = dummy

        for i in range(len(arr)):
            curr1.next = ListNode(arr[i])
            curr1 = curr1.next

        head = dummy.next
        return head
        

        #0, 1, 2, 3   len-1