class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        freq_s = [0] * 123
        freq_t = [0] * 123
        
        for c in t:
            freq_t[ord(c)] += 1

        def is_valid():
            for i in range(123):
                if freq_t[i] > freq_s[i]:
                    return False
            return True
        sm_window = len(s)+1
        L, R = 0, -1
        l, r = 0, 0

        while l < len(s):
            while r < len(s) and not is_valid():
                freq_s[ord(s[r])] += 1
                r += 1
            if is_valid() and (r-l) < sm_window:
                sm_window = r - l
                L, R = l, r
            freq_s[ord(s[l])] -= 1
            l += 1
        if R == -1:
            return ""
        return s[L:R]
