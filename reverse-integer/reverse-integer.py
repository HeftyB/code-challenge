"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Accepted
1,234,666
Submissions
4,782,883
"""

def solution_one (x):
    string = str(x)
    string = list(string)
    if x < 0:
        string = string[1:]
    ints = 0
    
    for index, i in enumerate(string):
        if index == 0:
            print(i)
            ints += int(i)
        else:
            ints += int(i) * (10**index)
    if ints > 0b01111111111111111111111111111111:
        return 0
    if x < 0:
        ints *= -1
    return ints

