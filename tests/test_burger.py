from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun


class TestBurger:

    def test_set_buns(self, burger):
        bun = Bun('Бриошь', 100.0)
        burger.set_buns(bun)
        assert burger.bun.get_name() == 'Бриошь'

    def test_add_ingredients(self, burger):
        ingredient = Ingredient('секретный', 'ингридиент', 100.0)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, burger):
        ingredient_1 = Ingredient('ингридиент', 'соус', 100.0)
        ingredient_2 = Ingredient('ингридиент', 'начинка', 200.0)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(1)
        assert burger.ingredients == [ingredient_1]

    def test_move_ingredient(self, burger):
        ingredient_1 = Ingredient('ингридиент', 'соус', 100.0)
        ingredient_2 = Ingredient('ингридиент', 'начинка', 200.0)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_price(self, burger, bun_mock, ingredient_mock):
        burger.bun = bun_mock
        burger.ingredients = [ingredient_mock]
        assert burger.get_price() == 700.0

    def test_get_receipt(self, burger, mock_bun, mock_ingredient1, mock_ingredient2):
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        burger.get_price = Mock(return_value=300)
        expected_receipt = f"(==== {mock_bun.get_name()} ====)\n= {mock_ingredient1.get_type()} {mock_ingredient1.get_name()} =\n= {mock_ingredient2.get_type()} {mock_ingredient2.get_name()} =\n(==== {mock_bun.get_name()} ====)\n\nPrice: 300"

        assert burger.get_receipt() == expected_receipt
