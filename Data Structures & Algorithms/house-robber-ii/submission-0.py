class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        prev1, prev2 = 0, 0

        for i in nums:
            curr = max(prev1, prev2+i)
            prev2 = prev1
            prev1 = curr
        return prev1