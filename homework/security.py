def social_security_number(number):
    if (number[12:14]) == '00':
        return number +' 지역 : 서울'
    elif (number[12:14]) == '01':
        return number +' 지역 : 경기도'
    elif (number[12:14]) == '02':
        return number +' 지역 : 인천'
    elif (number[12:14]) == '03':
        return number + ' 지역 : 충청북도'
    elif (number[12:14]) == '04':
        return number +' 지역 : 전라북도'
    elif (number[12:14]) == '05':
        return number +' 지역 : 경상도'
    elif (number[12:14]) == '06':
        return number +' 지역 : 부산'
    elif (number[12:14]) == '06':
        return number +' 지역 : 강원도'
    elif (number[12:14]) == '06':
        return number +' 지역 : 충청남도'
    elif (number[12:14]) == '06':
        return number +' 지역 : 전라남도'
    elif (number[12:13]) == '1':
        return number +' 지역 : 제주도'

S = social_security_number('030713-4101111')
print(S)
