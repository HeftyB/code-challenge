// Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

// There is only one duplicate number in nums, return this duplicate number.

// Follow-ups:

// How can we prove that at least one duplicate number must exist in nums? 
// Can you solve the problem without modifying the array nums?
// Can you solve the problem using only constant, O(1) extra space?
// Can you solve the problem with runtime complexity less than O(n2)?
 

// Example 1:

// Input: nums = [1,3,4,2,2]
// Output: 2
// Example 2:

// Input: nums = [3,1,3,4,2]
// Output: 3
// Example 3:

// Input: nums = [1,1]
// Output: 1
// Example 4:

// Input: nums = [1,1,2]
// Output: 1



// FIRST SOLUTION - NAIVE
// LOOP THROUGH ARRAY
// EACH ITERATION, NESTED LOOP THROUGH REST OF ARRAY TO CHECKING FOR MATCH


// SECOND SOLUTION
// LOOP THROUGH ARRAY ADDING EACH VALUE TO A HASHSET/DICT W/ A COUNTER OF OCCURENCES,
// LOOP THROUGH DICT AND RETURN KEY WITH VALUE > 1

// THIRD SOLUTION
// SORT ARRAY THEN LOOP THROUGH ARRAY CHECKING NEXT INDEX FOR A MATCH UP TO [-2] 