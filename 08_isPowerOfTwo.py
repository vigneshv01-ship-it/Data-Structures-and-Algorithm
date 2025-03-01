# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.

# Constraints:
#     -2^31 <= n <= 2^31 - 1

class Solution:

    ## Loop Approach
    def isPowerOfTwoByLoop(self, n: int) -> bool:
        if n<=0:
            return False
        elif n==1:
            return True

        q: int = int(n/2)
        r: int = int(n%2)

        isPowerOfTwo: bool = True
        while q!=1:
            if r==1:
                break

            r=int(q%2)
            q = int(q/2)

        if r==1:
            isPowerOfTwo = False

        return isPowerOfTwo
    
    ## Recursion Approach
    def checkPowerOfTwo(self, n: int) -> bool:
        if int(n%2) == 1:
            return False
        
        q: int = int(n/2)

        if q == 1:
            return True
        else:
            return self.checkPowerOfTwo(q)
    
    def isPowerOfTwo(self, n: int) -> bool:

        if n<=0:
            return False
        elif n==1:
            return True

        ob1 = Solution()
        return ob1.checkPowerOfTwo(n)
    


ob1 = Solution()
print(ob1.isPowerOfTwo(6))
print(ob1.isPowerOfTwoByLoop(6))