class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        zeroMoved = 0 

        while i < n - zeroMoved:
            if nums[i] == 0:
                temp = nums[i]
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]
                nums[n - 1] = temp 
                zeroMoved += 1 
            else:
                i += 1

        
