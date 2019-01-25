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

