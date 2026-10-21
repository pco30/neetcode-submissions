class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        R = L+1

        while R < len(nums):
            if nums[L] == nums[R]:
                nums.pop(R)
            else:
                L+=1
                R = L+1
        
        return len(nums)
        