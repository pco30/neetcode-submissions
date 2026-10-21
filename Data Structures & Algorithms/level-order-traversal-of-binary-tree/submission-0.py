# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = collections.deque()
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            lvl = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    lvl.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if lvl:
                ans.append(lvl)


        return ans
        