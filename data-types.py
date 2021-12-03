
x = 5
print(type(x))   # >>> int 

a = "BOUARARA"
print(type(3))   # >>> str 

c = complex(20j-4)
print(type(c))    # >>> complex

ls = list (("apple","banana","cherry"))
print(ls)   # >>> ['apple', 'banana', 'cherry']
print (type(ls))  # >>> list

a = tuple(("apple","banana","cherry"))
print(a)    # >>> ('apple','banana','cherry')
print(type(a))  # >>> tuple

y = range(7)
print(y)   # >>> range(0,7)
print(type(y))  # range

dc = dict (name = "hocine",age = 26)
print(dc)   # >>> {'name':'hocine','age':26}
print(type(dc))  # >>> dict

fr = frozenset ({'apple','banana','cherry'})
print(fr)     # >>> frozenset({'apple', 'banana', 'cherry'})
print(type(fr))  # >>> frozenset