class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for index, val in enumerate(nums):
            comp = target - val

            if comp in mapp:
                return [mapp[comp], index]
            mapp[val] = index
        