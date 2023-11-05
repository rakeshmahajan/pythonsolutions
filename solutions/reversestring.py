# List in general and conversion of List to string
# For and While loop
# reversed, range, len functions
# time library

import time

originalstr = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
reversedstring = ""
CHECKTIME = True

def solution1():
    global reversedstring
    reversedstring = ""
    for i in originalstr:
        reversedstring = i + reversedstring
    if not CHECKTIME:
        print(reversedstring)

def solution2():
    global reversedstring
    reversedstring = ""
    strlen = len(originalstr)
    for i in reversed(range(0, strlen)):
        reversedstring = reversedstring + originalstr[i]
    if not CHECKTIME:
        print(reversedstring)

# Using slicing
def solution3():
    x = originalstr[::-1]
    if not CHECKTIME:
        print(originalstr[::-1])

# Using reversed() and list() function
def solution4():
    global reversedstring
    reversedstring = ""
    for ele in list(reversed(originalstr)):
        reversedstring = reversedstring + ele

    if not CHECKTIME:
        print(reversedstring)

def execute(funcname):
    n = 10000
    start = time.time_ns()
    for i in range(n):
        funcname()
    end = time.time_ns()
    diff = end - start
    end_millis = diff // 1000000
    print(f"Total time to reverse string using {funcname} {n} times :  {end - start} ( {end_millis} millis )")


if __name__ == '__main__':
    print(f"String reverse time for string with lenght {len(originalstr)}")
    if CHECKTIME:
        execute(solution1)
        execute(solution2)
        execute(solution3)
        execute(solution4)
    else:
        solution1()
        solution2()
        solution3()
        solution4()
