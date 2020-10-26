

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def solution1(strs):
    # loop through each string in list
    # check each index of string to see if char == index in rest of string
    # when match is not found return string sliced ending with i'th char
    # if no matches are found return empty string
    
    if len(strs) == 0:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    for i in strs:
        if len(i) == 0:
            return ""
        
    for i in range(len(strs[0])):
        let = strs[0][i]
        for j in strs:
            if i == len(j):
                return j
            if j[i] != let:
                # if i == 0:
                #     return j
                return j[:i]
            
    return strs[0]
    
test_data = strs = ["flower","flow","flight"]

print(solution1(test_data))