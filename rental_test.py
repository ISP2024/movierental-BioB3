import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
		self.regular_movie = Movie("Air", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", Movie.REGULAR)
		self.assertEqual("Air", m.get_title())
		self.assertEqual(Movie.REGULAR, m.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental_regular = Rental(self.regular_movie, 4)
		self.assertEqual(rental_regular.get_price(), 5.0)
		rental_children = Rental(self.childrens_movie, 10)
		self.assertEqual(rental_children.get_price(), 12.0)

	def test_rental_points(self):
		rental_new = Rental(self.new_movie, 5)
		self.assertEqual(rental_new.rental_points(), 5)
		rental_new = Rental(self.new_movie, 10)
		self.assertEqual(rental_new.rental_points(), 10)
		rental_regular = Rental(self.regular_movie, 5)
		self.assertEqual(rental_regular.rental_points(), 1)
		rental_regular = Rental(self.regular_movie, 10)
		self.assertEqual(rental_regular.rental_points(), 1)
		rental_children = Rental(self.childrens_movie, 5)
		self.assertEqual(rental_children.rental_points(), 1)
		rental_children = Rental(self.childrens_movie, 10)
		self.assertEqual(rental_children.rental_points(), 1)
