/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.





/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */


// Given a pair of linked list representing a whole number combined,
// (digits in number are represented in reverse order in the linked list),
// return the sum of the two numbers as a linked list.  

// FIRST SOLUTION
// going through each linked list we can store the values in an Array,
// then traverse backwards in the array or reverse the array, 
// then combine each value into an integer

// once both integers are defined then add the values 
// and return the sum in linked list form

// SECOND SOLUTION
// traverse through both linked list at the same time adding the values together along the way 
// each sum of linked list would be added to the total by multiples of ten incrementing as traversal
// return total sum as a linked list 

// THIRD SOLUTION

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}


function firstSolution (l1, l2) {
    list1 = [];
    list2 = [];

    current = l1;
    
    list1.push(current.val)

    while (current.next) {
        list1.push(current.next.val);
        current = current.next;
    }

    currents = l2;
    
    list2.push(currents.val)
    
    while (currents.next) {
        list2.push(currents.next.val);
        currents = currents.next;
    }


    list1.reverse()
    list2.reverse()
    
    num1 = parseInt(list1.join(""), 10)
    num2 = parseInt(list2.join(""), 10)
    
    sum = num1 + num2
    
    sum = sum.toString()
    
    let returns = ListNode(sum[0], sum[1])
    
    for (let i = 1; i < sum.length; i++) {
        ListNode(sum[i], sum[i + 1])
    }
    return returns
}


ls1 = new ListNode(2, new ListNode(3, new ListNode(3)));
ls2 = new ListNode(5, new ListNode(6, new ListNode(4)));

console.log(ls1)
console.log(ls2)

// console.log(firstSolution(ls1, ls2));