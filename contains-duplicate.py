"""

 Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""
# in order to check if an array contains any duplicates:

# FIRST SOLUTION
# make a set from the array (set will ignore duplicates)
# compare length of set to length of array
# if length is == return true else return false


# SECOND SOLUTION
# make a hashtable for the array with each item as the key and a count of occurances as valuus
# loop through the hashtable and return true if any value is > 0

# THIRD SOLUTION
# LOOP THROUGH EACH ITEM IN THE ARRAY
# FOR EACH ITERATION OF LOOP LOOP THROUGH THE WHOLE ARRAY AGAIN(EXCLUDING CURRENT ITEM) AND RETURN TRUE IF A MATCH IS FOUND


input1 = [1,2,3,1]
input2 = [1,2,3,4]
input3 = [1,1,1,3,3,4,3,2,4,2]

def first_solution (arr):
    new_set = set(arr)
    if len(new_set) == len(arr):
        return False
    else:
        return True

# print(f"First Solution")
# print(first_solution(input1))
# print(first_solution(input2))
# print(first_solution(input3))


def second_solution (arr):
    arrDict = {}

    for i in arr:
        if i not in arrDict:
            arrDict[i] = 0

        arrDict[i] += 1

    for key, value in arrDict.items():
        if value > 1:
            return True

    return False


# print(f"Second Solution")
# print(second_solution(input1))
# print(second_solution(input2))
# print(second_solution(input3))

def third_solution (arr):
    for i in range(len(arr)):
        for j in arr[i + 1:]:
            if arr[i] == j:
                return True

    return False


print(f"Third Solution")
print(third_solution(input1))
print(third_solution(input2))
print(third_solution(input3))