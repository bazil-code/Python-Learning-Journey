def my_gen(n: int):
    start = 0
    while start < n:
        yield start
        start += 2
for i in my_gen(11):
    print(i)