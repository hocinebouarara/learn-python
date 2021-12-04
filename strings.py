print("Hello world!")  # >>> Hello world!

a = """ i use W3schols for learning 
it is best for learn web programing
.......
"""

print(a)  # >>> i use W3schools.com for learning
# it is best for learn web programing
# .......

a = "Hello World!"
print(a[0])    # >>> H

for x in "banana":
    print(x)  # >>> b
    # a
    # n
    # a
    # n
    # a
a = "hello world!"
print(len(a))  # >>> 12

txt = "The best things in life are free"
print("free" in txt)   # >>> True

if "free" in txt:
    print("Yes, 'free' is present")  # >>> Yes, 'free' is present

print("expensive" not in txt)   # >>> True

if "expensive" not in txt:
    # >>> No 'exepensive' is NOT present.
    print("No, 'expensive' is NOT present.")

# Slicing Strings

b = "Hello, World!"
print(b[2:5])  # >>> llo
print(b[:5])   # >>> Hello
print(b[2:])   # >>> ell, World!
print(b[-6:-1])


# Modify Strings
x = "Hocine bouarara"
print(x.upper())   # >>> HOCINE BOUARARA
x = "Hocine Bouarara"
print(x.lower())   # >>> hocine bouarara
x = "Hocine   Bouarara  "
print(x.strip())   # >>> hocine bouarara

print(x.replace('a', 'A'))  # >>> hocine bouArArA
x = "Hocine, Bouarara"

print(x.split(","))  # >>> ['Hocine','Bouarara']


#  String Concatination

firstname = "hocine"
lastname = "bouarara"
username = firstname + lastname
print("The user name is : ", username)   # The user name is : hocinebouarara

name=firstname+" "+lastname
print("The name is : ",name)     # The name is : hocine bouarara