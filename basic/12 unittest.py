import unittest

class demo(unittest.TestCase):
    def setUp(self) -> None:
        print('setup')

    def tearDown(self)-> None:
        print('tear down')

    def test_case1(self):
        print('test case')
        self.assertEqual(1, 1, '是否相等')
        self.ass


if __name__ == '__main__':
    unittest.main()