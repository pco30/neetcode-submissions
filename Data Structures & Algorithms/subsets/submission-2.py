class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, curr, ans):
            if i >= len(nums):
                ans.append(curr.copy())
                return
            
            curr.append(nums[i])
            helper(i+1, nums, curr, ans)
            curr.pop()
            helper(i+1, nums, curr, ans)
        
        curr, ans = [], []
        helper(0, nums, curr, ans)
        return ans