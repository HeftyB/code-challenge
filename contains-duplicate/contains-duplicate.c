# include <stdio.h>
# include <stdbool.h>
// # include <cs50.h>


/*
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

*/

// # in order to check if an array contains any duplicates:

// # FIRST SOLUTION
// # make a set from the array (set will ignore duplicates)
// # compare length of set to length of array
// # if length is == return true else return false


// # SECOND SOLUTION
// # make a hashtable for the array with each item as the key and a count of occurances as valuus
// # loop through the hashtable and return true if any value is > 0

// # THIRD SOLUTION
// # LOOP THROUGH EACH ITEM IN THE ARRAY
// # FOR EACH ITERATION OF LOOP LOOP THROUGH THE WHOLE ARRAY AGAIN(EXCLUDING CURRENT ITEM) AND RETURN TRUE IF A MATCH IS FOUND

bool containsDuplicate(int[], int);

int main (void)
{
    int newArray[1000000];

    for (int i = 0; i < 1000000; i++) {
        newArray[i] = i;
    }

    newArray[998000] = 999000;

    containsDuplicate(newArray, 1000000);   
    return 0; 
}

bool containsDuplicate(int nums[], int numsSize){

    // int length = sizeof(nums) / sizeof(nums[0]);
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++){
            // printf(" i is %i , j is  %i\n", i, j);
            if (nums[i] == nums[j]) {
                printf("True");
                return true;
            }
        }
    }
    printf("False");
    return false; 
}