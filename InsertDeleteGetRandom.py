import random
class RandomizedSet(object):

    def __init__(self):
        self.dict={}
        self.list=[]
        

    def insert(self, val):
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        return True
        

    def remove(self, val):
        if val not in self.dict:
            return False
        last_val = self.list[-1]
        index = self.dict[val]
        self.list[index] = last_val
        self.dict[last_val] = index
        self.list.pop()
        del self.dict[val]
        return True
        

    def getRandom(self):
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()