class Solution(object):
    def findErrorNums(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        dup = miss = -1
        for i in range(1, len(nums) + 1):
            if i not in count:
                miss = i
            elif count[i] == 2:
                dup = i

        return [dup, miss]
        
        