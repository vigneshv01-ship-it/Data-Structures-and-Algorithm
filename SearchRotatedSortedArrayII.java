/*
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
*/
import java.util.Arrays;
public class SearchRotatedSortedArrayII {
    public static void main(String args[])
    {
        int[] nums = {2,2,2,3,2,2,2};
        int target = 1;
        System.out.println(Arrays.toString(nums));
        System.out.println(target);
        boolean isValueExist = solution1(nums, target);
        System.out.println(isValueExist);
    }

    public static boolean solution1(int[] nums, int target)
    {
        boolean isValueExist = false;
        int n = nums.length;

        int minimalIndex = 0;
        for(int i=0; i<n-1; i++)
        {
            if(nums[i] > nums[i+1])
            {
                minimalIndex = i+1;
                break;
            }
        }

        int startIndex = 0;
        int endIndex = -1;
        if(minimalIndex > 0 && (nums[0] <= target && target <= nums[minimalIndex-1]))
        {
            startIndex = 0;
            endIndex = minimalIndex-1;
        }
        else if(nums[minimalIndex] <= target && target <= nums[n-1])
        {
            startIndex = minimalIndex;
            endIndex = n-1;
        }


        int midIndex;
        while(startIndex <= endIndex)
        {
            midIndex = startIndex + (endIndex-startIndex)/2;

            if(nums[midIndex] == target)
            {
                isValueExist = true;
                break;
            }

            if(target < nums[midIndex])
            {
                endIndex = midIndex-1;
            }
            else if(nums[midIndex] < target)
            {
                startIndex = midIndex+1;
            }
        }


        return isValueExist;
    }
}
