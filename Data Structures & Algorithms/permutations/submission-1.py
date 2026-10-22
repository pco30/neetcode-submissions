class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums):
            if i == len(nums):
                return [[]]
            
            ans = []
            curr = helper(i+1, nums)
            for p in curr:
                for j in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    ans.append(pcopy)
            return ans
        
        return helper(0, nums)
        