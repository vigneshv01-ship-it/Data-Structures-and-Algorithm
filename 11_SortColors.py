from typing import List

## Bubble Sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n: int = len(nums)

        for i in range(n-1):
            flag: bool = False
            for j in range(n-1-i):
                if nums[j]>nums[j+1]:
                    k: int = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = k
                    flag = True
            
            if flag == False:
                break

        print(nums)
        


ob = Solution()
nums: List[int] = [1]

ob.sortColors(nums)