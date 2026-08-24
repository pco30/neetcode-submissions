class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums):
            if i == len(nums):
                return [[]]
            
            ans = []
            curr = helper(i+1, nums)
            for b in curr:
                for j in range(len(b) + 1):
                    temp = b.copy()
                    temp.insert(j, nums[i])
                    ans.append(temp)
            return ans

        return helper(0, nums)
        