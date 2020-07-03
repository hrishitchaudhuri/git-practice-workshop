import time

def test(x, y):
    if(y==0):
        return y
    return test(y, y%x)

for i in range(0, 10):
    print('GCD of {} with 2 : '.format(i), test(2, 10))

