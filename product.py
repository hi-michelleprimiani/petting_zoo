class Product:

    @property  # The getter
    def price(self):
        try:
            return self.__price  # Note there are 2 underscores here
        except AttributeError:
            return 0

    @price.setter  # The setter
    def price(self, new_price):
        if type(new_price) is float:
            self.__price = new_price
        else:
            raise TypeError(
                'Please provide a floating point value for the price')


prod = Product()
print(prod.price)
# prints 0

prod.price = 1.0