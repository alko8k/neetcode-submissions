class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length = len(string)
            encoded += str(length) + "#" + string
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = list()
        i = 0
        while i < len(s):
            k = i
            while s[k] != "#":
                k += 1
            length = int(s[i:k])
            decoded.append(s[k+1:k+1+length])
            i = k + 1 + length
        return decoded

