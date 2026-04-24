class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(word)

        return list(grouped.values())