class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        hashmap = {}
        
        for num in nums:
            hashmap[num] = True 
        
        missing = []
        for i in range(1, n + 1):
            if i not in hashmap:
                missing.append(i)
        
        return missing

        # nums.sort()
        # n=len(nums)
        # nums=set(nums)
        # res=[]
        # for i in range(1,n+1):
        #     if i not in nums:
        #         res.append(i)
        # return res
        