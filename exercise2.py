# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

def check_counteble_k(data, checkedNumber):
    countNumber = 0
    for number in data:
        if checkedNumber == number:
            countNumber +=1
    return countNumber

new_list = []
new_list = [number for number in data2 if (check_counteble_k(data2, number) > k) and (number not in new_list)]
print(new_list)

