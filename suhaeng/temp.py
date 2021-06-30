def Fahrenheit_celcius(x):
    result = 0
    temp = input("화씨는 F, 섭씨는 C를 표기해 주세요 : ")
    if temp == 'C':
        result = x*1.8+32
        print("섭씨 "+str(x)+"를 화씨로 ->"+str(result))
        return str(result)
    elif temp == 'F':
        result = (x-32)/1.8
        print("화씨 " +str(x)+ "를 섭씨로 ->" + str(result))
        return str(result)

Fahrenheit_celcius(30)