class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        com = set()
        for i in range(len(nums)):
            com.add(nums[i])
        
        if len(com) == len(nums):
            return False
        
        return True
        