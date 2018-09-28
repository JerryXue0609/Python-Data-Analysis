
d = {"jerry":18,"xuezhen":21,"hehe":22,"kkk":23}

g = [1,"张三",2,"李四",3,"王五"]
#for key,val in d.items():
 #   print("key,value is ",key,val)

for x,y in zip(g,reversed(g)):
    print("x is {0},y is {1}".format(x,y))

if __name__ == '__main__':
    print("main run")
