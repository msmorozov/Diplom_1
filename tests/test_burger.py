from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self, burger, bun_fixture):
        burger.set_buns(bun_fixture)
        assert burger.bun.get_name() == bun_fixture.get_name()

    def test_add_ingredients(self, burger, mock_ingredient1):
        burger.add_ingredient(mock_ingredient1)
        assert burger.ingredients[0] == mock_ingredient1

    def test_remove_ingredient(self, burger, mock_ingredient1, mock_ingredient2):
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(1)
        assert burger.ingredients == [mock_ingredient1]

    def test_move_ingredient(self, burger, mock_ingredient1, mock_ingredient2):
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]

    def test_get_price(self, burger, bun_mock, ingredient_mock):
        burger.bun = bun_mock
        burger.ingredients = [ingredient_mock]
        expected_price = bun_mock.get_price()*2 + ingredient_mock.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, mock_bun, mock_ingredient1, mock_ingredient2):
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        burger.get_price = Mock(return_value=300)
        expected_receipt = f"(==== {mock_bun.get_name()} ====)\n= {mock_ingredient1.get_type()} {mock_ingredient1.get_name()} =\n= {mock_ingredient2.get_type()} {mock_ingredient2.get_name()} =\n(==== {mock_bun.get_name()} ====)\n\nPrice: 300"

        assert burger.get_receipt() == expected_receipt
