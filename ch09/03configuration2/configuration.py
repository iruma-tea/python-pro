import json
import random

FOODS = [
    'ピザ',
    'ハンバーガー',
    'サラダ',
    'スープ',
]


def random_food(request):
    food = random.choice(FOODS)

    if request.headers.get('Accept') == 'application/json':
        return json.dumps({'food': food})
    else:
        return food
