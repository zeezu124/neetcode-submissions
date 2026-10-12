public class Solution {
    public bool hasDuplicate(int[] nums) {
        Array.Sort(nums);
        
        while (nums != null && nums.Length > 0) {
            int currentNumber = nums[0];

            for (int i = 1; i < nums.Length; i++) {
                
                if (nums[i] == currentNumber) {
                    return true;
                }
                currentNumber = nums[i];
            }
            break;
        }
        return false;
    }
}