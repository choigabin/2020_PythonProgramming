from coffee import Coffee
from bubbletea import Bubbletea

class Order:
    def __init__(self):
        self.menu = []
        self.order_menu = []
        self.set_menu()

    def set_menu(self):
        self.menu = [Coffee("연유라떼", 3800), Bubbletea('흑당버블티' ,4200)]

    def add_order_menu(self):
         while True:
            number =1
            print('⬜⬛'*13+'메뉴'+'⬜⬛'*13)
            for drink in self.menu:
                print(str(number)+'. ', drink)
                number +=1
                #메뉴 선택
            menu = input('메뉴를 고르세요->')
            if menu == '':
                break
            if menu =='1':
               new_drink = Coffee('연유라떼', 3800)
            elif menu == '2':
                new_drink = Bubbletea('흑당 버블티', 4200)
            #옵션 선택하자
            new_drink.order()
            print(new_drink)
            self.order_menu.append(new_drink)

    def sum_price(self):
        total = 0
        for drink in self.order_menu:
            total+=drink.price
        return total

    def __str__(self):
        s = '-' * 20 + '주문 내역' + '_'*20+'\n'
        for drink in self.order_menu:
            s = str(drink) + '\n'
        s +=f'총 금액은 {self.sum_price()}원 입니다.'
        return s

if __name__ =='__main__':
   order = Order()
   order.add_order_menu()
   # order.order_menu = [Bubbletea('데스트 버블티', 3000), Coffee('테스트 커피', 10000)]
   print(order)