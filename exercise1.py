''' 
Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
'''
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
positiveCount = 0
negativeCount = 0

def check_positive_and_negative(number):
    if number > 0:
        return 1
    elif number == 0:
        return 0
    elif number < 0:
        return -1

def count_positive_and_negative(data):
    global positiveCount
    global negativeCount
    for number in data:
        if check_positive_and_negative(number) == 1:
            positiveCount +=1
        elif check_positive_and_negative(number) == -1:
            negativeCount +=1

count_positive_and_negative(data1)
print('positive_count:', positiveCount, '& negative_count:', negativeCount)