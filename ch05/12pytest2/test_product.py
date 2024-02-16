from product import Product


class TestProduct:

    def test_transform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        assert small_black_shoes.transform_name_for_sku() == 'SHOES'

        medium_pink_tank_top = Product('tank top', 'M', 'pink')
        assert medium_pink_tank_top.transform_name_for_sku() == 'TANKTOP'
