class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper1(nums):
            curr, ans = [], []
            helper2(0, nums, curr, ans)
            return ans
        
        def helper2(i, nums, curr, ans):
            if i >= len(nums):
                tot = 0
                for j in range(len(curr)):
                    tot += curr[j]

                if tot == target:
                    ans.append(curr.copy())
                return
            
            tot = 0
            for j in range(len(curr)):
                tot += curr[j]

            if tot > target:
                return
            
            curr.append(nums[i])
            helper2(i, nums, curr, ans)
            curr.pop()

            helper2(i+1, nums, curr, ans)

        ans = helper1(nums)

        return ans