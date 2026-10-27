class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, currsum = nums[0], 0
        for num in nums:
            if currsum < 0:
                currsum = 0
            currsum+=num
            maxsum = max(currsum, maxsum)
        return maxsum