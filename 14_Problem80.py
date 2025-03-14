from typing import List

## Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n:int = len(nums)
        
        i: int = 0
        j: int = i+3

        while(j < n):
            if (nums[i] >= nums[i+2]):
                temp: int = nums[i+2]
                nums[i+2] = nums[j]
                nums[j] = temp
                j += 1
            else:
                i += 1


        print (nums)

        if n < 3:
            return n
        elif n == 3:
            if nums[i] == nums[i+2]:
                return 2
            else:
                return n
        else:
            if i==0:
                return 2
            else:
                return i+3
    




ob = Solution()

nums: List[int] = [1,2,3,4]
print(ob.removeDuplicates(nums))