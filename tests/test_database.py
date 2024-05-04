from unittest.mock import Mock
import pytest
from praktikum.database import Database

class TestDatabase:

    def test_available_buns(self, db, bun_data):
        bun_name, bun_price = bun_data
        bun_mock = Mock()
        bun_mock.get_name.return_value = bun_name
        bun_mock.get_price.return_value = bun_price

        db.buns = [bun_mock]

        assert db.available_buns() == [bun_mock]

    def test_available_ingredients(self, db, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient_mock = Mock()
        ingredient_mock.get_type.return_value = ingredient_type
        ingredient_mock.get_name.return_value = ingredient_name
        ingredient_mock.get_price.return_value = ingredient_price

        db.ingredients = [ingredient_mock]

        assert db.available_ingredients() == [ingredient_mock]
