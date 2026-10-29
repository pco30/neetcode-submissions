class Solution:
    def reverse(self, x: int) -> int:
        ans = str(abs(x))
        r = len(ans) - 1
        rev_ans = ""

        while r >= 0:
            rev_ans += ans[r]
            r -= 1

        int_ans = int(rev_ans)

        if x < 0:
            int_ans = -int_ans

        if -(2**31) <= int_ans < 2**31:
            return int_ans

        return 0