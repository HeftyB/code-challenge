// An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

// For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
// Given an integer array nums, return the number of arithmetic subarrays of nums.

// A subarray is a contiguous subsequence of the array.

 

// Example 1:

// Input: nums = [1,2,3,4]
// Output: 3
// Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
// Example 2:

// Input: nums = [1]
// Output: 0
 

// Constraints:

// 1 <= nums.length <= 5000
// -1000 <= nums[i] <= 1000

package arithmeticSlices;
import java.util.ArrayList;
import java.util.List;




class Main
{
    public static void main(String[] args)
    {
        Solution sol = new Solution();

        int[] arry = new int[] {1,2,3,4,5};

        // List<int> myList = new ArrayList<>(1,2,3,4,5);

        int x = sol.numberOfArithmeticSlices(arry);
        
        System.out.println(x);
    } 

}





class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        
        int counter = 0;
        int streak = 0;
        int diff = 0;
        int lastDiff = 0;
        
        if(nums.length < 3)
        {
            return 0;
        }
        
        for(int i = 0; i < nums.length; i++ )
        {
            streak = 0;
            boolean start = true;
            
            for(int k = i; k < nums.length; k++)
            {
                if (k + 1 == nums.length)
                {
                    break;
                }
                diff = nums[k + 1] - nums[k];
                
                if (diff == lastDiff || start)
                {
                    streak++;
                } else {
                    streak = 0;
                }
                
                start = false;
                
                if (streak >= 2)
                {
                    counter++;
                }
                
                lastDiff = diff;
                
            }

        }
        
        return counter;
    }
}