class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = set()
        
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.add(nums[i])
            else:
                return nums[i]
        
        return -1
        