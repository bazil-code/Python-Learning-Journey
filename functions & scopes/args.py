def barca(name):
    print("Hello welcome to barca " + name + "!")
barca('pedri')
barca('messi')

def greet(*args):
    print("Hello " + args[0]+ "!")
    print("Hello " + args[1]+ "!")
    print("Hello " + args[2]+ "!")
greet('pedri', 'messi', 'shaka')
