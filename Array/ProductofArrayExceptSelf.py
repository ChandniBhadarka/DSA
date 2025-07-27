class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        
        # Left 
        l = 1
        for i in range(n):
            ans[i] = l
            l *= nums[i]
        
        # Right 
        r = 1
        for i in reversed(range(n)):
            ans[i] *= r
            r *= nums[i]
        
        return ans

   

        
        