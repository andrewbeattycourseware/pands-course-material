# messing with files 
# Author: Andrew Beatty

FILENAME= "data.txt"
'''
with open(FILENAME, 'rt') as f:
    for data in f:
        #print(data , end="" )
        print(data.strip() )
        #print(data[:-1])
'''
with open("data2.txt", "w+") as f:
    f.write("what the hell\n")
    f.write("brown cow\n")
    f.seek(0)
    data = f.read()
    print(data)

print("done")
    
