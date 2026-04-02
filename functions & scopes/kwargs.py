#**kwargs

def myfriends(**kwargs):
    for key, value in kwargs.items():
        print(f"Hello {value}!")
a = {"nam1": "pedri", "nam2": "messi", "nam3": "shaka"}
myfriends(**a)