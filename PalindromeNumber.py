class Solution:
    def isPalindrome(self, x:int) -> bool:
        if(x<0):
            return False
        return str(x) == str(x)[::-1]
                       # ''.join(reversed(str(x)))
                        '''
                         1.slice() parameters: start/stop/step
                         2.reversed() function: returns an iterator that
                        accesses the given sequence in the reverse order.
                        We have to convert the iterators to list or merge
                        all characters resulting from the reversed iteration
                        into a new string.
                        '''
