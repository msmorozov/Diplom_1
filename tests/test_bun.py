from praktikum.bun import Bun

class TestBun:

    def test_bun(self, bun_fixture):
        name, price = bun_fixture.get_name(), bun_fixture.get_price()
        assert bun_fixture.get_name() == name
        assert bun_fixture.get_price() == price