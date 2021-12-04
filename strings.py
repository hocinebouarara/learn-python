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

name = firstname+" "+lastname
print("The name is : ", name)     # The name is : hocine bouarara


# Format Strings

age = 26
txt = "My name is hocine, I am "+str(age)
print(txt)   # >>> My name is hocine, I am 26

txt = "My name is hocine, I am {}"
print(txt.format(age))  # >>> My name is hocine, I am 26

quantity=3
itemno=534
price=45.98
myOrder="I want {0} pieces of item {2} for {1} dollars."
print(myOrder.format(quantity,itemno,price)) # >>> I want 3 pieces of item 534 for 45.98

# same result with indexing
myOrder="I want {0} pieces of item {1} for {2} dollars."
print(myOrder.format(quantity,itemno,price)) # >>> I want 3 pieces of item 534 for 45.98






