
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        max_length = 0
        start = 0
        st = [[False]* length for _ in range(length)]
        for i in range(length):
            for j in range(i+1):
                if i == j:
                    st[i][j] = True
                elif s[i] == s[j] :
                    if i-j < 3:
                        st[i][j] = True
                    else:
                        st[i][j] = st[i-1][j+1]

                if st[i][j] == True and i-j+1 > max_length:
                    max_length = i-j+1
                    start = j

        return s[start:start+max_length]


'''
1 5 3 5 1
j . . i
  j . i
    j i
    
list comprehension:
list(map(lambda _:[1] *3, range(3)))
[[1]*3 for _ in range(3)]
'''
