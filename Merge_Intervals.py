class Solution(object):
    def merge(self,intervals):
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for A in intervals[1:]:
            B = merged[-1]
            if A[0] <= B[1]:
                B[1] = max(B[1], A[1])
            else:
                merged.append(A)
        return merged

 #A -> current interval B -> prevoius interval       