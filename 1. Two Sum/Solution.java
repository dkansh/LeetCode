import java.util.Map;
import java.util.HashMap;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; i++) {
            Integer index = map.get(nums[i]);
            if(index == null) {
                map.put(target-nums[i], i);
            }else {
                return new int[]{index, i};
            }
        }
        return new int[]{};
    }
}