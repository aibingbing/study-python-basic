#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PIL import Image

' a test module '  # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'ABB'


# 模块：在Python中，一个.py文件就称之为一个模块（Module

# 最大的好处是大大提高了代码的可维护性。
# 使用模块还可以避免函数名和变量名冲突。
# 相同名字的函数和变量完全可以分别存在不同的模块中，
# 因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。
# 但是也要注意，尽量不要与内置函数名字冲突。
# 点这里查看Python的所有内置函数。

# Python又引入了按目录来组织模块的方法，称为包（Package）。
# 每一个包目录下面都会有一个__init__.py的文件，
# 这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，
# 因为__init__.py本身就是一个模块


def main():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

    print sys.path

    im = Image.open('python-file-detail.png')
    print(im.format, im.size, im.mode)
    im.thumbnail((200, 100))
    im.save('thumb.jpg', 'JPEG')


# 当我们在命令行运行hello模块文件时
# ，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
# 最常见的就是运行测试。
if __name__ == '__main__':
    main()

# 作用域
# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。


def _private_1(name):
    return 'Hello, %s' % name


# 如果我们要添加自己的搜索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录：
#
