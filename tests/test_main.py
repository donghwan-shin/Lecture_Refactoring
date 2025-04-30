import unittest
import io
import contextlib

from main import CustomerManager, calculate_shipping_fee

class TestCustomerManager(unittest.TestCase):

    def test_add_customer(self):
        cm = CustomerManager()
        name = "Alice"
        purchases = [{'price': 50, 'item': 'banana'}, {'price': 80, 'item': 'apple'}]
        cm.add_customer(name, purchases)

        self.assertEqual(
            {name: purchases},
            cm.customers
        )

    def test_add_purchase(self):
        cm = CustomerManager()
        name = "Alice"
        purchase = {'price': 50, 'item': 'banana'}
        cm.add_purchase(name, purchase)

        self.assertEqual(
            {name: [purchase]},
            cm.customers
        )

    def test_add_purchase_multiple(self):
        cm = CustomerManager()
        name = "Alice"
        purchase = {'price': 50, 'item': 'banana'}
        cm.add_purchase(name, purchase)
        cm.add_purchase(name, purchase)

        self.assertEqual(
            {name: [purchase, purchase]},
            cm.customers
        )

    def test_discount_eligibility(self):
        cm = CustomerManager()
        cm.add_customer("Bob", [{'price': 600}])

        # Capture printed output
        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            cm.generate_report()

        output = captured.getvalue()

        self.assertIn("Bob", output)
        self.assertIn("Eligible for discount", output)

    def test_heavy_item_shipping_fee(self):
        purchases = [{'price': 100, 'weight': 25}]

        fee = calculate_shipping_fee(purchases, 'heavy')
        self.assertEqual(fee, 50)

    def test_fragile_item_shipping_fee(self):
        purchases = [{'price': 70, 'fragile': True}]

        fee = calculate_shipping_fee(purchases, 'fragile')
        self.assertEqual(fee, 60)

    def test_no_special_items_shipping_fee(self):
        purchases = [{'price': 40, 'weight': 5, 'fragile': False}]

        fee = calculate_shipping_fee(purchases)
        self.assertEqual(fee, 20)

        fee_fragile = calculate_shipping_fee(purchases, 'fragile')
        self.assertEqual(fee_fragile, 25)

    def test_add_purchases(self):
        cm = CustomerManager()
        name = "Alice"
        purchases = [{'price': 30}, {'price': 70}]
        cm.add_purchases(name, purchases)
        self.assertEqual(cm.customers[name], purchases)

    def test_get_total_spent(self):
        cm = CustomerManager()
        name = "Alice"
        purchases = [{'price': 90}, {'price': 150}]
        cm.add_customer(name, purchases)
        expected = 90 + 150 * 1.2  # One taxed, one not
        self.assertAlmostEqual(cm.get_total_spent(name), expected)

    def test_generate_report_no_discount(self):
        cm = CustomerManager()
        cm.add_customer("Bob", [{'price': 50}])

        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            cm.generate_report()
        output = captured.getvalue()

        self.assertIn("Bob", output)
        self.assertIn("No discount", output)

    def test_generate_report_potential(self):
        cm = CustomerManager()
        cm.add_customer("Bob", [{'price': 50}, {'price': 150}, {'price': 150}])

        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            cm.generate_report()
        output = captured.getvalue()

        self.assertIn("Bob", output)
        self.assertIn("Potential future discount customer", output)

    def test_generate_report_priority(self):
        cm = CustomerManager()
        cm.add_customer("Bob", [{'price': 700}])

        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            cm.generate_report()
        output = captured.getvalue()

        self.assertIn("Bob", output)
        self.assertIn("Eligible for discount", output)
        self.assertIn("Priority", output)

    def test_generate_report_vip(self):
        cm = CustomerManager()
        cm.add_customer("Bob", [{'price': 500}, {'price': 500}, {'price': 150}])

        captured = io.StringIO()
        with contextlib.redirect_stdout(captured):
            cm.generate_report()
        output = captured.getvalue()

        self.assertIn("Bob", output)
        self.assertIn("Eligible for discount", output)
        self.assertIn("VIP", output)

    def test_default_condition_heavy_shipping(self):
        purchases = [{'price': 40, 'weight': 25}]
        fee = calculate_shipping_fee(purchases)
        self.assertEqual(fee, 50)


if __name__ == "__main__":
    unittest.main()
