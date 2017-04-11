#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 函数式编程
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
import functools


def main():
    # 高阶函数
    print add(3, -5, 4, abs)
    # map
    r = map(f, list(range(11)))
    print r
    print list(map(str, list(range(10))))
    # reduce
    print reduce(fn, [1, 3, 5, 7, 9])
    # print reduce(add, [1, 3, 5, 7, 9, 11])
    print reduce(fn, map(char2num, '13579'))
    print '134567'
    # filter
    print list(filter(not_empty, ['A', '', None, 'C', 'D']))

    # 打印1000以内所有素数(死循环)
    '''for n in primes():
        if n < 1000:
            print n
        else:
            break
            '''
    # 排序
    sort_list = [36, 5, -12, -900, 567]
    print sorted(sort_list)
    print sort_list
    print sorted(sort_list, key=abs)
    # 字符串排序
    sort_list_str = ['bob', 'about', 'Zoo', 'Credit']
    print sorted(sort_list_str, key=str.lower)
    print sorted(sort_list_str, key=str.lower, reverse=True)

    # 函数作为返回值
    my_sum = lazy_sum(1, 3, 5, 7, 9)
    print my_sum
    print my_sum()

    # 闭包
    # 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
    print count()
    for func in count():
        print func()  # 函数返回值加上（）就是执行这个函数

    # lambda
    print list(map(lambda x: x * x, list(range(1, 11))))
    la = lambda x: x * x
    print la

    # 装饰器:在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
    print count.__name__
    ff = now  # 变成了wrapper
    print ff.__name__

    print now.__name__
    now()
    print now.__name__

    # 偏函数
    int2 = functools.partial(int, base=2)
    print int2('10000')
    return


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print ('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s:' % func.__name__)
#         return func(*args,**kw)
#     return wrapper


@log('execute')
def now():
    print('2017-04-09')


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def is_odd(n):
    return n % 2 == 0


def not_empty(s):
    return s and s.strip()


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def fn(x, y):
    return x * 10 + y


def f(x):
    return x * x


def add(x, y, z, func=abs):
    return func(x) + func(y) + func(z)


if __name__ == '__main__':
    main()