 #leetcode 455. Assign Cookies
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        childi, cookiej = 0, 0
        while childi < len(g) and cookiej < len(s):
            if s[cookiej] >= g[childi]:
                childi += 1
            cookiej += 1
        return childi
 '''
 time complexity: O(nlogn + nlogn + n) = O(nlogn)       sort(timesort/O(nlogn)
 '''
 
 #leetcode 376. Wiggle Subsequence
 class Solution:    #保留连续递增/递减序列的首尾元素
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <2:
            return len(nums)
        BEGIN, UP, DOWN = 0,1,2
        STATE = BEGIN
        max_length = 1
        for i in range(1, len(nums)):
            if STATE == 0:
                if nums[i-1] < nums[i]:
                    STATE = 1
                    max_length +=1
                elif nums[i-1] > nums[i]:
                    STATE = 2
                    max_length +=1
            if STATE == 1:
                if nums[i-1] > nums[i]:
                    STATE = 2
                    max_length +=1
            if STATE == 2:
                if nums[i-1] < nums[i]:
                    STATE = 1
                    max_length +=1
        return max_length

        
 #leetcode 402. Remove K Digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        res = ''
        nums = list(map(int,num))  
        for i in range(len(nums)):  #尽可能让得到的数字优先最高位最小：从高位向低位遍历num,遍历数字小于栈顶元素，将栈顶元素pop出栈，否则将遍历数字push入栈
            while len(s)!= 0 and s[len(s)-1]>nums[i] and k>0:
                s.pop(-1)
                k -= 1
            if nums[i] != 0 or len(s)!=0:   #栈为空时，不能填0
                s.append(nums[i])
        while k!= 0 and len(s)!=0:  #所有数字扫描完，k仍大于0
                s.pop(-1)
                k -= 1
        res = ''.join(str(i) for i in s)
        return '0' if res == '' else res
