from product import products

class store:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    def add_product(self, name):
        self.products.append(name)
        return self

    def print_info(self):
        for product in self.products:
            product.print_info()
        return self

    def sell_product(self, id):
        prod = self.products[id]
        print('Removing:', prod.print_info())
        del self.products[id]
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            if percent_increase > 0:
                product.update_price(percent_increase, True)
            else:
                product.update_price(percent_increase, False)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self





# prod1.update_price(.02, True).print_info()
