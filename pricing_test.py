import unittest
from rental import Rental
from movie import Movie
from pricing import NEW_RELEASE, REGULAR, CHILDREN


class PricingTest(unittest.TestCase):
    """Tests for get_price_for_movie method."""

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, ["Action", "Adventure"])
        self.regular_movie = Movie("Air", 2023, ["Drama"])
        self.childrens_movie = Movie("Frozen", 2013, ["Children"])

    def test_childrens_movies(self):
        """Movies with children genre should have ChildrensPrice as price code."""
        movie1 = Movie("Frozen", 2013, ["Children"])
        movie2 = Movie("Shrek", 2001, ["Children", "Comedy", "Fantasy"])
        movie3 = Movie("Khan Kluay", 2006, ["Adventure", "Children"])
        self.assertEqual(Rental.get_price_for_movie(movie1), CHILDREN)
        self.assertEqual(Rental.get_price_for_movie(movie2), CHILDREN)
        self.assertEqual(Rental.get_price_for_movie(movie3), CHILDREN)

    def test_regular_movies(self):
        """Normal movies should have ChildrensPrice as price code."""
        movie1 = Movie("Frozen", 2010, ["Horror", "Adventure"])
        movie2 = Movie("Pacific Rim", 2013, ["Action", "Sci-Fi"])
        movie3 = Movie("Bad Boys", 1995, ["Action", "Comedy"])
        self.assertEqual(Rental.get_price_for_movie(movie1), REGULAR)
        self.assertEqual(Rental.get_price_for_movie(movie2), REGULAR)
        self.assertEqual(Rental.get_price_for_movie(movie3), REGULAR)

    def test_new_movies(self):
        """Movies release this year should have ChildrensPrice as price code."""
        movie1 = Movie("Trap", 2024, ["Horrow", "Mystery"])
        movie2 = Movie("Kang Fu Panda 4", 2024, ["Children", "Action", "Adventure"])
        movie3 = Movie("Abigail", 2024, ["Horror", "Thriller"])
        self.assertEqual(Rental.get_price_for_movie(movie1), NEW_RELEASE)
        self.assertEqual(Rental.get_price_for_movie(movie2), NEW_RELEASE)
        self.assertEqual(Rental.get_price_for_movie(movie3), NEW_RELEASE)
