def reverse_num(number):

    num = int(str(number)[::-1])
    plus = number+num

    if num >= number:
        minus = num - number
    else:
        minus = number - num

    mult = number * num

    if num >= number:
        divc = num / number
    else:
        divc = number/num

    result = plus, minus, mult, divc

    return result

print(reverse_num(15))
print(reverse_num(22))
print(reverse_num(73))