class Solution(object):
    def generate(self, numRows):
        tri = []

        for i in range(numRows):
            if i == 0:
                tri.append([1]) 
            else:
                prev_row = tri[-1]
                new_row = [1] 
                for j in range(len(prev_row) - 1):
                    new_row.append(prev_row[j] + prev_row[j + 1])
                new_row.append(1) 
                tri.append(new_row)

        return tri

        