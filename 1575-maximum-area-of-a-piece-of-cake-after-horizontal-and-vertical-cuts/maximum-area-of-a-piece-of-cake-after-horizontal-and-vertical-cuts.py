class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        MOD = 10**9 + 7
        
        # Sort the cuts
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Max horizontal gap
        max_h_gap = max(horizontalCuts[0], h - horizontalCuts[-1])  # edges
        for i in range(1, len(horizontalCuts)):
            max_h_gap = max(max_h_gap, horizontalCuts[i] - horizontalCuts[i-1])
        
        # Max vertical gap
        max_v_gap = max(verticalCuts[0], w - verticalCuts[-1])  # edges
        for j in range(1, len(verticalCuts)):
            max_v_gap = max(max_v_gap, verticalCuts[j] - verticalCuts[j-1])
        
        # Result
        return (max_h_gap * max_v_gap) % MOD
