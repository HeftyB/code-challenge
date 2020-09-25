"""

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

"""


# SOLUTION 1
#  calculate total length of the arrays,
#  calculate median, if even 
#  for i in range (median)
#  compare arr1[counter1] to arr2[counter2] increment lowest value's counter
# when counter1 + counter2 == median return the lowest value between counter1 and counter 2
# if length is even then return the value calculated above + the previous value / 2

def solution1 (nums1, nums2):
    length = len(nums1) + len(nums2)
    counter1 = 0
    counter2 = 0
    median = length // 2
    previous = 0
    is_even = length % 2 == 0
    just_num2 = False
    just_num1 = False

    if len(nums1) == 0:
        if is_even:
            return (nums2[median - 1] + nums2[median]) / 2 
        return nums2[median]

    elif len(nums2) == 0:
        if is_even:
            return (nums1[median - 1] + nums1[median]) / 2
        return nums1[median]

    for i in range(median + 1):

        if just_num2:
            if i == median:
                if is_even:
                    return (nums2[counter2] + previous) / 2
                return nums2[counter2]
            previous = nums2[counter2]
            counter2 += 1
            continue
            
        if just_num1:
            if i == median:
                if is_even:
                    return (nums1[counter1] + previous) / 2
                return nums1[counter1]
            previous = nums1[counter1]
            counter1 += 1
            continue


        if i == median:
            if is_even:
                if nums1[counter1] <= nums2[counter2]:
                    return (nums1[counter1] + previous) / 2
                else:
                    return (nums2[counter2] + previous) / 2
            else:
                if nums1[counter1] > nums2[counter2]:
                    return nums2[counter2]
                return nums1[counter1]     
                
        if nums1[counter1] <= nums2[counter2]:
            previous = nums1[counter1]
            if counter1 == len(nums1) - 1:
                just_num2 = True
                continue
            counter1 += 1
            continue

        if nums1[counter1] > nums2[counter2]:
            previous = nums2[counter2]
            if counter2 == len(nums2) - 1:
                just_num1 = True
                continue
            counter2 += 1
            