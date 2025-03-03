class Solution:
    def isPowerOfFourByLoop(self, n: int) -> bool:

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
    

    def isPowerOfFour(self, n: int) -> bool:

        if n<=0:
            return False
        elif n==1:
            return True
       
        ob = Solution()
        isPowerOfFour: bool = ob.checkIsPowerOfFour(n)

        return isPowerOfFour    
    

    def checkIsPowerOfFour(self, n: int) -> bool:
        
        if int(n%4) >= 1:
            return False
        
        q: int = int(n/4)

        if q==1:
            return True

        return self.checkIsPowerOfFour(q)


ob1 = Solution()
print(ob1.isPowerOfFourByLoop(4))

print(ob1.isPowerOfFour(17))