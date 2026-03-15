class Solution(object):
    def countPrimes(self, n):

        if n <= 2:
            return 0
        isprime= [True]*n
        isprime[0]= isprime[1]= False
        
        p=2
        while p*p < n:
            if isprime[p]:
                for i in range(p*p, n, p):
                    isprime[i] = False
            p +=1
        return sum(isprime) 