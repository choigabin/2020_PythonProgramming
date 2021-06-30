from drink import Drink

class Bubbletea(Drink):
    _PEARLS = ['타피오카', '코코', '젤리', '알로에']
    
    def __init__(self, name, price):
        super().__init__(name, price)
        self.pearl =0

    def order(self):
        self.set_cup_size()
        self.set_sugar()
        self.set_ice()
        self.set_pearl()

    def set_pearl(self):
        pearl = input('펄을 고르세요  0: 타피오카, 1: 코코, 2: 젤리, 3: 알로에 ->')
        if pearl == '':
            self.pearl =0
        else:
            self.pearl = int(pearl)

    def __str(self):
        return super().__str__()+f'\t펄 : {Bubbletea._PEARLS[self.pearl]}'
    
if __name__ == '__main__':
    예서꺼 =Bubbletea('타로버블티', 3200)
    예서꺼.set_pearl()
    예서꺼.set_sugar()
    예서꺼.set_ice()
    예서꺼.set_cup_size()
    print(예서꺼)