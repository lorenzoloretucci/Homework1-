# -*- coding: utf-8 -*-
"""ScriptsHW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11LnCzu6khqScadVcrODMCyv9KqA2UXJ7

## **Problem 1**

Say "Hello, World!" With Python
"""

if __name__ == '__main__':
 
    print("Hello, World!")

"""Python If-Else"""

n = int(input())
check = {True: "Not Weird", False: "Weird"}

print(check[ n%2==0 and(n in range(2,6) or  n > 20)])

"""Arithmetic Operators"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a + b)
print(a-b)
print(a*b)

"""Python: Division"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a / b)

"""Loops"""

if __name__ == '__main__':
    n = int(input())
for i in range(n):
    if i < n:
        print(i**2)

"""Write a function"""

def is_leap(year):
    leap = False
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0 ):
        leap = True

    
    return leap

"""Print Function"""

if __name__ == '__main__':
    n = int(input())
for i in range(1, n+ 1):
    print(i, end='')

"""List Comprehensions"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print ([[q,w,e] for q in range(x+1)
 for w in range(y+1) 
 for e in range(z +1) 
 if ((q + w + e) != n) ])

"""Tuples"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

"""Finding the percentage"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    a = []
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
        
    for i in student_marks:
         if i == query_name:
            a = student_marks[i]
    mean = sum(a)/len(a)
    
    print("%.2f" % mean)

"""Find the Runner-Up Score!"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    B = list(set(list(arr)))
    C = len(B)
    D = sorted(B)
    print(D[C-2])

"""Nested Lists"""

a = []
b = []

if __name__ == '__main__':

    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([name, score])
        b.append(score)

    
    
    solonomi = []
    for el in range(len(a)):
        if a[el][1] == sorted(set(b))[1]:
            solonomi.append(a[el][0])
    
    solonomi.sort()
    for nome in solonomi:
        print(nome)

"""Lists"""

if __name__ == '__main__':

    N = int(input())

l = []

for i in range(N):
    cmd, *line = input().split()
    valori = list(map(int,line))
    if cmd == 'insert':
        l.insert(valori[0], valori[1])
    elif cmd == 'print':
        print(l)
    elif cmd =='remove':
        l.remove(valori[0])
    elif cmd == 'append':
        l.append(valori[0])
    elif cmd == 'sort':
        l.sort()
    elif cmd == 'pop':
        l.pop()
    elif cmd == 'reverse':
        l.reverse()

"""sWAP cASE"""

def swap_case(s):
    return s.swapcase()

"""String Split and Join"""

def split_and_join(line):
    
    return line.replace(' ', '-')
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

"""What's Your Name?"""

def print_full_name(a, b):
    print("Hello",str(a),str(b)+'!','You just delved into python.')

"""Mutations"""

def mutate_string(string, position, character):
    
    return string[:position] + character + string[position + 1:]

"""Text Wrap"""

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

"""Text Alignment"""

thickness = int(input()) 
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

"""Find a string"""

def count_substring(string, sub_string):
    total = 0
    count = None
    for i in range(len(string)):
        if len(string) > len(sub_string):
            count = string.find(sub_string)
            if (count>= 0):
                total += 1 
                string = string[(count+1):]

    return total

"""String Validators"""

if __name__ == '__main__':
    s = str(input())
    
print (any(a.isalnum() for a in s))
print(any (a.isalpha() for a in s))
print(any(a.isdigit() for a in s))
print(any(a.islower() for a in s))
print(any(a.isupper() for a in s))

"""Capitalize"""

def solve(s):
    return s.title()

"""Introduction to Sets"""

def average(array):
   Arr = set(array)
   return sum(Arr)/len(Arr)

"""Set .difference() Operation"""

N = int(input())
stud_E = set(map(int,input().split()))
n = int(input())
stud_F = set(map(int, input().split()))
print(len(stud_E - stud_F))

"""Set .intersection() Operation"""

N = int(input())
stud_E = set(map(int,input().split()))
n = int(input())
stud_F = set(map(int, input().split()))
print(len(stud_E & stud_F))

"""Set .union() Operation"""

n = int(input())
stud_E = set(map(int, input().split()))
N = int(input())
stud_F = set(map(int,input().split()))
print(len(stud_E | stud_F))

"""Set .add()"""

Ncountry = int(input())
country = set()
for i in range(Ncountry):
    country.add(str(input()))

print (len(country))

"""Symmetric Difference"""

n = int(input())
arr = set(map(int,input().split()))
N = int(input())
Arr = set(map(int,input().split()))
I1 = arr.difference(Arr)
I2 = Arr.difference(arr)
U = I1.union(I2)
Us = sorted(U)
print(*Us, sep='\n')

"""Set .symmetric_difference() Operation"""

N = int(input())
stud_E = set(map(int,input().split()))
n = int(input())
stud_F = set(map(int,input().split()))
print(len(stud_E ^ stud_F))

"""Set Mutations"""

n = int(input())
Set = set(map(int, input().split()))
N = int(input())

for n in range (N):
    cmd, line= input().split()
    Set1 = set(map(int, input().split()))
    if cmd == 'intersection_update':
        Set &= Set1
    elif cmd == 'update':
        Set |= Set1
    elif cmd == 'symmetric_difference_update':
        Set ^= Set1
    elif cmd == 'difference_update':
        Set -= Set1

print(sum(Set))

"""Check Subset"""

Nop = int(input())
for i in range(Nop):
    Nos = int(input())
    Set = set(map(int, input().split()))
    Nos2 = int(input())
    Set2 = set(map(int, input().split()))
    if Set & Set2 == Set:
        print ('True')
    else:
        print('False')

"""Check Strict Superset"""

Set1 = set(map(int,input().split()))
N = int(input())
for i in range (N):
    Set2 = set(map(int,input().split()))
    Set3 = set(map(int,input().split()))
    if (Set2 | Set3) != Set1:
        print('False')
        break
    else:
        print('True')

"""Set .discard(), .remove() & .pop()"""

for i in range(n):

    cmd = input().split()

    if cmd[0] == 'pop':
        Set.pop()
    elif cmd[0] == 'remove':
        Set.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        Set.discard (int(cmd[1]))

print(sum(Set)

"""collections.Counter()"""

from collections import Counter 
N = int(input())
NShoes = Counter(map(int,input().split()))
C = int(input())
Sum = 0

for i in range(C):
    S, P = map(int, input().split())
    if NShoes[S]:
        Sum += P
    
        NShoes[S] -= 1

print(Sum)

"""Alphabet Rangoli"""

def print_rangoli(size):
    
    A = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1,-size,-1):
        temp = '-'.join(A[size-1:abs(i):-1]+A[abs(i):size])
        print(temp.center(4*size-3,'-'))

"""DefaultDict Tutorial"""

from collections import defaultdict
N , M = map(int, input().split())

list1= defaultdict(list)

for i in range(1, N+1):
    list1[input()].append(str(i))
for el in range(M):
    print(' '.join(list1[input()]) or -1)

"""Collections.namedtuple()"""

from collections import namedtuple

N = int(input())

Students = namedtuple('Students', input())


Mark=[]

for i in range(N):
  Stud = Students(*input().split())
  Mark.append(Stud.MARKS)
  

Mark = list(map(int, Mark))
print(sum(Mark)/N)

"""Arrays"""

def arrays(arr):
    
    a = numpy.array((arr),float)
    
    return (a[::-1])

"""Shape and Reshape"""

import numpy

arr = list(map(int, input().split()))

G = numpy.array(arr)
print(numpy.reshape(G, (3,3)))

"""Transpose and Flatten"""

import numpy

n , m = input().split();
a = [];
for i in range(int(n)):
    Array = input().split();
    a.append(Array);
l= numpy.array(a,int);

print(numpy.transpose(l))

print(l.flatten())

"""Concatenate"""

import numpy 

N, M , P = map(int,input().split())

array1 =[]
array2 = []

for i in range(N):
    a = input().split()
    array1.append(a)

for y in range(M):
    b =input().split()
    array2.append(b)

Array1= numpy.array(array1, int)
Array2 = numpy.array(array2, int)
print(numpy.concatenate((Array1, Array2), axis= 0 ))

"""Zeros and Ones"""

import numpy

A = tuple(map(int, input().split()))

array1 = numpy.zeros((A), dtype = numpy.int)
array2 = numpy.ones((A), dtype = numpy.int)

print( array1)
print(array2)

"""Sum and Prod"""

import numpy

A, B = map(int, input().split())

arr = list(input().split() for i in range(A))
Arr = numpy.array(arr, int)

Array1 = numpy.array(Arr,int)
ArraySum= numpy.sum(Arr, axis= 0)

print(numpy.prod(ArraySum, axis= 0))

"""Min and Max"""

import numpy

A, B = map(int, input().split())

arr = list(input().split() for i in range(A))
Arr = numpy.array(arr, int)

array1 = numpy.min(Arr, axis= 1)

print(numpy.max(array1, axis = 0))

"""Mean, Var, and Std"""

import numpy

N,M = map(int, input().split())

A = []

for i in range(N):
    a = list(map(int, input().split()))
    a.append(A)

B = numpy.array(A)


print(numpy.mean(B, axis = 1))
print(numpy.var(B, axis = 0))
print(numpy.std(B))

"""Map and Lambda Function"""

cube = lambda x: x ** 3  

def fibonacci(n):
    a=[0,1]
    for i in range(n-2):
        a.append(a[-1]+a[-2])
    return [] if n==0 else [0] if n==1 else a
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

"""Zipped"""

A,i = map(int,input().split())
B=[]
for z in range(i):
    B.append(map(float,input().split()))

B = list(zip(*B))

for z in range(A):
    print(sum(B[z])/i)

"""## **Problem 2**

Birthday Cake Candles

*Resolve this exercise was easy. I use a function to complete it.*
"""

import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):
    
    return ar.count(max(ar))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

"""Viral Advertising

*I decided to solve the exercise by applying the mathematical formula shown in the text.*
"""

import math
import os
import random
import re
import sys


def viralAdvertising(n):
    comulative = 2
    share = 5
    like = 2
    
    for i in range(2, n+1):
        share = (share //2) * 3
        like =  share // 2
        comulative += like

    return comulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

"""Recursive digit Sum

*Perhaps the exercise on which I lost the most time. I wrote it several times but in the end I came to the solution in just a few steps.*
"""

import math
import os
import random
import re
import sys


def superDigit(n, k):
    
    if len(n) == 1:
        return(n)
    
    P =  sum(map(int, list(str(n))))
    P = P * k
        
    return (superDigit(str(P), 1))
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()