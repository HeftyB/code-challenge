/*
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
*/

function cheatingSolution (nums, target) {
    return nums.indexOf(target);
}