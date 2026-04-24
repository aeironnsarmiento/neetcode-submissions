class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs:
            encode += str(len(word)) + "," + word
        return encode

    def decode(self, s: str) -> List[str]:
        ["4,neet4,code4,love3,you"]

        decode = []
        i = 0
        
        while i < len(s):
            j = i
            while(s[j] != ","):
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decode.append(s[i:j])
            i = j

        return decode