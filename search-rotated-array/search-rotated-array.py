"""
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""

"""

FIRST SOLUTION - NAIVE
iterate through array looking for target and return

SECOND SOLUTION
check edges of array, if target < index[0] and > index[-1] reutrn -1 if true else
if target < index[0] && index[-1] iterate backwards until target is found or value @ index < index - 1 else
if target > index[0] iterate forwards until target is found or value > value @ index + 1


THIRD SOLUTION
index of pivot point in array cant be any greater than value of index[0] or value of index[-1] 
calculate and traverse backwards to find

if value > index[0] calculate difference compare with pivot index
if pivot index  is out if range check the index of the difference(the maximum number of index's away that target could possibly be) and interate backwards to target
if pivot index is in range then seach between index[1] and pivot index[-1]

"""




def first_solution (nums, taget):
    for index, i in enumerate(nums):
        if i == target:
            return index
    return -1




def cheating_solution (nums, target):
    if target not in nums:
        return - 1
    return nums.index(target)





def second_solution (nums, target):


    def inner_function (nums, target, start=0, end=-1):
        if len(nums) == 0:
            return -1

        if target == nums[start]:
            return start

        if target == nums[end]:
            if end == -1:
                return len(nums) - 1
            return end

        current_index = start + (end - start) // 2

        if nums[current_index] == target:
            return current_index

        elif start is end:
            return -1

        elif target > nums[current_index]:
            return second_solution(nums, target, current_index + 1, end - 1)

        elif target < nums[current_index]:
            return second_solution(nums, target, start + 1, current_index - 1)
    



    # if target < nums[0] and target > nums[-1]:
    #     return -1
    # if target == nums[0]:
    #     return 0
    # if target == nums[-1]:
    #     return len(nums) - 1
    
    # start = 0
    # end = len(nums) - 1
    # if target > nums[0]:
    #     midde = start + (end - start // 2)

    #     if nums[middle] == target:
    #         return middle
        
    #     if nums[start] == target:
    #         return start

    #     if nums[end] == target:
    #         return end

    #     if (middle - start <= 1) and (end - middle <= 1):
    #         return -1
        
    #     if nums[middle] > target:
    #         end = middle - 1
    #         start += 1

    #     if nums[middle] < target:
    #         pass







        




def third_solution (nums, target):
    # find out pivot index
    # check value of index[0]
    # store value as possible index from [-1]
    # check index len(num) - possible_index + 1
    # if value > index[0] check middle index between value and index[-1] to determing which way to go
    # keep checking until value < value[index - 1

    pivot_index = nums[0]
    end_index = len(nums) - 1

    max_pivot_index = end_index - pivot_index
    middle = None

    while True:
        if nums[end_index - max_pivot_index] < nums[(end_index - max_pivot_index) - 1]:
            pivot_index = max_pivot_index + (end_index - max_pivot_index) // 2
        difference = 
        elif nums[]

    def find_pivot (num):

        start = nums[0]
        end num[-1]

        if         


[6, 7, 8, 9, 0, 1, 2, 3, 4, 5]

start_neg_ind = nums[0] * -1
end_neg_ind = -1
middle_neg = start_neg_ind // 2

if
