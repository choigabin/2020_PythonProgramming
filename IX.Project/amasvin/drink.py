class Drink:
    _CUP_SIZES = ['레귤러', '점보']
    _ICES = ['0%', '50%', '기본', '150%']
    _SUGARS = _ICES

    def __init__(self, name, price):
        self.name = name
        self.price = price
        # 0은 레귤러, 1은 점보
        self.cup_size = 0
        # 0은 0%, 1은 50%, 2는 기본, 3은 150%
        self.ice = 2
        self.sugar = 2

    def __str__(self):
        return f'이름 : {self.name}\t 가격 : {self.price}\t 컵사이즈 : {Drink._CUP_SIZES[self.cup_size]}\t얼음량 : {Drink._ICES[self.ice]}\t당도 : {Drink._SUGARS[self.sugar]}'

    def set_cup_size(self):
        cup_size = input("컵사이즈를 고르세요(0은 레귤러, 1은 점보) : ")
        if cup_size == '':
            self.cup_size =0
        else:
            self.cup_size = int(cup_size)

        if self.cup_size == 1:#점보라면 가격을 1200원 더 받아야 한다.
            self.price += 1200

    def set_ice(self):
        ice = input("얼음량을 고르세요(0은 0%, 1은 50%, 2는 기본, 3은 150%) : ")
        if ice =='':
            self.ice =2
        else:
            self.ice = int(ice)

    def set_sugar(self):
        sugar = input("당도를 고르세요(0은 0%, 1은 50%, 2는 기본, 3은 150%) : ")
        if sugar == '':
            self.sugar =2
        else:
            self.sugar = int(sugar)

if __name__ == '__main__':
    서빈이꺼 = Drink('화이트 초코', 3500)
    서빈이꺼.set_cup_size()
    서빈이꺼.set_ice()
    서빈이꺼.set_sugar()
    print(서빈이꺼)