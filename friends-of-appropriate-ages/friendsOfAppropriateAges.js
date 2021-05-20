/*

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 


*/


/**
 * @param {number[]} ages
 * @return {number}
 */
 var numFriendRequests = function(ages) {
    let counter = 0;
    // let i = 0;
    
    let sorted = [...ages];
    
    sorted.sort((a, b) => a - b);
    
    for (let k = 0; k < ages.length; k++) {
        
        let index = sorted.lastIndexOf(ages[k]);
        let con1 = 0.5 * ages[k] + 7;
        let underHun = ages[k] < 100
        
        for (let j = 0; j < index; j++) {
            if (sorted[j] <=  con1) continue;
            if (sorted[j] > ages[k]) continue;
            if (sorted[j] > 100 && underHun) continue;
            
            counter++;
        }
    }
    
    
    /*
        dictonary with index as key and arry as val
        arr[0] condition 1
        arr[1] condition 2
        arr[2] condition 3
        
        age[b] must be in range of [con1, age[a]]
        
        loop once, map
        loop 2nd time count
    */
    

    
    return counter;
};