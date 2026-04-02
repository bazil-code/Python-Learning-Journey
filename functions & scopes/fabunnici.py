def fabunnici(n):
    if n<= 2:
     return n
    else:
     return fabunnici(n - 1) + fabunnici(n - 2)
for n in range(1, 11):
    print(f"Fibonacci sequence up to {n} terms:")
    result = fabunnici(n)
    print(result)