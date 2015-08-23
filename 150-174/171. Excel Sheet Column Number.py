'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        a=0
        for i in s:
            a=a*26+ord(i)-64
        return a
