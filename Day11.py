#!/usr/bin/env python
# -*- coding:utf-8 -*-
# IO
import os, pickle, json

def main():
    try:
        f = open("Day1.py", 'r')
        print f.readlines()
    finally:
        if f:
            f.close()
    with open("Day2.py", 'r') as f:
        print f.read()
    print f.closed

    # StringIO/BytesIO

    # 操作文件和目录
    print '******************'
    print os.name
    print os.uname()
    print os.environ

    print '--------------------'
    print os.path.abspath(".")
    print os.path.split("/Users/aibb/Documents/etu/python/code/StudyPython/Day11.py")
    print os.path.splitext("/Users/aibb/Documents/etu/python/code/StudyPython/Day11.py")
    # os.rename('thumb.jpg', 'thumb.jpeg')

    print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

    # 序列化
    d = dict(name='Bob', age=20, score=88)
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)
    f.close()
    # 反序列化
    f = open('dump.txt', 'rb')
    d = pickle.load(f)
    f.close()
    print d

    print json.dumps(d)
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print json.loads(json_str)


if __name__ == '__main__':
    main()


