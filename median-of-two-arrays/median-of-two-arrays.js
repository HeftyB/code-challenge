/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

*/




// STIILL GOT MINOR BUGS TO WORK OUT!!!!



var findMedianSortedArrays = function(nums1, nums2) {
    
    let length = nums1.length + nums2.length;
    let counter1 = 0;
    let counter2 = 0;
    let median = Math.floor(length / 2);
    let previous = 0;
    let isEven = length % 2 == 0;
    let justNum2 = false;
    let justNum1 = false;
    
    if (nums1.length == 0) {
        if (isEven) {
            return (nums2[median - 1] + nums2[median]) / 2;
        }
        return nums2[median];
    }
    
    else if (nums2.length == 0) {
        if (isEven) {
            return (nums1[median - 1] + nums1[median]) / 2;
        }
        return nums1[median];
    }
    
    for (let i = 0; i < median + 1; i++) {
        console.log("loop")
        if (justNum2) {
            if (i == median) {
                if (isEven) {
                    return (nums2[counter2] + previous) / 2;
                }
                return nums2[counter2];
            }
            previous = nums2[counter2];
            counter2++;
            continue
        }
        
        if (justNum1) {
            if (i == median) {
                if (isEven) {
                    return (nums1[counter1] + previous) / 2;
                }
                return nums1[counter1];
            }
            previous = nums1[counter1];
            counter1++;
            continue;
        }
        
        if (i == median) {
            if (isEven) {
                if (nums1[counter1] <= nums2[counter2]) {;
                    return (nums1[counter1] + previous) / 2
                } else {
                    return (nums2[counter2] + previous) / 2;
                }
            } else {
                if (nums1[counter1] > nums2[counter2]) {
                    return nums2[counter2];
                } else {
                    nums1[counter1];
                }
            }
        }
        
        
        if (nums1[counter1] <= nums2[counter2]) {
            previous = nums1[counter1];
            if (counter1 == nums1.length - 1) {
                justNum2 = true;
                continue
            }
            counter1++;
                continue
        }
                
        if (nums1[counter1] > nums2[counter2]) {
            previous = nums2[counter2];
            if (counter2 == nums2.length - 1) {
                justNum1 = true;
                continue
            }
            counter2++;
        }
    
    }
};