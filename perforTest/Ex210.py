import time


def execution_time_test(fun):
    def warp(*args, **kwargs):
        ts = time.time()
        res = fun(*args, **kwargs)
        te = time.time()

        print(fun.__name__, te - ts)
        return res

    return warp

l1 = [*range(0,10)]
lremove = [3,5,9]

@execution_time_test
def func1(l1,lremove):

    for i in range(100000):
        l12 = l1[:]
        lremove2 = lremove[:]
        for x in lremove2:
            if x in l12 : l12.remove(x)

@execution_time_test
def func2(l1,lremove):
    l2 = list()
    for i in range(100000):
        l2 = [ e for e in l1 if e not in lremove ]

@execution_time_test
def func3(l1,lremove):
    for i in range(100000):
        l3 = (e for e in l1 if e not in lremove)


func1(l1,lremove)
func2(l1,lremove)
func3(l1,lremove)