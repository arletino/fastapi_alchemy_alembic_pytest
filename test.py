from typing import TypeVar
T = TypeVar('tuple')

t = tuple

def test(t: type[tuple]) -> None:
    if t is tuple:
        print('tuple')
    else:
        print('not tuple')

test(t)
print(type(type))