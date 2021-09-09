# https://dev.to/codelearnern/notes-to-get-into-oop-in-python-3ak4

class Product:
    # class constructor
    # self keyword represent the object instance
    def __init__(self, name, description, price):
        # Set the object instance self.name
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.__class__.__name__}{self.name, self.price}"


if __name__ == '__main__':
    iphone = Product("Iphone", "Apple Iphone Max Pro", 12000)
    print(iphone)