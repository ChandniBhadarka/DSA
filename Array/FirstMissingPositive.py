class Solution:
    def firstMissingPositive(self, nums):
        if 1 not in nums:
            return 1

        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

       
        prev = 1
        for num in nums:
            if num < 1:
                continue
            if num == prev:
                continue
            elif num == prev + 1:
                prev = num
            elif num > prev + 1:
                return prev + 1

        return prev + 1
