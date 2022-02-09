import pytest


def setup_module():
    print("setup_module")


def teardown_modeule():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test_login():
    print("登录")


class TestDemo():
    def setup_class(self):
        print("这是setup_class")

    def setup_method(self):
        print("setup_method")

    def set_up(self):
        print("set_up")

    def tear_down(self):
        print("tear_down")

    def teardown_class(self):
        print("teardown_class")

    def teardown_method(self):
        print("teardown_method")

    def test_one(self):
        print("开始执行 test_one 方法")
        x = "this"
        assert 'h' in x

    def test_two(self):
        print("开始执行 test_two 方法")
        x = "hello"
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three 方法")
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == '__main__':
    pytest.main()
