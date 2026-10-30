class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans, currsum = nums[0], 1

        for i in range(len(nums)):
            currsum *= nums[i]
            ans = max(ans, currsum)
            if currsum == 0:
                currsum = 1

        currsum = 1
        for i in range(len(nums)-1, -1, -1):
            currsum *= nums[i]
            ans = max(ans, currsum)
            if currsum == 0:
                currsum = 1

        return ans