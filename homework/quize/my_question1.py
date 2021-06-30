def change(char,*chars):
    num = chars[0]
    print("입력된 문자:",char)
    print("반복 출력할 번수:",num,"번")
    for a in chars:
        print(char*a)
    print(str(num)+"번 출력했습니다.")

change("★",3)
