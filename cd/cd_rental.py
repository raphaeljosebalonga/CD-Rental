from cd import Cd
from customer import Customer

class Cd_rental(object):
	def __init__(self):
		self.customers = {}
		self.cds = {}
		self.rented_list = {}
		self.customers_name = {}
		self.cds_name = {}

	def add_customer(self, customer):
		self.customers[customer.customer_id] = {}
		self.customers_name[customer.customer_id] = customer.customer_name

	def add_cd(self, cd):
		self.cds[cd.cd_id] = cd.rented
		self.cds_name[cd.cd_id] = cd.cd_name

	def check_customer_id(self, customer_id, tries):
		result = self.customers.get(customer_id)
		if tries < 2:
		    if result == None:
		    	return "Try Again."
		    else:
		    	return result
		else:
			if result == None:
			    return "No Customer found with given customer ID."
			else:
				return result

	def get_rented_if(self, cd_id):
		return self.cds.get(cd_id)

	def check_out(self, customer_id, cd_id):
		if len(self.rented_list) >= 3:
			return "Violated CD Rental Limit business rule"
		else:
			if self.customers.get(customer_id) != None:
				if self.cds.get(cd_id) == False:
					self.rented_list[cd_id] = True
					self.customers[customer_id] = self.rented_list
					self.cds[cd_id] = True
					return self.rented_list
				elif self.cds.get(cd_id) == True:
					return "CD already rented"
				else:
					return "No CD in Library"

	def print_contract(self, customer_id, cd_id):
		return self.customers_name.get(customer_id), self.cds_name.get(cd_id)