# 1

def func(llll):
    llll.insert(0, "Element")
    llll.insert(1, "start")
    llll.append("finish")
    return llll

print(func(['hello', 5, 'John', ]))

# 2

def func_1(*args):
    arg1, arg2, arg3 = args
    a = {}
    a[arg1] = 1
    a[arg2] = 2
    a[arg3] = 3
    return a

print(func_1('x', 5, 'John'))

# 3

def func_3(a):
    x = list(a)
    y = []
    z = []

    for element in x:
        c = element % 2 == 0
        if c:
            y.append(element)
    for lesr in x:
        d = lesr ** 2
        z.append(d)

    print(y)
    print(z)

func_3((1,2,3,4,5))


