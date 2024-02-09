# @@range_begin(list1)
TAX_RATES_BY_STATE = {
    'MI': 1.06,
    # @@range_end(list1)
    'AK': 1.00,
    'AL': 1.04,
    'AR': 1.065,
    'AZ': 1.056,
    'WY': 1.04
    # @@range_begin(list2)  # ←この行は無視してください。書籍の本文に引用するためのものです。
}


def add_sales_tax(total, state):
    return total * TAX_RATES_BY_STATE[state]

# @@range_end(list2)  # ←この行は無視してください。書籍の本文に引用するためのものです。


def test():
    total = 1000
    grand_total = add_sales_tax(total, 'MI')
    print(f'合計金額={grand_total}')


if __name__ == '__main__':
    test()
