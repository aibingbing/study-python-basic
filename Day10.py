#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 错误，调试和测试
import logging,pdb

def main():
   try:
       print 'try...'
       r = 10 / 0
       print 'result:', r
   except ZeroDivisionError as e:
       print 'except:', e
       logging.info(e)
   finally:
       print 'finally...'
   print 'END'

   pdb.set_trace()
   foo('0')


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()


