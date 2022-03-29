"""
@Project ：tri-func
@File ：FunctionTest.py
@Author ：Linshuaijiang
@Date ：2022/3/29 16:25
"""

import unittest
from function_angle.arcsin import asin
from function_angle.arctan import atan
from function_angle.cos import cos
from function_angle.sin import sin


class TestFunc(unittest.TestCase):         # 测试类

    def test_arcsin(self):                 # 测试arcsin函数
        self.assertEqual(0, asin(0))
        self.assertEqual(30, asin(0.5))
        self.assertEqual(45, asin(0.7071))
        self.assertEqual(60, asin(0.8660))
        self.assertEqual(90, asin(1))
        self.assertEqual(-30, asin(-0.5))
        self.assertEqual(-45, asin(-0.7071))
        self.assertEqual(-90, asin(-1))
        self.assertEqual(-60, asin(-0.8660))

    def test_arctan(self):                 # 测试arctan函数
        self.assertEqual(0, atan(0))
        self.assertEqual(30, atan(0.5773))
        self.assertEqual(45, atan(1))
        self.assertEqual(60, atan(1.732))
        self.assertEqual(0, atan(0))
        self.assertEqual(-30, atan(-0.5773))
        self.assertEqual(-45, atan(-1))
        self.assertEqual(-60, atan(-1.732))

    def test_cos(self):                    # 测试cos函数
        self.assertEqual(1, cos(0))
        self.assertEqual(0.866, cos(30))
        self.assertEqual(0.5, cos(60))
        self.assertEqual(0, cos(90))
        self.assertEqual(-0.5, cos(120))
        self.assertEqual(-1, cos(180))
        self.assertEqual(0, cos(270))
        self.assertEqual(1, cos(360))
        self.assertEqual(0.866, cos(-30))
        self.assertEqual(0.5, cos(-60))
        self.assertEqual(0, cos(-90))
        self.assertEqual(-0.5, cos(-120))
        self.assertEqual(-1, cos(-180))
        self.assertEqual(0, cos(-270))
        self.assertEqual(1, cos(-360))

    def test_sin(self):                    # 测试sin函数
        self.assertEqual(0, sin(0))
        self.assertEqual(0.5, sin(30))
        self.assertEqual(0.866, sin(60))
        self.assertEqual(1, sin(90))
        self.assertEqual(0.866, sin(120))
        self.assertEqual(0, sin(180))
        self.assertEqual(-1, sin(270))
        self.assertEqual(0, sin(360))
        self.assertEqual(-0.5, sin(-30))
        self.assertEqual(-0.866, sin(-60))
        self.assertEqual(-1, sin(-90))
        self.assertEqual(-0.866, sin(-120))
        self.assertEqual(0, sin(-180))
        self.assertEqual(1, sin(-270))
        self.assertEqual(0, sin(-360))


if __name__ == '__main__':
    unittest.main()


