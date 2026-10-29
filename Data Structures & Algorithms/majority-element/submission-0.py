class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = len(nums) // 2
        dic = {}

        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num] = 1
            
            if dic[num] > c:
                return num
        
        return -1
        