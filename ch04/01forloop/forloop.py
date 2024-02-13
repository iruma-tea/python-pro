# 1重のループ、1ステップ
names = ['小山', '中山', '大山', '高山']
for name in names:
    print(name)


# 1重のループ、複数ステップ
names = ['小山', '中山', '大山', '高山']
for index, name in enumerate(names):
    greeting = 'こんにちは、私の名前は'
    print(f'{index + 1}. {greeting}{name}です。')

names = ['小山', '中山', '大山', '高山']
for name in names:
    print(f'私は{name}です。')

message = '本日のゲスト： '
for name in names:
    message += f'{name}さん '
print(message)

# 入れ子になったforループ


def has_duplicates(sequence):
    for index1, item1 in enumerate(sequence):
        for index2, item2 in enumerate(sequence):
            if item1 == item2 and index1 != index2:
                return True
    return False


sequence = [0, 5, 10, 7, 19, 4]
print(has_duplicates(sequence))
sequence = [0, 5, 4, 10, 7, 19, 4]
print(has_duplicates(sequence))
