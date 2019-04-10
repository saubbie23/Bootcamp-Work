from store import store
from product import products

store1 = store("Big Ron's")
prod1 = products('Apple', 4, 'Fruit')
prod2 = products('Banana', 10, 'Fruit')
prod3 = products('Plunger', 9, 'Worthless')
store1.add_product(prod1).add_product(prod2).add_product(prod3)
store1.print_info()
store1.set_clearance('Fruit', .4).print_info()