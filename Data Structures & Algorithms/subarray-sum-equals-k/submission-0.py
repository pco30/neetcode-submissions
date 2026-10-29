class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsums = {0:1}
        ans, currsum = 0, 0

        for num in nums:
            currsum += num
            diff = currsum - k

            ans += prefixsums.get(diff, 0)
            prefixsums[currsum] = 1 + prefixsums.get(currsum, 0)

        return ans
        