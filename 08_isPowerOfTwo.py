# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.

# Constraints:
#     -2^31 <= n <= 2^31 - 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        elif (n == 1) or (n == 2) or (n == -2):
            return True
        
        divisor: int = 2
        if n<0:
            divisor = -2


        q: int = int(n/divisor)
        r: int = int(n%divisor)

        isPowerOfTwo: bool = False

        if(divisor<0):
            while r != 1:
                r = int(q%divisor)
                q = int(q/divisor)
                if q == 2:
                    isPowerOfTwo = False
                    break
                elif q == -2:
                    isPowerOfTwo = True
                    break
        else:
            while r != 1:
                r = int(q%divisor)
                q = int(q/divisor)
                if q == 2:
                    isPowerOfTwo = True
                    break
        
        if r==1:
            return False
        else:
            return isPowerOfTwo
    

ob = Solution()
print(ob.isPowerOfTwo(4))