/*
https://leetcode.com/contest/weekly-contest-354/problems/sum-of-squares-of-special-elements/
2778. Sum of Squares of Special Elements
You are given a 1-indexed integer array nums of length n.

An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

Return the sum of the squares of all special elements of nums.

Input: nums = [1,2,3,4]
Output: 21
Explanation: There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4.
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.

Algorithm:
- Identify the length of the array 'n'.
- Initialize an Integer variable 'sumOfSquares' with value 0
- Loop through the array until 'n-1'
    - If the current array element divides n (i.e current array element MODULO n is 0)
        - Find current array element multiplied by itself
        - Add sumOfSquares with the above result and assign it back to sumOfSquares
- Return sumOfSquares

 */
public class SumOfSquaresOfSpecialElements {
    public static void main(String[] args)
    {
        int[] nums = {1,2,3,4};

        int n=nums.length;
        int sumOfSquares = 0;
        int temp = 0;

        for(int i=0; i<n; i++)
        {
            if(n % (i+1) == 0)
            {
                temp = nums[i] * nums[i];
                sumOfSquares = sumOfSquares + temp;
                temp = 0;
            }
        }
        System.out.println(sumOfSquares);
    }
}
