# 더하기, 빼기, 곱하기, 나누기, 나머지구하기, 종료 기능이 있는 계산기 프로그램을 만들어 보시오.(두 개의 수를 사용한다.)
#
# 1.
# #문제
# plus 함수
# 인자값: 정수 2개
# 리턴값: 정수 2개의 합
#
# #함수호출코드
# print(plus(10, 20))
# #실행결과
# 30
#
# 2.
# #문제
# minus 함수
# 인자값: 정수 2개
# 리턴값: 정수 2개의 차
#
# #함수호출코드
# print(minus(10, 20))
# #실행결과
# -10
#
# 3.
# #문제
# multiply 함수
# 인자값: 정수 2개
# 리턴값: 정수 2개 나누기
#
# #함수호출코드
# print(multiply(10, 20))
# #실행결과
# 200
#
# 4.
# #문제
# divide 함수
# 인자값: 정수 2개
# 리턴값: 정수 2개 나누기
#
# #함수호출코드
# print(divide(10, 20))
# #실행결과
# 0.5
#
# 5.
# #문제
# rest 함수
# 인자값: 정수 2개
# 리턴값: 정수 2개 나눈 나머지
#
# #함수호출코드
# print(rest(55, 20))
# #실행결과
# 15
def Plus(a,b):
    sum = a+b
    return sum

def Minus(a,b):
    sum = a-b
    return sum
def multiply(a,b):
    sum = a*b
    return sum
def divide(a,b):
    sum = a/b
    return sum
def rest(a,b):
    sum = a%b
    return sum