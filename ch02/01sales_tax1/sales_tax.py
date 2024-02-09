# @@range_begin(list1)
def add_sales_tax(total, tax_rate):  # 売上税を追加
    return total * tax_rate  # 日本の消費税とは違い、最終消費者のみに課せられる
# @@range_end(list1)


def test():
    total = 1000
    rate = 1.1
    grand_total = add_sales_tax(total, rate)
    print(f'合計金額={grand_total}')


if __name__ == '__main__':
    test()
