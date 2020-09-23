/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
*/

/*
FIRST SOLUTION
make a copy of the Array
sort the copied Array
starting with the largest number and descending 
compare all numbers until a result is found
find the results indices in the original array 
return indices
 



SECOND SOLUTION
make a hashtable from the array with the keys being the value of the array and the values being the indices
make a copy of the array and sort the copied array
starting at the highest value calculate the difference between the target and value and check if difference is in hashtable
if no difference is found move to next one
can exclude and values in array that are larger that target


THIRD SOLUTION
BRUTE FORCE
using nested for loops (i, j) itertate over each value in the array comparing to see if sum == target
if i + j == target ? [i, j] : return "there is no match"

*/

const solution1 = (nums, target) => {
	let arr1 = [...nums];
	arr1.sort();

	for (let j = arr1.length - 1; j > 0; j--) {
		for (let i = 0; i < arr1.length; i++) {
			if (arr1[j] + arr1[i] == target) {
				if (arr1[j] == arr1[i]) {
					let firstInd = nums.indexOf(arr1[i]);
					for (let k = firstInd + 1; k < nums.length; k++) {
						if (nums[k] == arr1[j]) {
							return [firstInd, k];
						}
					}
				}
				return [nums.indexOf(arr1[i]), nums.indexOf(arr1[j])];
			}
		}
	}
};

const solution2 = (nums, target) => {
	let dict = {};

	for (let i = 0; i < nums.length; i++) {
		if (!(nums[i] in dict)) {
			dict[nums[i]] = [];
		}
		dict[nums[i]].push(i);
	}

	for (let i = 0; i < nums.length; i++) {
		let difference = target - nums[i];
		if (difference in dict) {
			if (difference == nums[i] && dict[difference].length > 1) {
				return dict[difference];
			} else if (dict[difference][0] == i) {
				continue;
			} else {
				return [dict[difference][0], i];
			}
		}
	}
};

function solution3(nums, target) {
	for (let i = 0; i < nums.length; i++) {
		for (let k = i + 1; k < nums.length; k++) {
			if (nums[i] + nums[k] == target) {
				return [i, k];
			}
		}
	}
}
