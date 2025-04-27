class CustomerManager:
    def __init__(self):
        self.customers = []
        self.taxRate = 0.2
        self.discountThreshold = 500

    def add_customer(self, name, purchases):
        self.customers.append((name, purchases))

    def generate_report(self):
        for name, purchases in self.customers:
            total_spent = 0
            for purchase in purchases:
                if purchase['price'] > 100:
                    taxed_price = purchase['price'] * (1 + self.taxRate)
                    total_spent += taxed_price
                else:
                    total_spent += purchase['price']
            print(name)
            if total_spent > self.discountThreshold:
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

    def calculate_shipping_fee(self, purchases):
        heavy_item = False
        for purchase in purchases:
            if purchase.get('weight', 0) > 20:
                heavy_item = True
                break
        if heavy_item:
            return 50
        else:
            return 20

def calculate_shipping_fee_for_heavy_items(purchases):
    for purchase in purchases:
        if purchase.get('weight', 0) > 20:
            return 50
    return 20

def calculate_shipping_fee_for_fragile_items(purchases):
    fragile_item = False
    for purchase in purchases:
        if purchase.get('fragile', False):
            fragile_item = True
            break
    if fragile_item:
        return 60
    else:
        return 25

flat_tax = 0.2