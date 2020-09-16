import pytest

@pytest.mark.fail(raises=IndexError)   
class TestHello():
    def test_hello(self):
         assert 4 == 4
