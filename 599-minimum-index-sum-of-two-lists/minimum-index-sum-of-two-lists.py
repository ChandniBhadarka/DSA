class Solution(object):
    def findRestaurant(self, list1, list2):
        hashmap = {word: i for i, word in enumerate(list1)} 
        min_sum = float('inf')
        result = []

        for j, word in enumerate(list2):
            if word in hashmap:
                index_sum = j + hashmap[word]
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [word]
                elif index_sum == min_sum:
                    result.append(word)
                    
        return result
        # min_sum = float('inf')
        # result = []
        # for i, w1 in enumerate(list1):
        #     for j, w2 in enumerate(list2):
        #         if w1 == w2:
        #             s = i + j
        #             if s < min_sum:
        #                 min_sum = s
        #                 result = [w1]
        #             elif s == min_sum:
        #                 result.append(w1)
        # return result
        