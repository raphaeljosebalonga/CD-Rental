import sys
sys.path.insert(0, '../../')

import unittest

from cd.cd_rental import Cd_rental
from cd.cd import Cd
from cd.customer import Customer

class TestCdRental(unittest.TestCase):
	def setUp(self):
		self.cd_rental = Cd_rental()
		
	def test_if_cd_rental_is_initially_empty(self):
		self.assertEqual({}, self.cd_rental.cds)
		self.assertEqual({}, self.cd_rental.customers)
		self.assertEqual(len(self.cd_rental.cds), 0)
		self.assertEqual(len(self.cd_rental.customers), 0)

	def test_add_customer(self):
		customer_1 = Customer(1, "James")
		customer_2 = Customer(2, "John")

		self.cd_rental.add_customer(customer_1)
		self.cd_rental.add_customer(customer_2)

		self.assertEqual(len(self.cd_rental.customers), 2)

	def test_add_cds(self):
		cd_1 = Cd(1, "Insert Disc", False)
		cd_2 = Cd(2, "Eject Disc", False)

		self.cd_rental.add_cd(cd_1)
		self.cd_rental.add_cd(cd_2)

		self.assertEqual(len(self.cd_rental.cds), 2)

	def test_customer_id_not_found_1(self):
		self.assertEqual(self.cd_rental.check_customer_id("001", 1), "Try Again.")

	def test_customer_id_not_found_2(self):
		self.assertEqual(self.cd_rental.check_customer_id("001", 1), "Try Again.")

		customer_1 = Customer(1, "James")

		self.cd_rental.add_customer(customer_1)

		self.assertEqual(self.cd_rental.check_customer_id(1, 2), {})

	def test_customer_id_not_found_3(self):
		cd_rental = Cd_rental()
		self.assertEqual(cd_rental.check_customer_id("001", 1), "Try Again.")
		self.assertEqual(cd_rental.check_customer_id("001", 2), "No Customer found with given customer ID.")


	def test_check_customer_id(self):
		customer_1 = Customer(1, "James")

		self.cd_rental.add_customer(customer_1)

		self.assertEqual(self.cd_rental.check_customer_id(1, 1), {})

	def test_get_rented(self):
		cd_1 = Cd(1, "Insert Disc", False)

		self.cd_rental.add_cd(cd_1)

		self.assertEqual(self.cd_rental.get_rented_if(0001), False)

	def test_record_rented(self):
		customer = Customer(1, "James")
		cd = Cd(1, "Insert Disc", False)

		self.cd_rental.add_cd(cd)

		self.cd_rental.add_customer(customer)

		self.cd_rental.check_out(1, 1)

		self.assertEqual(self.cd_rental.check_customer_id(1, 1), {1: True})
		self.assertEqual(self.cd_rental.get_rented_if(001), True)

	def test_violate_business_rules(self):
		customer = Customer(1, "James")
		customer2 = Customer(2, "John")
		cd1 = Cd(1, "Insert Disc", False)
		cd2 = Cd(2, "Insert Disc", False)
		cd3 = Cd(3, "Insert Disc", False)
		cd4 = Cd(4, "Insert Disc", False)

		self.cd_rental.add_cd(cd1)
		self.cd_rental.add_cd(cd2)
		self.cd_rental.add_cd(cd3)
		self.cd_rental.add_cd(cd4)
		self.cd_rental.add_customer(customer)
		self.cd_rental.add_customer(customer2)

		self.cd_rental.check_out(1, 4)
		self.cd_rental.check_out(1, 1)
		self.cd_rental.check_out(1, 2)

		self.assertEqual(self.cd_rental.check_out(1, 3), "Violated CD Rental Limit business rule")
		self.assertEqual(self.cd_rental.customers.get(2), {})
		self.assertEqual(self.cd_rental.customers.get(23), None)


	def test_print_contract(self):
		customer = Customer(1, "James")
		cd = Cd("Breaking Bad", "Insert Disc", False)

		self.cd_rental.add_customer(customer)
		self.cd_rental.add_cd(cd)

		self.cd_rental.check_out(1, "Breaking Bad")

		self.assertEqual(self.cd_rental.print_contract(1, "Breaking Bad"), ("James", "Insert Disc"))


if __name__ == '__main__':
	unittest.main()