class Tire:
    def __repr__(self):
        return 'ゴムのタイヤ'


class FancyTire:
    def __repr__(self):
        return '素敵なタイヤ'


class Frame:
    def __repr__(self):
        return 'アルミのフレーム'


class CarbonFiberFrame:
    def __repr__(self):
        return 'カーボンファイバーのフレーム'


class Bicycle:
    def __init__(self, front_tire, back_tire, frame):
        self.front_tire = front_tire
        self.back_tire = back_tire
        self.frame = frame

    def print_specs(self):
        print(f'フレーム: {self.frame}')
        print(f'前のタイヤ: {self.front_tire}。後ろのタイヤ: {self.back_tire}')


if __name__ == '__main__':
    bike = Bicycle(Tire(), Tire(), Frame())
    bike.print_specs()

    print("------------------")

    bike = Bicycle(Tire(), Tire(), CarbonFiberFrame())
    bike.print_specs()

    print(isinstance(FancyTire(), Tire))
    print(issubclass(int, int))
    print(issubclass(FancyTire, Tire))
    print(issubclass(dict, float))
