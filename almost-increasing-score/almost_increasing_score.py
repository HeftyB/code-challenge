"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""


def almostIncreasingSequence(sequence):
   
    counter = 0
    
    sets = set(sequence)
    
    if len(sequence) - len(sets) > 1:
        return False
        
    if sequence[0] > sequence[-1] and sequence[1] > sequence[-2]:
        return False
        
    for index, i in enumerate(sequence):
        if index == len(sequence) - 1:
            continue    
        if not i < sequence[index + 1]:
            counter += 1
            
    if counter > 1:
        return False
    else:
        return True
