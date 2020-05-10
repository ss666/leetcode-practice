#Integer to Roman
class Solution:
    def intToRoman(self, num:int) -> str:
        RomanDict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90: 'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res =''
        for i in RomanDict:
            if num // i != 0:
                res = res + RomanDict[i] * (num // i)
                num = num % i
        return res
        
#Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        RomanDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)-1):
            if RomanDict[s[i]] < RomanDict[s[i+1]]:
                res = res - RomanDict[s[i]]
            else:
                res = res + RomanDict[s[i]]
        return res + RomanDict[s[-1]]
    
'''
 1.Greed Algorithms: 适用于难以找到全局最优解的复杂问题。把求解问题拆分为若干子问题，求解子问题的局部最优解，进行合并。贪心算法所求得的解不一定是全局最优解，贪心策略的选择需满足无后效性
 2.Besides hastables, another way to implement dictionaries is red-black tree. A hastable performs a lookup in O(1):O(n) time. A red-black tree performs a lookup in 0(log n) time. Hashtables have better performance at small sizes and are more easier to implement.
 3.Mechanisms to reslove collisions: open addresssing or separate chaining.
 '''
