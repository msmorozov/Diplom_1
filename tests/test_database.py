import pytest
from praktikum.database import Database

class TestDatabase:

    @pytest.fixture
    def db(self, db):
        return db

    def test_available_buns(self, db, bun_fixture):
        db.buns = [bun_fixture]
        assert db.available_buns() == [bun_fixture]

    def test_available_ingredients(self, db, ingredient_data_param):
        db.ingredients = [ingredient_data_param]
        assert db.available_ingredients() == [ingredient_data_param]
