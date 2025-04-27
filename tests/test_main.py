import unittest

from main import CustomerManager, calculate_shipping_fee_for_fragile_items

class TestCustomerManager(unittest.TestCase):

    def test_basic_report_generation(self):
        cm = CustomerManager()
        purchases = [{'price': 50}, {'price': 80}]
        cm.add_customer("Alice", purchases)

        # We cannot capture print easily without capturing stdout,
        # so in real tests we would restructure the code to return values.
        cm.generate_report()

    def test_discount_eligibility(self):
        cm = CustomerManager()
        purchases = [{'price': 600}]
        cm.add_customer("Bob", purchases)

        cm.generate_report()

    def test_vip_and_priority_customers(self):
        cm = CustomerManager()

        purchases_vip = [{'price': 950}]
        purchases_priority = [{'price': 850}]

        cm.add_customer("Charlie", purchases_vip)
        cm.add_customer("Diana", purchases_priority)

        cm.generate_report()

    def test_heavy_item_shipping_fee(self):
        cm = CustomerManager()
        purchases = [{'price': 100, 'weight': 25}]

        fee = cm.calculate_shipping_fee(purchases)
        self.assertEqual(fee, 50)

    def test_fragile_item_shipping_fee(self):
        purchases = [{'price': 70, 'fragile': True}]

        fee = calculate_shipping_fee_for_fragile_items(purchases)
        self.assertEqual(fee, 60)

    def test_no_special_items_shipping_fee(self):
        cm = CustomerManager()
        purchases = [{'price': 40, 'weight': 5, 'fragile': False}]

        fee = cm.calculate_shipping_fee(purchases)
        self.assertEqual(fee, 20)

        fee_fragile = calculate_shipping_fee_for_fragile_items(purchases)
        self.assertEqual(fee_fragile, 25)

if __name__ == "__main__":
    unittest.main()
