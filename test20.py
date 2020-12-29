print('Hello world123')
a = 5


def asd():
    global a
    a = a + 1
    print(a)


for i in range(10):
    asd()


