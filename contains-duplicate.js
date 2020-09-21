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


input1 = [1,2,3,1];
input2 = [1,2,3,4];
input3 = [1,1,1,3,3,4,3,2,4,2];

const firstSolution = arr => {
    newSet = new Set(arr);
    if (newSet.size == arr.length) {
        return false;
    } else {
        return true;
    }
}

// console.log(firstSolution(input1));
// console.log(firstSolution(input2));
// console.log(firstSolution(input3));


function secondSolution (arr) {
    newOb = {};

    for (let i = 0; i < arr.length; i++) {
        if (!(arr[i] in newOb)) {
            newOb[arr[i]] = 0;
        }

        newOb[arr[i]]++;
    }

    for (const key in newOb) {
        if (newOb[key] > 1) {
            return true;
        }
    }

    return false;
}


// console.log(secondSolution(input1));
// console.log(secondSolution(input2));
// console.log(secondSolution(input3));


const thirdSolution = (arr) => {
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] == arr[j]) {
                return true;
            }
        }
    }
    return false;
}

// console.log(thirdSolution(input1));
// console.log(thirdSolution(input2));
// console.log(thirdSolution(input3));