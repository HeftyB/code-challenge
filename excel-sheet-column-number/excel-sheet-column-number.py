"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    """

def solution_one(s):
    # convert string into base26 
    column_dict = {}
    start = 65
    for i in range(1, 27):
        column_dict[chr(start)] = i
        start += 1
    for index, c in enumerate(s[::-1]):
        if index == 0:
            num = column_dict[c]
        else:
            num += 26**index * column_dict[c]
        print(num)
    return num