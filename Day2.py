#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 与字符编码有关的测试


def main():
    print ord("A")
    print chr(65)
    # unicode编码
    print unichr(25991)
    print ord(u'中')

    print 'ABC'.encode('ascii')
    print 'ABC'.encode('utf-8')
    # print '中国人'.encode('ascii')
    chinese = u'中国人'
    print chinese.encode('utf-8')
    print chinese.encode('utf-8')

    print b'ABCD'.decode('ascii')
    print 'length:%s' % len(chinese)
    print 'bytes:%s' % len(bytes('中国人'))


if __name__ == '__main__':
    main()