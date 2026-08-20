class Solution:
    def isValid(self, s: str) -> bool:
        ans = []

        for i in range(len(s)):
            if s[i] in "([{":
                ans.append(s[i])

            elif s[i] in ")]}":
                if len(ans) == 0:
                    return False

                if s[i] == ")" and ans[-1] == "(":
                    ans.pop()
                elif s[i] == "]" and ans[-1] == "[":
                    ans.pop()
                elif s[i] == "}" and ans[-1] == "{":
                    ans.pop()
                else:
                    return False

        if len(ans) == 0:
            return True
        return False