import json
import random

FOODS = [
    'ピザ',
    'ハンバーガー',
    'サラダ',
    'スープ'
]


def random_food(request):
    food = random.choice(FOODS)

    if request.headers.get('Accept') == 'Application/json':
        return json.dumps({'food': food})
    elif request.headers.get('Accept') == 'Application/xml':
        return f'<response><food>{food}</food></response>'
    else:
        return food
