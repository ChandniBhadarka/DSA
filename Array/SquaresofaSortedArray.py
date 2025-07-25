class Solution(object):
    def sortedSquares(self, nums):
        
        squared = [x * x for x in nums]
    
        squared.sort()
        
        return squared

        