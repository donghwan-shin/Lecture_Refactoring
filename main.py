class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.potential_discount_threshold = 300
        self.discount_threshold = 500
        self.priority_threshold = 800
        self.vip_threshold = 1000

    def add_customer(self, name, purchases):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)

    def get_total_spent(self, name):
        total_spent = 0
        for purchase in self.customers[name]:
            if purchase['price'] > self.tax_threshold:
                total_spent += purchase['price'] * (1 + self.tax_rate)
            else:
                total_spent += purchase['price']

        return total_spent

    def generate_report(self):
        for name, purchases in self.customers.items():
            total_spent = self.get_total_spent(name)

            print(name)
            if total_spent > self.discount_threshold:
                print("Eligible for discount")

                if total_spent > self.vip_threshold:
                    print("VIP Customer!")
                elif total_spent > self.priority_threshold:
                        print("Priority Customer")

            else:
                if total_spent > self.potential_discount_threshold:
                    print("Potential future discount customer")
                else:
                    print("No discount")


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