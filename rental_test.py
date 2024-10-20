import unittest
from rental import Rental
from movie import Movie
from pricing import NEW_RELEASE, REGULAR, CHILDREN


class RentalTest(unittest.TestCase):

	def setUp(self):
		self.new_movie = Movie("Dune: Part Two")
		self.regular_movie = Movie("Air")
		self.childrens_movie = Movie("Frozen")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air")
		self.assertEqual("Air", m.get_title())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1, NEW_RELEASE)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5, NEW_RELEASE)
		self.assertEqual(rental.get_price(), 15.0)
		rental_regular = Rental(self.regular_movie, 4, REGULAR)
		self.assertEqual(rental_regular.get_price(), 5.0)
		rental_children = Rental(self.childrens_movie, 10, CHILDREN)
		self.assertEqual(rental_children.get_price(), 12.0)

	def test_rental_points(self):
		rental_new = Rental(self.new_movie, 5, NEW_RELEASE)
		self.assertEqual(rental_new.get_rental_points(), 5)
		rental_new = Rental(self.new_movie, 10, NEW_RELEASE)
		self.assertEqual(rental_new.get_rental_points(), 10)
		rental_regular = Rental(self.regular_movie, 5, REGULAR)
		self.assertEqual(rental_regular.get_rental_points(), 1)
		rental_regular = Rental(self.regular_movie, 10, REGULAR)
		self.assertEqual(rental_regular.get_rental_points(), 1)
		rental_children = Rental(self.childrens_movie, 5, CHILDREN)
		self.assertEqual(rental_children.get_rental_points(), 1)
		rental_children = Rental(self.childrens_movie, 10, CHILDREN)
		self.assertEqual(rental_children.get_rental_points(), 1)
