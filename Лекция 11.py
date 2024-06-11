import numpy as np
def z1():
    arr = np.array([[3], [-1]])
    print(arr*2)

def z2():
    arr1 = np.array([[1,-2, 4], [2, 0, -1]])
    arr2 = np.array([[5, 2, 3], [4, 6, 2]])
    print(arr1+ arr2)

def z3():
    arr1=np.array([[1,2],[2,-1],[3,0]])
    arr2=np.array([[-1,1],[1,2],[0,0]])
    print(arr1-arr2*3)

def z4():
    arr1=np.array([[1,-1],[2,0],[3,0]])
    arr2=np.array([[1,1],[2,0]])
    print(arr1@arr2)
    print(arr1,'\n',arr2)

def z5():
    arr=np.array([[1,0],[-2,3]])
    print(arr)
    b=arr.transpose()
    print(b)

# def z6():


while True:
    i=int(input('Число: '))
    if i == 1:
        z1()
    if i == 2:
        z2()
    if i == 3:
        z3()
    if i == 4:
        z4()
    if i == 5:
        z5()
    if i == 6:
        z6()
    if i<1 or i>6:
        break