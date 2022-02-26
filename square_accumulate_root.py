#!/bin/python3

import math
import os
import random
import re
import sys

def consumer():
    while True:
        x = yield
        print(x)

def producer(n):
    for _ in range(n):
        x = int(input())
        yield x
#Just find some hints on the top ###using yield

# Complete the 'rooter', 'squarer', and 'accumulator' function below.

def rooter():
    x = 0
    while True:
        x = yield math.floor(math.sqrt(x)) # math.sqrt(x) will output 0.000000000 so must have to add floor

def squarer():
    x = 0
    while True:
        x = yield x**2

def accumulator():
    total = 0
    x = 0
    while True:
        total += x
        yield total


def pipeline(prod, workers, cons):
    for num in prod:
        for i, w in enumerate(workers):
            num = w.send(num)
            next(w)
        cons.send(num)
    for worker in workers:
        worker.close()
    cons.close()


if __name__ == '__main__':
    order = input().strip()
    
    n = int(input())

    prod = producer(n)

    cons = consumer()
    next(cons)
    
    root = rooter()
    next(root)

    accumulate = accumulator()
    next(accumulate)

    square = squarer()
    next(square)

    pipeline(prod, eval(order), cons)
