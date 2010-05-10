#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

def fib(n):
    """Calcula a série de Fibonacci"""
    # define os valores para a=0 e b=1
    a, b = 0,1

    # calcula a série até o valor dado em n
    while a < n:
        print(a),
        a, b = b, a+b
    
