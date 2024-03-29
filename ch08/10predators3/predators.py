from abc import ABC, abstractmethod


class Predator(ABC):
    @abstractmethod
    def eat(self, prey):
        pass


class Bear(Predator):  # <5>
    def eat(self, prey):  # <6>
        print(f'熊が{prey}を一撃！')

    def roar(self):
        print('熊が吠えた！')


class Owl(Predator):
    def eat(self, prey):
        print(f'フクロウが{prey}めがけて急降下！')


class Chameleon(Predator):
    def eat(self, prey):
        print(f'カメレオンが舌を伸ばして{prey}をペロリ！')


if __name__ == '__main__':
    bear = Bear()
    bear.eat('シカ')
    owl = Owl()
    owl.eat('ネズミ')
    chameleon = Chameleon()
    chameleon.eat('ハエ')

    bear.roar()
