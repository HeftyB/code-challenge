/*

Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

 */

var secondHighest = function(s) {
    /*
        moke array of numerical digits
        sort
        return [-2]
        
        loop once
        check each char isNumeric()
        if true check agianst greatest
        if char is greater 2ndgreatest, greatest = greatest, char
        if this is first numerical digit set 2ndgreatest to char aswell.
    */
    
    
    // let numArr = [];
    // let sets = new Set();
    
    // for (let i = 0; i < s.length; i++) {
    //     if(!(isNaN(s[i]))) {
    //         if (sets.has(s[i])) continue;
            
    //         numArr.push(parseInt(s[i]));
    //         sets.add(s[i])
    //     }
    // }
    
    // numArr.sort((a, b) => a - b);
    // let l = numArr.length;
    
    // if (l < 2 || numArr[l - 2] === numArr[l - 1]) {
    //     return -1
    // }
    
    // return numArr[l - 2]


    let greatest = -1;
    let sgreatest = null;
    
    for (let i = 0; i < s.length; i++) {
        if(!(isNaN(s[i]))) {
            let n = parseInt(s[i]);
            
            if(n == greatest) continue;
            
            if (n > greatest) {
                sgreatest = greatest;
                greatest = n;
            }
            else if (n > sgreatest && n < greatest) {
                sgreatest = n;
            }
        }
    }
    
    if (sgreatest == null) {
        return -1;
    }
    
    return sgreatest;
};