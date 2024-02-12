from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')


def day():
    return datetime.now().strftime('%A')


def part_of_day():
    current_hour = datetime.now().hour
    if current_hour < 12:
        part_of_day = '午前'
    elif 12 <= current_hour < 17:
        part_of_day = '午後'
    else:
        part_of_day = '夜'
    return part_of_day


class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self, store):
        print(f'{store}へようこそ！私、{self.name}と申します。')
        print(f'{day()}の{part_of_day()}、いかがお過ごしですか？')
        print('本日のお客様に20% クーポンを差し上げます！')


if __name__ == '__main__':
    greeter = Greeter("竈門")
    greeter.greet("Pythonプロショップ")
