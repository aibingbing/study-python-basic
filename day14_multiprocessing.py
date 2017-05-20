#! /usr/local/env/bin python
# -*- coding=utf-8 -*-


from multiprocessing import Process
import os


def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())


if __name__ == '__main__':
    print  'parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    p1 = Process(target=run_proc, args=('test',))
    print 'Child process will start.'
    p.start()
    p1.start()
    print 'p process is alive? %s' % p.is_alive()
    p.join()
    p1.join()
    print 'Child process end.'
    print 'p process is alive? %s' % p.is_alive()
