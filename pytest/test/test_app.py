#!/usr/bin/python
# -*- coding: utf-8 -*-

def test_1():
    a = 2
    b = 2
    print('test_1', a, b)
    assert a == b

def test_2():
    a = 1
    b = 2
    assert a != b
