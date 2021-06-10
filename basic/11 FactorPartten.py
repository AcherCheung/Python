from abc import ABCMeta, abstractmethod


class Coke(metaclass=ABCMeta):
    @abstractmethod
    def drink(self):
        pass


class Coca(Coke):
    def drink(self):
        print('drink Coca-Cola')


class Pepsi(Coke):
    def drink(self):
        print('drink Pepsi-Cola')


class FastFoodRestaurant():
    def make_coke(self, name):
        return eval(name)()


KCD = FastFoodRestaurant()
coke = KCD.make_coke('Coca')
coke.drink()
