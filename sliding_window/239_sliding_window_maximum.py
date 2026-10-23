from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque([])
        # 1,3,-1,-3,5,3,6,7
        # l    r
        l = r = 0
        res = []
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r - l + 1 >= k:
                res.append(nums[q[0]])  # max is always the leftmost in q
                l += 1  # first window move onwards. l = 0 until window is atleast k

            r += 1
        return res
