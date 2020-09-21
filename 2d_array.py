def i_sum (arr, x_index, y_index):
    sums = 0
    sums = sums + arr[y_index][x_index]
    sums = sums + arr[y_index][x_index + 1]
    sums = sums + arr[y_index][x_index + 2]
    sums = sums + arr[y_index + 1][x_index + 1]
    sums = sums + arr[y_index + 2][x_index]
    sums = sums + arr[y_index + 2][x_index + 1]
    sums = sums + arr[y_index + 2][x_index + 2]


    # print(f"x = {x_index}, y = {y_index}")
    # print((arr[x_index][y_index], arr[x_index + 1][y_index], arr[x_index + 2][y_index]))
    # print((arr[x_index + 1][y_index + 1]))
    # print((arr[x_index][y_index + 2], arr[x_index + 1][y_index + 2], arr[x_index + 2][y_index + 2]))
    # print(f"sums = {sums}")
    return sums


# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_list = []
    x_index = 0
    y_index = 0

    max_y = 3
    max_x = 3

    for i in range(4):

        sum_list.append(i_sum(arr, x_index, y_index))
        x_index = x_index + 1
        sum_list.append(i_sum(arr, x_index, y_index))
        x_index = x_index + 1
        sum_list.append(i_sum(arr, x_index, y_index))
        x_index = x_index + 1
        sum_list.append(i_sum(arr, x_index, y_index))
        x_index = 0
        y_index += 1

    sum_list.sort()
    
    return sum_list[-1]
