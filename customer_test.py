import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
	""" Tests of the Customer class"""

	def setUp(self):
		"""Test fixture contains:

    	c = a customer
    	movies = list of some movies
    	"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Dune: Part Two", 2024, ["Action", "Adventure"])
		self.regular_movie = Movie("Air", 2023, ["Drama"])
		self.childrens_movie = Movie("Frozen", 2013, ["Children"])

	def test_billing(self):
		rental_1 = Rental(self.new_movie, 2)
		self.c.add_rental(rental_1)
		self.assertEqual(self.c.get_total_charge(), 6.0)
		rental_2 = Rental(self.new_movie, 10)
		self.c.add_rental(rental_2)
		self.assertEqual(self.c.get_total_charge(), 36.0)
		rental_3 = Rental(self.regular_movie, 5)
		self.c.add_rental(rental_3)
		self.assertEqual(self.c.get_total_charge(), 42.5)
		rental_4 = Rental(self.childrens_movie, 5)
		self.c.add_rental(rental_4)
		self.assertEqual(self.c.get_total_charge(), 47.0)

	def test_statement(self):
		stmt = self.c.statement()
    	# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
    	# add a rental
		self.c.add_rental(Rental(self.new_movie, 4)) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])

	def test_total_rental_points(self):
		rental_1 = Rental(self.new_movie, 5)
		self.c.add_rental(rental_1)
		self.assertEqual(self.c.get_total_rental_points(), 5)
		rental_2 = Rental(self.new_movie, 10)
		self.c.add_rental(rental_2)
		self.assertEqual(self.c.get_total_rental_points(), 15)
		rental_3 = Rental(self.regular_movie, 3)
		self.c.add_rental(rental_3)
		self.assertEqual(self.c.get_total_rental_points(), 16)
		rental_4 = Rental(self.childrens_movie, 999)
		self.c.add_rental(rental_4)
		self.assertEqual(self.c.get_total_rental_points(), 17)
