class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for s in strs:
            sortedWord = "".join(sorted(s))
            if sortedWord in grouped:
                grouped[sortedWord].append(s)
            else:
                grouped[sortedWord] = [s]

        return list(grouped.values())