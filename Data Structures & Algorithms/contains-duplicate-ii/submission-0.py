class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if abs(L-R) > k:
                window.remove(nums[L])
                L+=1
            if nums[R] not in window:
                window.add(nums[R])
            elif nums[R] in window:
                return True
        
        return False
        