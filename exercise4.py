# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

def combinate_three_digits(list):
    #if arr < 3, cannot combinate
    if len(list) < 3:
        return "cannot combinate"
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and i!=k):
                    print(list[i], list[j], list[k])

print(combinate_three_digits(data4))
