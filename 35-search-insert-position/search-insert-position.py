class Solution(object):
    # def searchInsert(self, nums, target):
    #     if target in nums:
    #         return nums.index(target)

    #     for i in range(len(nums)):
    #         if nums[i] > target:
    #             nums.insert(i, target)
    #             return i
        
    #     nums.append(target)
    #     return len(nums) - 1

    def searchInsert(self, nums, target):
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        
        return start
        