from memory_profiler import profile
import copy
from pympler import asizeof
from random import randint
import sys

# class A:
#         def __init__(self):
#             self.temp = [[randint(1, 10), randint(1, 10), randint(1, 10)] * i for i in range(100)]


@profile(precision=4)
def main():
    class A:
        def __init__(self):
            self.temp = [[randint(1, 10), randint(1, 10), randint(1, 10)] * i for i in range(100)]
    cls_a = A().temp
    print(asizeof.asizeof(cls_a))
    cls_b = copy.deepcopy(cls_a)
    b = [[randint(1, 10), randint(1, 10)] * i for i in range(100)] 
    print(asizeof.asizeof(b))
    # cls_b = copy.deepcopy(cls_a)
    k = copy.deepcopy(asizeof.asizeof(b))

def mem_size(l: list):
    return (sys.getsizeof(l) - 56) // 8

def test():
    x = []
    y = []
    for i in range(100):
        print(f'{len(x)=}, {mem_size(x)=}, {x=}')
        print(f'{len(y)=}, {mem_size(y)=}, {y=}')
        x.append(i)
        y += [i]
 


test()
# main()