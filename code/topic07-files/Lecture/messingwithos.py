# messsing with the os module
# Author Andrew Beatty

import os

FILENAME = "..\lab07.01-quiz-a.py"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line, end='')
else:
    print (FILENAME, "does not exist")


#os.remove("data2.txt")