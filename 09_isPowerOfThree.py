class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n<=0:
            return False
        elif n==1:
            return True
        
        r: int = int(n%3)
        q: int = int(n/3)


        isPowerOfThree: bool = True

        while q != 1:
            if r>=1:
                break

            r = int(q%3)
            q = int(q/3)
        

        if r>=1:
            isPowerOfThree = False
        

        return isPowerOfThree


ob = Solution()
print(ob.isPowerOfThree(10))
        