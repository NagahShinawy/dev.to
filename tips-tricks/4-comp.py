class Product:
    def __init__(self, name, price, owner=None, release=None):
        self.name = name
        self.price = price
        self.owner = owner
        self.release = release

    def __repr__(self):
        return f"{self.__class__.__name__}{self.name, self.price}"


if __name__ == "__main__":
    iphone = Product("Iphone Max", "12K")
    mac = Product("Macbook Pro", "30K")
    lenovo = Product("Lenovo Thinkpad", "25K")
    print(iphone)
    print(mac)
    print(lenovo)
    items = [iphone, mac, lenovo]
    print(items)

    items = [{"item": item.name, "price": item.price} for item in items]

    print(items)

    items = [
        {"item": "Iphone Max", "price": "12K"},
        {"item": "Macbook Pro", "price": "30K"},
        {"item": "Lenovo Thinkpad", "price": "25K"},
    ]
