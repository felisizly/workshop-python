# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

2 + 2
50 - 5*6
(50 - 5*6) / 4
8/5

17/3
17//3
17%3
5*3+2
5**2
2**7

width = 20
height = 5 * 9
width * height

n

4*3.75-1

tax = 12.5/100
price = 100.50
price*tax
price + _
round(_, 2)

'spam eggs'
'doesn\'t'
"doesn't"
'"Yes, they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'
s
print(s)

print('C:\some\name') 
print(r'C:\some\name')

print("""\
    Usage: thingy [OPTIONS]
    -h                  Display this usage message
    -H hostname         Hostname to connect to
    """)

3 * 'un' + 'ium'

'Py' 'thon'

text = ('Put several strings within parentheses'
        'to have them joined together.')
text

prefix = 'Py'
prefix 'thon'

word = 'Python'
word[0]
word[5]

word[-1]
word[-2]
word[-6]

word[0:2]
word[2:5]

word[:2]
word[4:]
word[-2:]

word[:2] + word[2:]
word[:4] + word[4:]

word[42]

word[4:42]
word[42:]

word[0] = 'J'
word[2:] = 'py'

'J' + word[1:]
word[:2] + 'py'

s = 'supercalifragilisticexpialidocious'
len(s)

squares = [1, 4, 9, 16, 25]
squares

squares [0]
squares[-1]
squares[-3]

squares[:]

squares + [36, 49, 64, 81, 100]

cubes = [1, 8, 27, 65, 125]
4 ** 3
cubes[3] = 64
print (cubes)

cubes.append(216) 
cubes.append(7 ** 3)
cubes

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
letters[2:5] = ['C', 'D', 'E']
letters
letters[2:5] = []
letters
letters[:] = []
letters

letters = ['a', 'b', 'c', 'd']
len(letters)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

i = 256*256
print('The value of i is', i)

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
