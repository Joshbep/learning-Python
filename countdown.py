def countdown(num):
    if num < 2:
        return str(num)
    return str(num)+ " "+countdown(num-1)