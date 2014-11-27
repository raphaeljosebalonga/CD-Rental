import sys
sys.path.insert(0, '../../')

import unittest

from cd.customer import Customer

class TestCustomer(unittest.TestCase):
	def test_customer_object_can_be_created(self):
	    customer = Customer("001", "John")
	    self.assertEqual(customer.customer_id, "001")
	    self.assertEqual(customer.customer_name, "John")


if __name__ == '__main__':
	unittest.main()