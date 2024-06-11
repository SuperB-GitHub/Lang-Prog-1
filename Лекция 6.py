import numpy as np

def e():
    a=int(input('Введите число:' ))
    b=np.eye(a)
    b=b.astype(int)
    c=np.tril(([2]*a),-1)
    c=np.fliplr(c)
    b=np.fliplr(b)
    print(c+b)
e()

# def f():