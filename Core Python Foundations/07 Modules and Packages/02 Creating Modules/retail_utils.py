def calculate_discount(price, rate):
    return price * (1 - rate)

def check_stock(stock):
    return "Low" if stock < 50 else "Sufficient"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price