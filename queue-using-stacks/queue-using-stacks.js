/*
"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
"""
*/

// # SOLUTION 1

// # use an array as a stack container

// # push - using a temporary stack pop all items from original stack
// # add new item to empty original stack
// # pop the items off the temp stack back on to original

// # pop - using pop() return .pop(0)

// # peek - return value at index 0 of stack array

// # empty - return true if length of stack array is == 0


stack = [];

let push = x => stack.push(x);
let peek = () => stack[0];
let pop = () => stack.shift();
let empty = () => stack.length == 0 ? true : false