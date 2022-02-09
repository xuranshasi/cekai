import pytest
import yaml


class TestData:
    @pytest.mark.parametrize("a,b,c", yaml.safe_load(open("./data.yml")))
    def test_data(self, a, b, c):
        print(a + b + c)

