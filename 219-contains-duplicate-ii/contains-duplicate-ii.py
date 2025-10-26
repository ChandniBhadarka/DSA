class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False
        n = {}
        for i, num in enumerate(nums):
            if num in n and i - n[num] <= k:
                return True
            n[num] = i
        return False