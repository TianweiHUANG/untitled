#!/usr/bin/python
# -*- coding: utf-8 -*-

def _init():
    global _global_dict
    _global_dict = {}

def set_value(name, value):
    _global_dict[name] = value

#参数defValue作为函数get_value()出错时返回的值,如果不指定该参数
#则默认defValue=None,即函数get_value()出错时返回None。
def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue