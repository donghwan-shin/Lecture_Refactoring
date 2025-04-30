class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name, purchases):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)

    def generate_report(self):
        for name, purchases in self.customers.items():
            total_spent = 0
            for z in purchases:
                if z['price'] > self.tax_threshold:
                    taxed_price = z['price'] * (1 + self.tax_rate)
                    total_spent += taxed_price
                else:
                    total_spent += z['price']
            print(name)
            if total_spent > self.discount_threshold:
                print("Eligible for discount")
            else:
                if total_spent > 300:
                    print("Potential future discount customer")
                else:
                    print("No discount")
            if total_spent > 1000:
                print("VIP Customer!")
            else:
                if total_spent > 800:
                    print("Priority Customer")

def calculate_shipping_fee(purchases, condition='heavy'):
    if condition == 'heavy':
        for purchase in purchases:
            if purchase.get('weight', 0) > 20:
                return 50
        return 20
    elif condition == 'fragile':
        for purchase in purchases:
            if purchase.get('fragile', False):
                return 60
        return 25