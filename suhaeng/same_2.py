# def solution(characters):
#     result = ""
#     result += characters[0]
#     for i in range(1,len(characters)):
#         if characters[i-1]!= characters[i]:
#             result += characters[i]
#     return result
# characters = "aaaabbbb"
# print(solution(characters))


def solution3(ch):
    result = ""
    result += ch[0]
    for i in range(1, len(ch)):
        if ch[i-1]!=ch[i]:
            result +=ch[i]
    return result

def solution1(characters1):
    for i in range(len(characters1)-1):
        for j in range(i+1, len(characters1)):
            if characters1[i] == characters1[j]:
                return True
    return False
#
# def solution(str1):
#     input_list = list(str1)
#     result_list = []
#     for i in range(len(input_list)):
#         if i == 0:
#             result_list.append(input_list[i])
#         elif result_list[-1] != input_list[i]:
#             result_list.append(input_list[i])
#     return ''.join(result_list)

# print(solution("aaaab"))
#
# characters1 ='aaaaahhhhh'
# print(solution(characters1))

# def zip(sentence):
#     count = 0   # 문자를 세기 위한 변수
#     next = ""   # sentence가 달라지는 곳을 감지하는 수단
#     result = "" # 결과를 저장하는 공간
#     for i in sentence:
#         if next != i:
#             next = i
#
#             if count:
#                 result += str(count)
#             result += i
#             count = 1
#         else:
#             count += 1
#     if count:
#         result += str(count)
#     return result

def countOverlap(characters):
    result = []
    firesult =[]
    result += characters[0]
    for i in range(1,len(characters)):
        if characters[i-1]!= characters[i]:
            result.append(characters[i])
        else:
            cnt = characters.count(characters[i])
            result.append(cnt)
    for i in range(0,len(result)-1):
        if result[i - 1] != result[i]:
            firesult.append(str(result[i]))
    return ''.join(firesult)

print(countOverlap("ddaaappaad"))