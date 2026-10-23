class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26
        a = ord('a')

        l = 0
        r = len(s1)

        for c in s1:
            freq1[ord(c) - a] += 1
        
        for c in s2[0:r]:
            freq2[ord(c) - a] += 1

        if freq1 == freq2:
            return True

        for l in range(len(s2) - len(s1)):
            freq2[ord(s2[l]) - a] -= 1
            freq2[ord(s2[l+r]) - a] += 1

            if freq1 == freq2:
                return True
            
        return False
