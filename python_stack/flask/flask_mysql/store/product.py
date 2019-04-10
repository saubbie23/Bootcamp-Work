class products:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def print_info(self):
        print(f"Product name: {self.name}\nPrice: ${self.price}\nCategory:{self.category}")
        return self

    def update_price(self, percent_change, is_increased):
        if is_increased:
            pct_diff = self.price * percent_change
            self.price += pct_diff
        else:
            pct_diff = self.price * (percent_change)
            self.price -= pct_diff
        return self
