def day_to_weekday(a):
        weekday = " "
        if a%7==1:
            weekday = "월요일"
        elif a%7==2:
            weekday = "화요일"
        elif a%7==3:
            weekday = "수요일"
        elif a % 7 == 4:
            weekday = "목요일"
        elif a % 7 == 5:
            weekday = "금요일"
        elif a % 7 == 6:
            weekday = "토요일"
        elif a % 7 == 0:
            weekday = "일요일"


        return weekday

for i in range(1, 31):
    print(day_to_weekday(i))