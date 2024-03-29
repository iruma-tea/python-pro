# 関数をクラスのメソッドにする
import random
OPTIONS = ['グー', 'チョキ', 'パー']


class JankenSimulator:
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None

    def get_computer_choice(self):
        return random.choice(OPTIONS)

    def get_human_choice(self):
        choice_number = int(input('「グー」か「チョキ」か「パー」を番号で選んでください: '))
        return OPTIONS[choice_number - 1]

    def print_options(self):
        print('\n'.join(f'({i}) {option.title()}' for i,
              option in enumerate(OPTIONS, 1)))

    def print_choices(self, human_choice, computer_choice):
        print(f'あなたが選んだのは「{human_choice}」です。')
        print(f'コンピュータが選んだのは「{computer_choice}」です。')

    def print_win_lose(self, human_choice, computer_choice, human_beats,
                       human_lose_to):
        if computer_choice == human_lose_to:
            print(f'残念でした。{computer_choice}の勝です。')
        elif computer_choice == human_beats:
            print(f'おめでとうございます！{human_choice}の勝です。')

    def print_result(self, human_choice, computer_choice):
        if human_choice == computer_choice:
            print('引き分けです。')

        if human_choice == 'グー':
            self.print_win_lose('グー', computer_choice, 'チョキ', 'パー')
        elif human_choice == 'パー':
            self.print_win_lose('パー', computer_choice, 'グー', 'チョキ')
        elif human_choice == 'チョキ':
            self.print_win_lose('チョキ', computer_choice, 'パー', 'グー')

    def simulate(self):
        self.print_options()
        human_choice = self.get_human_choice()
        computer_choice = self.get_computer_choice()
        self.print_choices(human_choice, computer_choice)
        self.print_result(human_choice, computer_choice)


jaken = JankenSimulator()
jaken.simulate()
