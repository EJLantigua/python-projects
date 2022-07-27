def power(base, num):
    if num > 0:
        return base * power(base, num - 1)
    else:
        return 1

print(power(5,3))
