class love:
    def __init__(self,name1,persent1,name2,persent2):
        self.name1=name1
        self.persent1=persent1
        self.name2 = name2
        self.persent2 = persent2

    def good_love(self):
        print(self.name1+"와 "+self.name2+"의 궁합을 봅니다")

    def love_persent(self):
        sum = self.persent1+self.persent2
        if sum>=90:
            print("이 둘은 최고의 궁합! 점수는 "+str(sum)+"점!")
        elif sum>=80:
            print("정말 잘맞아! 좋은 친구인걸~ 점수는 "+str(sum)+"점!")
        elif sum>=70:
            print("좋은데~ 괜찮은 사이야! 점수는 "+str(sum)+"점!")
        elif sum>=60:
            print("나쁘지 않아! 하지만 좀 어색한데~ 점수는 "+str(sum)+"점!")
        elif sum<=50:
            print("음 둘이 안친해? 괜찮은거야? 점수는 "+str(sum)+"점!")
        return sum

love_person = love("박재연", 16,"김나현",73)
love_person.good_love()
love_person.love_persent()