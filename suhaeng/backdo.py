# num = input("숫자를 입력하세요")
# newNumber =""
# max = 0
# min = 0
# for digit in num:
#     newNumber = digit + newNumber
# if (newNumber>num):
#     max = int(newNumber)
#     min = int(num)
# else:
#     max = int(num)
#     min = int(newNumber)
# plus = max+min
# minus = max - min
# print("덧셈",plus)
# print("뺄셈",minus)

num = input("숫자를 입력하세요 : ")
newNumber = ""
max =0
min =0
for digit in num:
    newNumber = newNumber+digit
if (newNumber>num):
    max= int(newNumber)
    min = int(num)
else:
    max = int(num)
    min = int(newNumber)
plus = max+min
minus = max-min

print("덧셈 : ",plus)
print("뺄셈 : ",minus)