class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        strs.sort()

        first = strs[0]
        last = strs[-1]

        result = []
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result.append(first[i])

        return "".join(result)


       