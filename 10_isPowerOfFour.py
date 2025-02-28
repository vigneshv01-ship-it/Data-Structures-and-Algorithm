class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n<=0:
            return False
        elif n == 1:
            return True
        
        q: int = int(n/4)
        r: int = int(n%4)

        isPowerOfFour: bool = True

        while q!=1:
            if r>=1:
                break

            r = int(q%4)
            q = int(q/4)

        if r>=1:
            isPowerOfFour = False

        return isPowerOfFour
    

ob = Solution()
print(ob.isPowerOfFour(0))
print(ob.isPowerOfFour(1))
print(ob.isPowerOfFour(2))
print(ob.isPowerOfFour(3))
print(ob.isPowerOfFour(4))
print(ob.isPowerOfFour(5))
print(ob.isPowerOfFour(6))
print(ob.isPowerOfFour(7))
print(ob.isPowerOfFour(8))
print(ob.isPowerOfFour(9))
print(ob.isPowerOfFour(10))
print(ob.isPowerOfFour(11))
print(ob.isPowerOfFour(12))
print(ob.isPowerOfFour(13))
print(ob.isPowerOfFour(14))
print(ob.isPowerOfFour(15))
print(ob.isPowerOfFour(16))
print(ob.isPowerOfFour(17))
print(ob.isPowerOfFour(18))
print(ob.isPowerOfFour(19))
print(ob.isPowerOfFour(19))