class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [float("-inf")] * l 
        dp[0]=nums[0]
        
        for i in range(1,l):
                dp[i]=max(dp[i-1]+nums[i],nums[i])
                
        return max(dp)