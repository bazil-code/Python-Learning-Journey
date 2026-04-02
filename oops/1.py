class kettle:
    power_src = "Electricity" #universal attribute
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def switch_on(self):
        print("Kettle is switched on.")

    def switch_off(self):
        print("Kettle is switched off.")
kettle1 = kettle("Philips", 1500)
kettle2 = kettle("Bosch", 2000)

print(kettle1.brand)  # Output: Philips
print(kettle2.price)  # Output: 2000
kettle1.switch_on()  # Output: Kettle is switched on.
kettle2.switch_off()  # Output: Kettle is switched off.
print(kettle1.power_src)  # Output: Electricity

# Accessing class attribute using class name - name spaces
# print(kettle.__dict__)