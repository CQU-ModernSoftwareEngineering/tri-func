# -*- coding: utf-8 -*-
"""
@Project ：tri-func
@File ：CalculatorMainWindow.py
@Author ：JRJ
@Date ：2022/3/31 17:00
界面交互代码，调用计算函数接口，
和界面按键监听接口，实现计算机界面交互设计
"""

import sys
from CalculatorUi.CalculatorUi import UiMainWindow
from function_angle.sin import sin
from function_angle.cos import cos
from function_angle.arcsin import asin
from function_angle.arctan import atan
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.is_compute = False  # 标志位，是否进行了运算
        self.is_error = False  # 标志位，运算是否出错，出错了运算按钮将锁死
        self.is_rad = True  # 标志位 ，表示是否计算的是弧度
        # 按键监听
        self.ui.number_0_button.clicked.connect(lambda: self.display_number(0))
        self.ui.number_1_button.clicked.connect(lambda: self.display_number(1))
        self.ui.number_2_button.clicked.connect(lambda: self.display_number(2))
        self.ui.number_3_button.clicked.connect(lambda: self.display_number(3))
        self.ui.number_4_button.clicked.connect(lambda: self.display_number(4))
        self.ui.number_5_button.clicked.connect(lambda: self.display_number(5))
        self.ui.number_6_button.clicked.connect(lambda: self.display_number(6))
        self.ui.number_7_button.clicked.connect(lambda: self.display_number(7))
        self.ui.number_8_button.clicked.connect(lambda: self.display_number(8))
        self.ui.number_9_button.clicked.connect(lambda: self.display_number(9))
        self.ui.del_button.clicked.connect(self.display_delete_one_number)
        self.ui.reset_button.clicked.connect(self.display_reset)
        self.ui.dot_button.clicked.connect(self.display_dot)
        self.ui.sign_button.clicked.connect(self.change_sign)
        self.ui.radian_button.clicked.connect(self.change_rad)
        self.ui.sin_button.clicked.connect(lambda: self.compute(0))
        self.ui.cos_button.clicked.connect(lambda: self.compute(1))
        self.ui.arctan_button.clicked.connect(lambda: self.compute(2))
        self.ui.arcsin_button.clicked.connect(lambda: self.compute(3))

    def str_to_number(self):
        """
        将显示框的文本转为对应的数值，判断字符串是否为空，
        对字符串中是否包含“°”进行判读，并改变self.is_rad状态
        :return: number，字符串对应的值或者None
        """
        number_str = self.ui.display_box.text()
        if len(number_str) < 1:
            self.is_error = True
            return None
        if "°" in number_str:
            self.is_rad = False
            number_str = number_str[:-1]  # 去掉度数单位，截取数字文本 并且转换为弧度
        if self.is_error:
            return None
        return eval(number_str)

    def display_to_box(self, content):
        """
        在显示框上显示内容
        :param content: str，要的显示内容；
        :return: None
        """
        self.ui.display_box.setText(content)

    def compute(self, compute_type):
        """
        根据不同的按钮功能，对用户输入进行计算，将计算结果显示到显示框上；
        :param compute_type: int，计算类型的标识；
        :return: None；
        """

        input_value = self.str_to_number()  # 获取用户输入

        if self.is_error or input_value is None:
            return None
        if compute_type == 0:
            result = sin(input_value, self.is_rad)  # 计算sin
        elif compute_type == 1:
            result = cos(input_value, self.is_rad)  # 计算cos
        elif compute_type == 2 and self.is_rad:
            # 这里使用self.is_rad进行判读，是为了防止输入值是度数
            result = str(atan(input_value)) + "°"  # 计算arctan
        elif compute_type == 3 and self.is_rad:

            result = asin(input_value)  # 计算arcsin
            if isinstance(result, bool):
                # 返回一个bool值说明输入有误，显示提示信息
                result = "无效输入"
                self.is_error = True
            else:
                result = str(result) + "°"
        else:
            result = "无效输入"
            self.is_error = True  # 出错 锁死
        self.display_to_box(str(result))  # 显示结果
        self.is_rad = True
        self.is_compute = True

    def display_number(self, number):
        """
        在显示框上显示按钮对应的值
        :param number: 按钮对应的值
        :return: None
        """
        display_content = self.ui.display_box.text()  # 获取显示框的文本
        if display_content == "0" or self.is_compute:
            display_content = str(number)  # 当前内容为0，直接更新为的按钮数字
        else:
            display_content += str(number)  # 当前内容不为0，追加数字
        self.display_to_box(display_content)  # 回显内容
        self.is_compute = False
        self.is_error = False

    def display_dot(self):
        """
        在显示框上显示一个小数点.
        :return: None
        """
        display_content = self.ui.display_box.text()  # 获取显示框的文本
        if "." in display_content or self.is_compute:
            return
        else:
            display_content += "."  # 追加一个小数点
            self.display_to_box(display_content)  # 回显内容

    def display_delete_one_number(self):
        """
        清除当前显示框上数值最右侧的一位数；
        当显示框上的数值只有一位时，再次按清除按钮显示0；
        :return: None;
        """
        display_content = self.ui.display_box.text()  # 获取显示框文本
        if self.is_compute:
            return
        if len(display_content) == 1:
            display_content = "0"  # 当显示框上的数值只有一位时，再次按清除按钮显示0；
        else:
            display_content = display_content[:-1]  # 清除当前显示框上数值最右侧的一位数
        self.display_to_box(display_content)  # 回显内容

    def display_reset(self):
        """
        重置显示框上的内容为0
        :return:None
        """
        self.is_compute = False
        self.is_error = False
        self.display_to_box("0")

    def change_sign(self):
        """
        改变显示框上文本的正负号
        :return:
        """
        display_content = self.ui.display_box.text()  # 获取显示框的文本
        if display_content == "0":  # 文本内容为0，不作符号处理
            return
        elif "-" in display_content:
            display_content = display_content[1:]
        else:
            display_content = "-" + display_content
        self.display_to_box(display_content)

    def change_rad(self):
        """
        改变显示框中数值的弧度或者角度
        return:
        """
        if self.is_rad:
            self.is_rad = False
            return self.ui.display_box.setText(self.ui.display_box.text() + '°')
        else:
            self.is_rad = True
            return self.ui.display_box.setText(self.ui.display_box.text()[:-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
