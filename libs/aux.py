# -*-coding:utf-8 -*-
# !/usr/bin/env python


def sort(array):
    # Algoritmo de quicksort, es recursivo.
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return array


def to_list(arg, l):
    lst = arg.split('/')
    long = (len(lst) == l)
    ret = []
    if long:
        ret = lst
    return ret


def is_to_list(string, l):
    lst = string.split('/')
    return len(lst) == l
