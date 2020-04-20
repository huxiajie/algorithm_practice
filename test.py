# encoding: utf-8
import gc
import sys
li = [1, 2, 3]
li2 = li

a="2"
def ppp(lii,b):
    # lii.append(4)
    print(id(a))
    print(id(b))
    b="2"
    print(id(a))
    print(id(b))
    print("qqqq")
    print(id(li))
    print(id(lii))
    return li


if __name__ == "__main__":
    gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
    a = []
    b = []
    a.append(b)
    b.append(a)
    print(a, b)
    print('a refcount:', sys.getrefcount(a))
    print('b refcount:', sys.getrefcount(b))
    del a
    # del b
    print(gc.collect())
    # print('a refcount:', sys.getrefcount(a))
    # print('b refcount:', sys.getrefcount(b))
