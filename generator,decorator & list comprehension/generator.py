# memory efficient than normal code

def my_gen(n: int):
    start = 0
    while start < n:
        yield start
        start += 1
for i in my_gen(10):
    print(i)
