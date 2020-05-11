#Single Number:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        countNum = dict()
        for i in nums:
            if i in countNum:
                countNum[i] = countNum[i] + 1
            else:
                countNum[i] = 1;             
        for e,v in countNum.items():
            if v == 1:
                return e
'''
access dictionary items:
    dict[key]
    dict.get(key, [default])
    for item in dict.items():
    for key, value in dict.items():
    for key in dict.keys():
    for value in dict.values():
'''

# bitwise solution: binary XOR. Consider in Boolean algebra form
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
    
#Single Number 2:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a,b = 0,0
        for i in nums:
            a = (a^i) & ~b
            b = (b^i) & ~a 
        return a
'''
We need 2 bits to store 3 states: 对于重复元素x, 第一次碰到赋值给a, 第二次碰到赋值给b, 第三次碰到全部消除，即 a^ num, b^nums; 
  a b
0 0 0
1 x 0
2 0 x
3 0 0
'''

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        return list(set(nums[::3]) - set(nums[1::3]))[0]

#Single Number 3:
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        countNum = dict()
        for i in nums:
            if i in countNum:
                countNum[i] += 1
            else:
                countNum[i] = 1
                
        res = list()
        for e,v in countNum.items():
            if v==1:
                res.append(e)
        return res
            
class Solution2:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        return list(set(nums[::2]) ^ set(nums[1::2]))


    


