/*
https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

33. Search in Rotated Sorted Array

Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1


 */
import java.util.Arrays;
public class SearchRotatedSortedArray {
    public static void main(String args[])
    {
        int[] nums = {4,5,6,7,0,1,2};
        int target = 0;
        System.out.println(Arrays.toString(nums));
        System.out.println(target);
        int outputIndex = solution1(nums, target);
        System.out.println(outputIndex);
    }

    public static int solution1(int[] nums, int target)
    {
        int outputIndex = -1;
        int n = nums.length;

        int minimalIndex = 0;
        for(int i=1; i<n; i++)
        {
            if(nums[minimalIndex] > nums[i])
            {
                minimalIndex = i;
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
                outputIndex = midIndex;
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

        return outputIndex;
    }
}
