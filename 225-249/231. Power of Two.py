'''
Given an integer, write a function to determine if it is a power of two.
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n and n&(n-1)==0)
