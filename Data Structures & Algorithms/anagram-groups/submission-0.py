class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for st in strs:
            sorted_str = "".join(sorted(st))
            ans[sorted_str].append(st)
        return list(ans.values())
        