class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, curr, ans):
            if i >= len(nums):
                ans.append(curr.copy())
                return
            
            curr.append(nums[i])
            helper(i+1, nums, curr, ans)
            curr.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, nums, curr, ans)
        
        nums.sort()
        ans, curr = [], []
        helper(0, nums, curr, ans)
        return ans
        