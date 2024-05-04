import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from praktikum.database import Database

# Фикстуры для объекта Burger
@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun_mock():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_price.return_value = 250.0
    return bun_mock

@pytest.fixture
def ingredient_mock():
    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_price.return_value = 200.0
    return ingredient_mock

# Фикстуры для объекта Bun
@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Булочка'
    return mock_bun

@pytest.fixture
def mock_ingredient1():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "Соус"
    mock_ingredient.get_type.return_value = "ингридиент"
    return mock_ingredient

@pytest.fixture
def mock_ingredient2():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "Котлетька"
    mock_ingredient.get_type.return_value = "мясо"
    return mock_ingredient

# Фикстуры для объекта Bun с параметризацией
@pytest.fixture(params=[
    ("Обычная булка", 1000.0),
    ("Булочка с кунжутом", 500.0),
    ("Бриошь", 1500.0)
])
def bun_fixture(request):
    name, price = request.param
    return Bun(name, price)

# Фикстуры для объекта Database
@pytest.fixture
def db():
    return Database()

# Фикстуры для базы данных с параметризацией
@pytest.fixture(params=[
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
])
def bun_data(request):
    return request.param

# Фикстуры для ингредиентов с параметризацией
@pytest.fixture(params=[
    ("sauce", "hot sauce", 100),
    ("sauce", "sour cream", 200),
    ("sauce", "chili sauce", 300),
    ("filling", "cutlet", 100),
    ("filling", "dinosaur", 200),
    ("filling", "sausage", 300)
])
def ingredient_data(request):
    return request.param

# Параметризованные фикстуры для объекта Ingredient
@pytest.fixture(params=[
    ("Котлетька", "мясо", 100),
    ("Соус", "ингредиент", 200),
    ("Лист салата", "овощ", 50)
])
def ingredient_data(request):
    return request.param