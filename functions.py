import json
import string
import random
from time import perf_counter, sleep
import inspect

def delete_dupes_for_lists(List):
    return list(set(List))

def find_substrings(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:i + len(sub_string)] == sub_string:
                count += 1
    return count

def json_write(text, file):
    with open(file, 'a') as f: 
        json.dumps(text, f)
        f.write("\n")

def random_string(long):
    return ''.join([random.choice([char for char in string.ascii_letters]) for _ in range(long)])

def random_word(long=None):
    with open("words.txt") as f:
        if long is None:
            l = random.choice([line for line in f.readlines()])
        else:
            words = [line if len(line.strip()) == long else '' for line in f.readlines()]
            try:
                l = random.choice(delete_dupes_for_lists(words).remove(''))
            except:
                l = random.choice(delete_dupes_for_lists(words))

    return l

def delete_dupes_for_elements(string):
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

def time_it(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        val = function(*args, **kwargs)
        print(f"function '{function.__name__}()' took {perf_counter() - start} seconds to execute!")

        return val
    
    return wrapper


def int_to_list(n): # can not do negative

    if n < 0:
        raise Exception("'int_to_list' function does not take negative numbers")

    temp = []
    

    while n > 0:
        temp.append(n % 10)
        n //= 10

    return temp[::-1]


def word_count(s):
    temp = {}

    s = s.split()

    for word in s:
        if word in temp:
            temp[word] += 1
        else:
            temp[word] = 1

    return temp



def list_to_int(l):
    s = ""
    for char in l:
        s += str(char)

    return int(s)


if __name__ == "__main__": # for debugging:
    print(word_count("as fas fas"))



