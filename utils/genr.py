import contextlib


def gen1():
    print('start')
    yield
    print('stop')