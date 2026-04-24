class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}

        for word in strs:
            keys = "".join(sorted(word))
            if keys not in wordMap:
                wordMap[keys] = []
            wordMap[keys].append(word)
        
        return list(wordMap.values())