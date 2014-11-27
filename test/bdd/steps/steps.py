import sys
sys.path.insert(0, '../../..')

from lettuce import *
from nose.tools import assert_equal

from cd.cd_rental import Cd_rental
from cd.cd import Cd
from cd.customer import Customer

@step(u'Given Customer has ID')
def given_customer_has_id(step):
    customer = Customer("Fame Game", {})
    cd_rental = Cd_rental()
    cd_rental.add_customer(customer)
    assert_equal(cd_rental.check_customer_id("Fame Game", 1), {})

@step(u'Given CD has ID')
def given_cd_has_id(step):
    cd = Cd("Hunger Names", "some name", False)
    cd_rental = Cd_rental()
    cd_rental.add_cd(cd)
    assert_equal(cd_rental.get_rented_if("Hunger Names"), False)

@step(u'Given CD is not currently rented')
def given_cd_is_not_currently_rented(step):
    cd = Cd("Dawn Age", "some name", False)
    cd_rental = Cd_rental()
    cd_rental.add_cd(cd)
    assert_equal(cd_rental.get_rented_if("Dawn Age"), False)

@step(u'When Clerk checks out CD')
def when_clerk_checks_out_cd(step):
    cd = Cd("Arch Age", "some freaking name", False)
    customer = Customer("Jane", 0)
    cd_rental = Cd_rental()
    cd_rental.add_customer(customer)
    cd_rental.check_out(customer, cd)

@step(u'Then CD recorded as rented')
def then_cd_recorded_as_rented(step):
    cd = Cd("Fall", "name",  False)
    customer = Customer("James", 0)
    cd_rental = Cd_rental()
    cd_rental.add_customer(customer)
    cd_rental.add_cd(cd)
    cd_rental.check_out("James", "Fall")
    assert_equal(cd_rental.get_rented_if("Fall"), True)
    assert_equal(cd_rental.check_customer_id("James", 1), {'Fall': True})

@step(u'Rental contract printed')
def rental_contract_printed(step):
    cd = Cd("Breaking Bad", "name dammit", False)
    customer = Customer("Jones", 0)
    cd_rental = Cd_rental()
    cd_rental.add_customer(customer)
    cd_rental.add_cd(cd)
    cd_rental.check_out("Jones", "Breaking Bad")
    assert_equal(cd_rental.print_contract("Jones", "Breaking Bad"), (0, 'name dammit'))