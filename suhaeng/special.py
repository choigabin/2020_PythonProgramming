# def solution(sentence):
#     sentence = []
#     n = int(input())
#     for i in range(n):
#         sentence.append(input())
#     result = solution(sentence)
#     for r in result:
#         print(r)
#     result = []
#     for sen in sentence:
#         temp = ""
#         for s in sen:
#             if s in ", .?!":
#                 temp += s
#         if temp /== "":
#             result.append("특정한문자가없습니다.")
#         else:
#             result.append(temp)
#         return result

def SpecialCharsolution(str):
    result = []
    for s in str:
        temp = ""
        for d in s:
            if d in ",.?!":
                temp += d
        if temp == "":
            result.append("특정한 문자가 없습니다.")
        else:
            result.append(temp)
    return result
d = "fusof!!!..!!"
print(SpecialCharsolution(d))