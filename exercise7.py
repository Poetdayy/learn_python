# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

even_list = []

#Method: split number. VD: 1000 -> 1,0,0,0. Check each element in number %2
for number in range(1000,3000):
    num_str = str(number)

    #set_flag_even
    all_even = True

    for digit_char in num_str:
        digit = int(digit_char)
        if digit % 2 != 0:
            all_even = False
            break
    
    if all_even:
        even_list.append(number)

result_str = ",".join(map(str, even_list))
print(result_str)



