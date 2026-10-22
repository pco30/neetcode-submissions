class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i, curr, ans, n, k):
            if len(curr) == k:
                ans.append(curr.copy())
                return
            
            if i > n:
                return
            
            curr.append(i)
            helper(i+1, curr, ans, n, k)
            curr.pop()
            helper(i+1, curr, ans, n, k)
        
        curr, ans = [], []
        helper(1, curr, ans, n, k)
        return ans

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         def helper(i, curr, ans, n, k):
#             if len(curr) == k:
#                 ans.append(curr.copy())
#                 return
#             if i > n:
#                 return
            
#             for j in range(i, n+1):
#                 curr.append(j)
#                 helper(j+1, curr, ans, n, k)
#                 curr.pop()

#         ans = []
#         helper(1, [], ans, n, k)
#         return ans
        
        