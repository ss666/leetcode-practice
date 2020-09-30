#dp:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [float("-inf")] * l 
        dp[0]=nums[0]
        
        for i in range(1,l):
                dp[i]=max(dp[i-1]+nums[i],nums[i])
                
        return max(dp)



#divide and conquer:
 class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #从中间值开始，起始位置为中间下标，一部分向左求和，另一部分向右求和，最终两部分相加即可
        def max_crossing_sum(left, right, mid):
            left_sum = right_sum = 0
            sml = smr = float("-inf")
            for i in range(mid,left-1,-1):
                left_sum += nums[i]
                if left_sum > sml:
                    sml = left_sum
            for i in range(mid+1,right+1,1):
                right_sum += nums[i]
                if right_sum > smr:
                    smr = right_sum

            return max(sml+smr, sml, smr) 
                
     
        def max_subarray_sum(left,right):
            if left==right:
                return nums[left]
            mid = (left+right) // 2
            left_sum = max_subarray_sum(left, mid)
            right_sum = max_subarray_sum(mid+1, right)
            crossing_sum = max_crossing_sum(left, right, mid)      
            return max(left_sum, right_sum, crossing_sum)

        
        l = len(nums)
        return max_subarray_sum(0, l-1)
        