class Solution(object):
    def majorityElement(self, nums):
        ct = 0
        for num in nums:
            if ct == 0:
                ct = 1
                ans = num
            elif num == ans:
                ct += 1
            else:
                ct -= 1
        return ans