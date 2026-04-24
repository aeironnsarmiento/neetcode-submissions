class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            encodedString += word
            encodedString += "😀"
        return encodedString

    def decode(self, s: str) -> List[str]:
        ans = []
        word = ""
        for ch in s:
            if ch != "😀":
                word += ch
            else:
                ans.append(word)
                word = ""
        if word:
            ans.append(word)
        return ans