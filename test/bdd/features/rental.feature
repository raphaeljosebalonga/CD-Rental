Feature: cd rental
As the clerk of the cd_rental shop
I want to check out a CD for a customer
so that I can keep track of who has rented it

Scenario: Check Out CD
Given Customer has ID
Given CD has ID
Given CD is not currently rented
When Clerk checks out CD
Then CD recorded as rented
Then Rental contract printed