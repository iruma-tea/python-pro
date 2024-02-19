class Bird:
    def fly(self):
        print('飛行中!')


class Hummingbird(Bird):
    def fly(self):
        print('高速に羽ばたき中！')


class Penguin(Bird):
    def fly(self):
        print('飛べません！')


a = Bird()
a.fly()
b = Hummingbird()
b.fly()
c = Penguin()
c.fly()
