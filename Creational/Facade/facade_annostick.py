class Discount:
    def calculate(self, value):
        return value * 0.9


class Shipping:
    def calculate(self):
        return 5


class Fees:
    def calculate(self, value):
        return value * 1.05


class ShopeeFacadePattern:
    def __init__(self) -> None:
        self.discount = Discount()
        self.shipping = Shipping()
        self.fees = Fees()

    def calculate(self, price):
        price = self.discount.calculate(price)
        price = self.fees.calculate(price)
        price += self.shipping.calculate()

        return price
    
def buy(price):
    shoppe = ShopeeFacadePattern()
    print(f'Price:: {shoppe.calculate(price)}')

buy(120000)