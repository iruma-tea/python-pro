# ミックスイン
class SpeakMixin:
    def speak(self):
        name = self.__class__.__name__.lower()
        print(f'一匹の{name}が「こんにちは！」と言った。')


class RollOverMixin:
    def roll_over(self):
        print('横回転した！')


class Dog(SpeakMixin, RollOverMixin):
    pass  # なにもしない


dog = Dog()
dog.speak()
dog.roll_over()
