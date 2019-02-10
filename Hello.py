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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Python Variables Are Pointers
x = [1, 2, 3]
y = x
print(y)
x.append(4) # append 4 to the list pointed to by x
print(y) # y's list is modified as well!

x=4
y=x
x = 'something else'
# Note also that if we use = to assign another value to x, this will not
# affect the value of y—assignment is simply a change of what object
# the variable points to
print(y) # y is unchanged
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# iterates over all permutations of a sequence
from itertools import permutations
p = permutations(range(3))
print(*p)

from itertools import combinations
c = combinations(range(4), 2)
print(*c)

from itertools import product
p = product('ab', range(3))
print(*p)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# List Comprehensions
[i for i in range(20) if i % 3 > 0]

# Basic List Comprehensions
L = []
for n in range(12):
    L.append(n ** 2)
L

[n**2 for n in range(12)]

# Multiple Iteration
[(i, j) for i in range(2) for j in range(3)]

# Conditions on the Iterator
[val for val in range(20) if val % 3 > 0]

# what we’re doing is constructing a list, leaving out multiples of 3,
# and negating all multiples of 2.
[val if val % 2 else -val for val in range(20) if val % 3]

{a % 3 for a in range(1000)}
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# generator expression:
# a list comprehension in which
# elements are generated as needed rather than all at once
print(n**2 for n in range(12))


# 1. List comprehensions use square brackets, 
# while generator expressions use parentheses

# to print the contents of a generator expression is
# to pass it to the list constructor
list(n**2 for n in range(12))

# 2. A list is a collection of values, 
# while a generator is a recipe for producing values
L = [n ** 2 for n in range(12)]
for val in L:
    print(val, end=' ')

# generator expression does not actually compute
# the values until they are needed.
G = (n ** 2 for n in range(12))
for val in G:
    print(val, end=' ')

# The count iterator will go on happily counting forever until you tell
# it to stop; this makes it convenient to create generators that will also
# go on forever:
from itertools import count
factors = [2, 3, 5, 7]
G = (i for i in count() if all(i % n > 0 for n in factors))
for val in G:
    print(val, end=' ')
    if val > 40: break

# 3. A list can be iterated multiple times; a generator expression is single use
L = [n ** 2 for n in range(12)]
for val in L:
    print(val, end=' ')

for val in L:
    print(val, end=' ')
print()

G = (n ** 2 for n in range(12))
# print(*G)
# print(*G)

list(G)
list(G)

# This can be very useful 
# because it means iteration can be stopped and started:
G = (n**2 for n in range(12))
for n in G:
    print(n, end=' ')
    if n > 30: break
print("\ndoing something in between")

for n in G:
    print(n, end=' ')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Generator Functions: Using yield
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
L1 = [n ** 2 for n in range(12)]
L2 = []
for n in range(12):
    L2.append(n ** 2)

print(L1)
print(L2)

G1 = (n ** 2 for n in range(12))
def gen():
    for n in range(12):
        yield n ** 2
G2 = gen()
print(*G1)
print(*G2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Generators -> Example: Prime Number Generator
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Generate a list of candidates
L = [n for n in range(2, 40)]
print(L)

# Remove all multiples of the first value
L = [n for n in L if n == L[0] or n % L[0] > 0]
print(L)

# Remove all multiples of the second value
L = [n for n in L if n == L[1] or n % L[1] > 0]
print(L)

# Remove all multiples of the third value
L = [n for n in L if n == L[2] or n % L[2] > 0]
print(L)

def gen_primes(N):
# """Generate primes up to N"""
    primes = set()
    for n in range(2, N):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

print(*gen_primes(70))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Modules and Packages
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Loading Modules: the import Statement
# Explicit module import
import math
math.cos(math.pi)
# Explicit module import by alias
import numpy as np
np.cos(np.pi)
# Explicit import of module contents
from math import cos, pi
cos(pi)
# Implicit import of module contents
from math import *
sin(pi) ** 2 + cos(pi) ** 2

from numpy import *
sum(range(5), -1)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# String Manipulation and Regular Expressions
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
multiline = """
one
two
three
"""

fox = "tHe qUICk bROWn fOx."
fox.upper()
fox.lower()
fox.title()
fox.capitalize()
fox.swapcase()

# Formatting strings: Adding and removing spaces
line = ' this is the content '
line.strip()
line.rstrip()
line.lstrip()

num = "000000000000435"
num.strip('0')

line = "this is the content"
line.center(30)
line.ljust(30)
line.rjust(30)

'435'.rjust(10, '0')
# right-pad a string with zeros
'435'.zfill(10)

# Finding and replacing substrings
# 
line = 'the quick brown fox jumped over a lazy dog'
line.find('fox')
line.index('fox')
line.find('bear')
# not found: index() raises a ValueError
line.index('bear')

line.rfind('a')

line.endswith('dog')
line.startswith('fox')

# The replace() function returns a new string
line.replace('brown', 'red')
line.replace('o', '--')

# Splitting and partitioning strings

# A more sophisticated example
import re
email = re.compile('\w+@\w+\.[a-z]{3}')
text = "To email Guido, try guido@python.org \
or the older address guido@google.com."
email.findall(text)

email.sub('--@--.--', text)

email.findall('barack.obama@whitehouse.gov')

# Basics of regular expression syntax

# Simple strings are matched directly
regex = re.compile('ion')
regex.findall('Great Expectations')

# Some characters have special meanings
# r preface in r'\$' indicates a raw string
# the backslash is used to indicate special characters.
regex = re.compile(r'\$')

regex.findall("the cost is $20")

print('a\tb\tc')
print(r'a\tb\tc')

# Special characters can match character groups.
# the character \w, which is a
# special marker matching any alphanumeric character.
# \s, a special marker indicating
# any whitespace character.

regex = re.compile(r'\w\s\w')
regex.findall('the fox is 9 years old')

# Square brackets match custom character groups
# match any lowercase vowel
regex = re.compile('[aeiou]')
regex.split('consequential')

# 
regex = re.compile('[A-Z][0-9]')
regex.findall('1043879, G2, H6')

# Wildcards match repeated characters.
regex = re.compile(r'\w{3}')
regex.findall('The quick brown fox')

regex = re.compile(r'\w+')
regex.findall('The quick brown fox')

email = re.compile(r'\w+@\w+\.[a-z]{3}')
email2 = re.compile(r'[\w.]+@\w+\.[a-z]{3}')
email2.findall('barack.obama@whitehouse.gov')

# Parentheses indicate groups to extract
email3 = re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
text = "To email Guido, try guido@python.org"\
"or the older address guido@google.com."
email3.findall(text)

email4 = re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+)'\
'\.(?P<suffix>[a-z]{3})')
match = email4.match('guido@python.org')
match.groupdict()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# A Preview of Data Science Tools
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# NumPy: Numerical Python
import numpy as np
x = np.arange(1, 10)
x
x ** 2

# reshape our x array into a 3x3 array
M = x.reshape((3, 3))
M

# transpose using .T
M.T

# a matrix-vector product using np.dot
# [5*1+2*6+3*7, 4*5+5*6+6*7, 7*5+8*6+9*7]
np.dot(M, [5, 6, 7])

# eigenvalue decomposition
np.linalg.eigvals(M)

# Pandas: Labeled Column-Oriented Data
# Pandas is a much newer package than NumPy, 
# and is in fact built on top of it
import pandas as pd
df = pd.DataFrame({'label': ['A', 'B', 'C', 'A', 'B', 'C'],
'value': [1, 2, 3, 4, 5, 6]})
df
df['label']
df['label'].str.lower()
df['value']
df['value'].sum()

df.groupby('label').sum()

# Matplotlib: MATLAB-style scientific visualization

# run this if using Jupyter notebook

import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = np.linspace(0, 10) # range of values from 0 to 10
y = np.sin(x) # sine of these values
plt.plot(x, y); # plot as a line

# SciPy: Scientific Python
from scipy import interpolate
# choose eight points between 0 and 10
x = np.linspace(0, 10, 8)
y = np.sin(x)
# create a cubic interpolation function
func = interpolate.interp1d(x, y, kind='cubic')
# interpolate on a grid of 1,000 points
x_interp = np.linspace(0, 10, 1000)
y_interp = func(x_interp)
# plot the results
plt.figure() # new figure
plt.plot(x, y, 'o')
plt.plot(x_interp, y_interp);


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



































