# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.

# Constraints:
#     -2^31 <= n <= 2^31 - 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
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
    

ob = Solution()

print(ob.isPowerOfTwo(6))