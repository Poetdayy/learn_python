# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

def add_elements_into_array(list1, list2):
    if len(list1) != len(list2):
        return "Number of rows in matrix and elements list must match."
    
    result_list = []
    for i in range(len(list1)):
        first_element = list2[i][0]
        # use [] for add 2 matrix
        row = list1[i] + [first_element]
        result_list.append(row) 

    return result_list

print(add_elements_into_array(data5_list1, data5_list2))



    
    
