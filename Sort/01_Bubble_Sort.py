from typing import List
class Solution:
    def BubbleSort(self, nums: List[int]) -> None:
        l: int = len(nums)

        for i in range(l-1):        ## No. Of Pass
            flag: bool = False
            
            for j in range(l-1-i):  ## No. Of Comparisons
                if nums[j] > nums[j+1]:
                    k: int = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = k
                    flag = True
            
            if flag == False:
                break
    
        print(nums)
                                                  

ob = Solution()
nums: List[int] = [5,4,3,2,1]
ob.BubbleSort(nums)