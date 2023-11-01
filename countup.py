# countup(num)
#     return num if num is 1
#     return str(num) + countup(num+1)

def countup(num):
    if num < 2:
        return str(num)
    return countup(num-1)+" "+str(num)
print(countup(7))