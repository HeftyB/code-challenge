"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

*/
"""

# Given a pair of linked list when combined representing a whole number,
# (digits in number are represented in reverse order in the linked list),
# return the sum of the two numbers as a linked list.  

# FIRST SOLUTION
# going through each linked list we can store the values in an Array,
# then traverse backwards in the array or reverse the array, 
# then combine each value into an integer

# once both integers are defined then add the values 
# and return the sum in linked list form

# SECOND SOLUTION
# traverse through both linked list at the same time adding the values together along the way 
# each sum of linked list would be added to the total by multiples of ten incrementing as traversal
# return total sum as a linked list 

# THIRD SOLUTION


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def first_solution (l1, l2):
    list1 = []
    list2 = []

    current = l1
    
    list1.append(current.val)

    while current.next:
        list1.append(current.next.val)
        current = current.next

    currents = l2
    list2.append(currents.val)

    while currents.next:
        list2.append(currents.next.val)
        currents = currents.next

    num1 = 0
    num2 = 0

    for index, i in enumerate(list1):
        if index == 0:
            list1[index] = i
            continue
        list1[index] = i * (10**index)
        
    for index, i in enumerate(list2):
        if index == 0:
            list2[index] = i
            continue
        list2[index] = list2[index] * (10**index)
        
    for i in list1:
        num1 += i

    for i in list2:
        num2 += i
    
    sums = str(num1 + num2)
    
    sum = []
    
    for c in sums:
        sum.insert(0, c)
    
    starting_node = ListNode(int(sum[0]))
    current = starting_node
    
    
    for i in range(1, len(sum)):
        new_node = ListNode(sum[i])
        current.next = new_node
        current = new_node
        
    return starting_node
        