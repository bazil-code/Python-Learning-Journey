def bun_cheese(original_func):
    def wrapper():
        print("bun")
        original_func()
        print("cheese")
    return wrapper
def chicken():
    print("chicken")
burger = bun_cheese(chicken)
burger()
