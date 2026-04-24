class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in grouped:
                grouped[sortedWord].append(word)
            else:
                grouped[sortedWord] = [word]

        return list(grouped.values())