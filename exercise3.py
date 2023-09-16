# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

def find_maximum_adjacent_pairs(data):
    list_max_values = []

    #Not enough elements to form adjacent pairs
    if len(data) < 2:
        return []
    
    for i in range(len(data) - 1): 
        maximum = max(data[i], data[i+1])
        list_max_values.append(maximum)

    return list_max_values
    
print(find_maximum_adjacent_pairs(data3))
