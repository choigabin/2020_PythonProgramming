#369게임
#1~20까지
def count369(n):
    #count = 0
    #for ch in str(n) :
    #    #if ch == '3' or ch == '6' or ch == '9' :
    #    if ch in "369" :
    #        count += 1
    #return count
    n_string = str(n)
    return n_string.count("3")+n_string.count("6")+n_string.count("9")

for n in range(1, 100) :
    if n % 5 == 0:  #우선순위(제일 먼저 판단)
        print("뿌쑝!")
    else : #뿌쑝이 아닐 때
        #  숫자에 3, 6, 9가 있으면 개수 세기 -> count
        count = count369(n)
        #  count가 0이면, 숫자 출력
        if count == 0:
            print(n)
        #  count가 0이 아니면, count만큼 "짝" 출력
        if count != 0:
            print("짝"*count)
