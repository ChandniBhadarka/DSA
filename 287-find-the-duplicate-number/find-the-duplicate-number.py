class Solution(object):
    def findDuplicate(self, nums):
        # slow = nums[0]
        # fast = nums[0]

        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break

        # slow = nums[0]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]

        # return slow
        hs=[0]*len(nums)
        for i in nums:
            if hs[i]==1:
                return i
            else:
                hs[i]=1   
        