# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 给Python初学者超快的Py脚本解说
import os as ostest
import sys


def main():
    print '************************'
    print 'Hello,World!'

    print "这是Alice\'的问候."
    print '这是Bob\'的问候。'

    foo(5, 10)

    print '='*10
    print '这将是直接执行'+ostest.getcwd()
    print '系统当前登录人是：'+ostest.getlogin()

    second_func()
    print '************************'

'''这个
是多行注释'''


def second_func():
    counter = 0
    counter += 1
    print '{} + 1 = {}'.format(counter,counter+1)

    food_array = ['苹果', '香蕉', '火龙果', '菠萝']
    print food_array
    for i in food_array:
        print '历次遍历：'+ i

    print '数到10'
    for i in range(1, 10, 1):
        print i


def test_execute_order():
    print '\n'
    print '******定义在方法外面的函数，必须在前面定义，后面才能调用，调用顺序取决于代码先后'


def foo(param1,param2):
    res = param1+param2
    print '{} 加 {} 等于{}'.format(param1, param2, res)
    print '%s 加 %s 等于%s'%(param1, param2, res)

    if res < 50:
        print '这个'
    elif (res>=50) and ((param1==42) or (param2==24)):
        print '那个'
    else:
        print '恩。。。'
    return res  # 这个是单行注释


def input_name():
    name = raw_input('please input your name first:')
    print '输入的内容是：{}'.format(name)

print "使用的Python版本是："+sys.version
if __name__ == '__main__':
    input_name()
    main()

test_execute_order()
