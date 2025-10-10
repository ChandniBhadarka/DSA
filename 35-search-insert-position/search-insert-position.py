class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)

        for i in range(len(nums)):
            if nums[i] > target:
                nums.insert(i, target)
                return i
        
        nums.append(target)
        return len(nums) - 1
        