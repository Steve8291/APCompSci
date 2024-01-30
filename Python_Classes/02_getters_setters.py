# # Python Getters & Setters ##
# Use this to make zero-argument methods accessible as if they were attributes.
# Makes sense when the calculation is stored as a variable.
# This give you some control over whether users can set or get a value.
# if you want to get a simple calculated value, @property is an excellent choice.
# If you want an elaborate value calculated, a method indicates that better.
# Use normal method get_price() when price is expensive to calculate or has side effects.
# If accessing the value requires passing arguments, you must use a method.


class House:
    def __init__(self, price):
        # Underscore indicates that price attribute is protected.
        # Tells other developers that price should not be accessed using dot notation.
        self._price = price

    @property
    def price(self):
        """The price property doc string"""
        return self._price

    # If you do not define a setter you can prevent user from setting value
    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price


house_obj = House(5000.0)
print(house_obj.price)
print(house_obj._price)  # Could still be accessed directly but should not be.

house_obj.price = 8000.00
print(house_obj.price)

house_obj.price = 600
print(house_obj.price)

print('\n')
help(house_obj)

# Delete price:
del house_obj.price
# print(house_obj.price)  # Will result in error
