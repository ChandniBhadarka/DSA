class Solution(object):
    def missingNumber(self, nums):
        #method 1 -> sorting
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return len(nums)

        #method 2 -> XOR
        n = len(nums)
        res = 0
        for i in range(n + 1):  
            res ^= i
        for num in nums:
            res ^= num
        return res

        