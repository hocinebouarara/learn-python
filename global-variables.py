
z = 'hocine'
def myfunc():
    print(z)

myfunc()  # >>> hocine


def myfunc1():
    global z
    z = "bouarara"
myfunc1()
print("my last name is ",z)  #   >>> bouarara
