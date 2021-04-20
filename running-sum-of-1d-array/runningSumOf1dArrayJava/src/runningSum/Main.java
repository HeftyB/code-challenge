package runningSum;


public class Main {

    public static void main (String[] args)
    {

        int[] arry = new int[] { 1, 2, 3, 4 };
        int[] answer = new int[] { 1, 3, 6, 10};

        Solution sol = new Solution();

        int[] x = sol.runningSum(arry);

        System.out.println(x.toString());
    }
    
}


class Solution {
    public int[] runningSum(int[] nums) {
        int[] retArry = new int[nums.length];
        
        int prev = 0;
        
        for (int i = 0; i < nums.length; i++)
        {
            retArry[i] = nums[i] + prev;
            prev = retArry[i];
        }
        
        return retArry;
    }
}