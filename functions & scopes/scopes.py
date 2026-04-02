# local scope
def scope():
    x = 5
    print(x)
scope()

# global scope
x=10
def scope():
    global x
    print(x)
scope()
