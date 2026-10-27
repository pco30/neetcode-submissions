class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            mid = (l+r) // 2
            tot = 0

            for i in piles:
                tot+=math.ceil(float(i) / mid)
            if tot <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
        