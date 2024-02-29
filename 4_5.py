class Order:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price


class Customer:
    def place_order(self, product, quantity, price, processor):
        order = Order(product, quantity, price)
        processor.process_order(order)


class OrderProcessor:
    def __init__(self):
        self.orders = []

    def process_order(self, order):
        self.orders.append(order)
        print("Замовлення оброблено:", order.product, "-", order.quantity, "шт.")

    def total_revenue(self):
        return sum(order.total_price() for order in self.orders)

processor = OrderProcessor()
customer1 = Customer()
customer2 = Customer()

customer1.place_order("Ноутбук", 2, 1200, processor)
customer2.place_order("Смартфон", 1, 800, processor)
customer1.place_order("Мишка", 3, 25, processor)

print("Загальний дохід:", processor.total_revenue())
