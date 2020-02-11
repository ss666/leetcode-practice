class Solution{
    public int[] twoSum(int[] nums, int target){
        HashMap<Integer,Integer> table = new HashMap<>();
        for(int i = 0; i<nums.length; i++)
            table.put(nums[i], i);
        for(int i = 0; i<nums.length; i++){
            int res = target - nums[i];
            if(table.containsKey(res) && table.get(res)!=i)
                return new int[]{i,table.get(res)};
        }
        throw new IllegalArgumentException();
    }
}
    
    
    