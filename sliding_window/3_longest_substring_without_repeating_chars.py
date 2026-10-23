class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        unique = set()
        longest = 0
        while r < len(s):
            if s[r] in unique:
                while s[l] != s[r]:
                    unique.remove(s[l])
                    l += 1
                l += 1 # move forward cuz currently s[l] == s[r]
            else:
                unique.add(s[r])
            r += 1
            longest = max(longest, r-l)
        return longest        

