#! usr/bin/env python3
import datetime as t
from urllib import request
def readfile(filename):
    with open(filename,"r") as f:
        str = f.read()
        print(str)

def writefile(filename, filecontent):
    with open(filename,"a+")as f:
        f.write(filecontent)

def writeURLcontent(url,filename):
    res = request.urlopen(url)
    with open(filename,"w")as f:
        f.write(str(res.read()))

if __name__ == '__main__':
    #writefile("./test.txt","呵呵新增加的内容，时间：{}  \n".format(t.datetime.now()))
    writeURLcontent("http://www.baidu.com/","./test.txt")
    readfile("./test.txt")
