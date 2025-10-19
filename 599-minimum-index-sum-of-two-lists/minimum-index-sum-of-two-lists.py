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
        