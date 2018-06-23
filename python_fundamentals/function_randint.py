# As part of this assignment, please create a function randInt() where

# randInt() returns a random integer between 0 to 100
# randInt(max=50) returns a random integer between 0 to 50
# randInt(min=50) returns a random integer between 50 to 100
# randInt(min=50, max=500) returns a random integer between 50 and 500
# Create this function without using random.randInt() but you are allowed to use random.random().

import random
# randInt() returns a random integer between 0 to 100
def rand_int():
    num = round(random.random() * 100)
    return num

# randInt(max=50) returns a random integer between 0 to 50
def rand_max():
    num = random.randrange(0,50)
    return num

# randInt(min=50) returns a random integer between 50 to 100
def rand_min():
    num = random.randrange(50,100)
    return num

# randInt(min=50, max=500) returns a random integer between 50 and 500
def rand_big():
    num = random.randrange(50,500)
    return num
