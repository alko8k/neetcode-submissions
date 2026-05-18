class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.strip()
        f = 0
        l = len(s) - 1

        while f < l:
            if not s[f].isalnum():
                f += 1
                continue
            elif not s[l].isalnum():
                l -= 1
                continue
            elif s[f] != s[l]:
                return False
            f +=1
            l -= 1
        return True