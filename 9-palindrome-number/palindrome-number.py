class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!= s[j]:
                return False
            i = i+1
            j = j-1 
        return True


        