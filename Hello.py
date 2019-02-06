msg="Hello,World!"

## git remote rm origin
## git remote rm upstream
## git remote add origin git@github.com:jiuningzhong/MIT-6.1.git
## git push --set-upstream origin master

print(msg)

type(5)
print(3.0-1)

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

L = [1,3,5,1,2,3,4,5]
L.sort()

L = []
nmax = 30
for n in range(2, nmax):
    for factor in L:
        #print(str(n)+ ' ' + str(factor))
        if n % factor == 0:
            break
    else: # no break
        L.append(n)
        print(L)
print(L)

def real_imag_conj(val):
    return val.real, val.imag, val.conjugate()

def fibonacci(N, a=0, b=1):
    L = []
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

def catch_all(*args, **kwargs):
    print("args =", args)
    print("kwargs = ", kwargs)

inputs = (1, 2, 3)
keywords = {'pi': 3.14}

catch_all(*inputs, **keywords)
catch_all('a', keyword=2)
catch_all(1, 2, 3, a=4, b=5)

data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
{'first':'Grace', 'last':'Hopper', 'YOB':1906},
{'first':'Alan', 'last':'Turing', 'YOB':1912}]

sorted([2,4,3,5,1,7,98,93,6])

sorted(data, key=lambda item: item['first'])
sorted(data, key=lambda item: item['YOB'])

add = lambda x, y: x + y
add(1, 2)

def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 1E100

safe_divide(1,0)
safe_divide(1,'a')

def fibonacci_non_negative(N):
    if N < 0:
        raise ValueError("N must be non-negative")
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

fibonacci_non_negative(-10)

N = -10
try:
    print("trying this...")
    print(fibonacci(N))
except ValueError:
    print("Bad value: need to do something else")

try:
    x = 1 / 0
except ZeroDivisionError as err:
    print("Error class is: ", type(err))
    print("Error message is:", err)

class MySpecialError(ValueError):
    pass

# raise MySpecialError("here's the message")

try:
    print("do something")
    raise MySpecialError("[informative error message here]")
except MySpecialError:
    print("do something else")

# Iterators
for i in range(10):
    print(i, end=' \n')
    # print('\n')

# try…except…else…finally
try:
    print("try something here")
except:
    print("this happens only if it fails")
else:
    print("this happens only if it succeeds")
finally:
    print("this happens no matter what")

# Iterating over lists
for value in [2, 4, 6, 8, 10]:
    # do some operation
    print(value + 1, end=' \n')

I = iter([2, 4, 6, 8, 10])
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))

# range(): A List Is Not Always a List
range(10)

for i in range(10):
    print(i, end=' ')

N = 10 ** 12
for i in range(N):
    if i >= 10: break
    print(i, end=', ')

# Useful Iterators
L = [2, 4, 6, 8, 10]
for i in range(len(L)):
    print(i, L[i])

# enumerate iterator
for i, val in enumerate(L):
    print(i, val)

# zip iterator
L = [2, 4, 6, 8, 10]
R = [3, 6, 9, 12, 15]
for lval, rval in zip(L, R):
    print(lval, rval)

# find the first 10 square numbers
# The map iterator takes a function 
# and applies it to the values in an iterator
square = lambda x: x ** 2
for val in map(square, range(10)):
    print(val, end=' ')

# find values up to 10 for which x % 2 is zero
# filter iterator looks similar, except it only passes through values
# for which the filter function evaluates to True
is_even = lambda x: x % 2 == 0
for val in filter(is_even, range(10)):
    print(val, end=' ')

# *args and **kwargs can be used to 
# pass sequences and dictionaries to functions
# The operative difference is the asterisk characters:
# a single * before a variable means “expand this as a sequence”, while
# a double ** before a variable means “expand this as a dictionary”.

print(*range(10))

print(*map(lambda x: x ** 2, range(10)))

L1 = (1, 2, 3, 4)
L2 = ('a', 'b', 'c', 'd')
z = zip(L1, L2)
print(*z)

z = zip(L1, L2)
new_L1, new_L2 = zip(*z)
print(new_L1, new_L2)

# iterates over all permutations of a sequence
from itertools import permutations
p = permutations(range(3))
print(*p)