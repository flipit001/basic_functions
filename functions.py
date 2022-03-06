import json
import string
import random
from time import perf_counter, sleep
import inspect
def deletedupesforlists(List):
    return list(set(List))
def find_substrings(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:i + len(sub_string)] == sub_string:
                count += 1
    return count
def jsonwrite(text, file):
    with open(file, 'a') as f:
        json.dumps(text, f)
        f.write("\n")
def randomstring(long):
    return ''.join([random.choice([char for char in string.ascii_letters]) for _ in range(long)])
def randomword(long=None):
    with open("words.txt") as f:
        if long is None:
            l = random.choice([line for line in f.readlines()])
        else:
            words = [line if len(line.strip()) == long else '' for line in f.readlines()]
            try:
                l = random.choice(deletedupesforlists(words).remove(''))
            except:
                l = random.choice(deletedupesforlists(words))
    return l
def deletedupesforelements(string):
    temp_list = [char for char in string]
    anotherlist = {}
    for char in temp_list:
        if char in anotherlist:
            anotherlist[char] += 1
        else:
            anotherlist[char] = 1
    temp1 = temp_list[::-1]
    for char in temp_list:
        if anotherlist[char] != 1:
            anotherlist[char] -= 1
            temp1.remove(char)
    return ''.join(temp1[::-1])

def timeit(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        val = function(*args, **kwargs)
        print(f"function '{function.__name__}()' took {perf_counter() - start} seconds to execute!")
        return val
    
    return wrapper
@timeit
def add(a,b):
    sleep(2)
    return a+b

print(add(1,2))