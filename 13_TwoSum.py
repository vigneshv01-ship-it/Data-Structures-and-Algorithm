from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left: int = 0
        right:int = len(numbers)-1

        while left < right:

            sum: int = numbers[left]+numbers[right]

            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            elif sum == target:
                left += 1
                right += 1
                return [left, right]      

        return []
    

ob = Solution()
print(ob.twoSum([1], 1))