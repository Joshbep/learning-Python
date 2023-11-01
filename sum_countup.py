# def sum_countup(num):
#     reutrn num + num - 1 to get the sum

def sum_countup(num):
    if num < 2:
        return num
    return sum_countup(num-1) + num
print(sum_countup(1))