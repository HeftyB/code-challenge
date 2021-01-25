"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""
def solution1(grid):
        # loop through and map servers corodinates to Dictionary
        # while adding severs connected by same row to return set
        # loop through keys and map which columns have servers
        # loop through keys and check if column was active if so
        # add to set 
        # return len of set
        
#         serv_dict = {}
#         ret_set = new set()
        
#         for i in grid:
#             for j in i:
#                 if j == 1:
#                     ret_set.add

        if len(grid) == 0:
            return 0

        serv_dict = {}
        col_dict = {}
        row_dict = {}
        ret_set = set()
        
        for index, i in enumerate(grid):
            # row_servers = 0

            for dex, j in enumerate(i):
                if j == 1:

                    if dex not in col_dict:
                      col_dict[dex] = 0

                    col_dict[dex] += 1
                    
                    if index not in row_dict:
                        row_dict[index] = 0
                        
                    row_dict[index] += 1

                    serv_dict[(dex, index)] = True

        for key, value in serv_dict.items():
            
            if key[0] in col_dict and col_dict[key[0]] > 1:
                ret_set.add(key)
                
            if key[1] in row_dict and row_dict[key[1]] > 1:
                ret_set.add(key)
        
        return len(ret_set)



test_case = [[0,0,1,0,0],[1,0,1,0,0],[0,1,0,0,0],[1,0,0,1,0]]


print(solution1(test_case))



