class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        maxP = 0

        l, r = 0, 0
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            count.add(s[r])
            maxP = max(maxP, len(count))

        return maxP