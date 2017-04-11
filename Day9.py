#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 面向对象编程
from types import MethodType


class Student(object):
    name = 'Student'

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print '%s: %s ' %(self.__name, self.__score)


class Animal(object):
    def run(self):
        print('Animal is running....')


class Dog(Animal):
    def run(self):
        print 'Dog is running...'

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def set_age(self, age):
    self.age = age


def main():
   bass = Student
   print bass
   # bass_object = Student()
   # print bass_object
   # bass_object.name = 'abb'
   # print bass_object.name

   xiaoming = Student('xiaoming', 20)
   print xiaoming.print_score()
   print xiaoming
   print xiaoming.get_score()
   print xiaoming._Student__name
   # print xiaoming.__name

   dog = Dog()
   dog.run()

   cat = Cat()
   cat.run()

   print type(dog)
   print type(cat)
   print isinstance(dog, list)
   print isinstance(dog, Animal)
   print isinstance(dog, Dog)

   print dir(dog)

   print dir(str)
   print Student.name
   s = Student('ddd', 222)
   print s.name
   Student.age = 100
   print Student.age

   s.set_age = MethodType(set_age, s)
   s.set_age(25)
   s.age

   # for n in Fib():
   #     print n
   print callable(s)
   print callable([1, 2, 3])
   print callable(hello)

   Hello = type('Hello',(object,),dict(hello=hello))
   h = Hello()
   h.hello()
   print type(Hello)
   print type(h)


def hello(self, name='world'):
    print('Hello, %s.' % name)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a


if __name__ == '__main__':
    main()


