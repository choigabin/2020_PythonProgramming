from drink import Drink

class Coffee(Drink):
    def order(self):
        self.set_cup_size()
        self.set_sugar()
        self.set_ice()

if __name__ == '__main__':
    예손이꺼 = Coffee('고구마 라떼', 322)
    예손이꺼.set_cup_size()
    예손이꺼.set_sugar()
    예손이꺼.set_ice()
    print(예손이꺼)