class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = {}

        for i in range(len(nums)):
            if nums[i] not in sol:
                sol[nums[i]] = 1
            else:
                sol[nums[i]]+=1
        
        sorted_sol = dict(sorted(sol.items(), key=lambda item: item[1], reverse=True))
        ans = list(sorted_sol)[:k]
        return ans
        