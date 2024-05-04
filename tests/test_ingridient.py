from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_name(self, ingredient_data):
        name, ingredient_type, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    def test_get_price(self, ingredient_data):
        name, ingredient_type, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    def test_get_type(self, ingredient_data):
        name, ingredient_type, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

