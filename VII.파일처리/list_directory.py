#p228
#텍스트파일 : txt, html, xml
#이미지파일: jpg, png, gif,
import os
data = os.listdir('.')

for d in data:
    print(d)
    print("is directory? : "+str(os.path.isdir(d)))
    print("is file? : "+ str(os.path.isfile(d)))

#. : 상대경로
#(./)디렉터리 : 상대경로
#/ 디렉터리 : 절대경로
#c:/디렉터리 : 절대경로
#c:\ 디렉터리 : 절대경로