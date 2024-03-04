
# the with statement will atomatically close the file
# when it is finished with it

with open("test-a.txt",'wr') as f:
    data = f.read()
    print (data)

# The old way
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()