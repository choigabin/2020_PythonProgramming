def is_prime_number(number):
    count =0
    for i in range(1, number):
        if number % 1 ==0:
            count+=1
    if count == 2:
        return "소수입니다."
    else:
        return "소수가 아닙니다."

print(is_prime_number(3))
print(is_prime_number(6))