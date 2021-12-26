import time


def execution_time_test(fun):
    def warp(*args, **kwargs):
        ts = time.time()
        res = fun(*args, **kwargs)
        te = time.time()

        print(fun.__name__, te - ts)
        return res

    return warp


@execution_time_test
def func1():
    for i in range(100000):
        l1 = [[[1]]]*10
    return l1

@execution_time_test
def func2():
    for i in range(100000):
        l1 = [[[1]] for _ in range(10)]
    return l1

print(func1())
print(func2())
