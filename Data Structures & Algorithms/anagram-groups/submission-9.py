class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in charMap:
                charMap[key] = []
            charMap[key].append(word)

        return list(charMap.values())