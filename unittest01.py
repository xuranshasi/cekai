# 单测unittest
import unittest


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("set up")

    def tearDown(self) -> None:
        print("tearDown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(1, 1, "判断相等")
        self.assertIn("hello", "helloworld")

    def test_case02(self):
        print("testcase02")
        self.assertEqual(2, 2, "判断相等")
        self.assertIn("hello", "helloworld")

    @unittest.skipIf(1 == 1, "跳过这条用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(3, 3, "判断相等")
        self.assertIn("hello", "helloworld")


class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test_demo1_case0")

    def test_demo1_case1(self):
        print("test_demo1_case1")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(demo("test_case01"))
    suite.addTest(demo1("test_demo1_case0"))
    unittest.TextTestRunner().run(suite)