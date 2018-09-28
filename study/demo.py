#! usr/bin/env/ python3


def hello():
    print("hello world")

def getArea(width=10,height=10):
    return width*height

def print_info(arg,*args):
    print(arg)
    for i in args:
        print(i)
    return
def print_info2(arg,**kwargs):
    print(arg)
    print(kwargs)

if __name__ == "__main__":
    #print("area is =", getArea())
    #print_info(12,23,323,21)
    print_info2(21,a=23,b=32,c=34)
    sum = lambda a,b : a+b  #匿名函数 lambda
    print("相加的数为：", sum(23,42))