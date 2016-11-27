import timeit

def test1():
    return my_print()

def test2():
    return my_print()

def test3():
    return my_print()

if __name__ == '__main__':


    print(timeit.timeit("test1()", setup="from __main__ import test1"))
    print(timeit.timeit("test2()", setup="from __main__ import test2"))
    print(timeit.timeit("test3()", setup="from __main__ import test3"))