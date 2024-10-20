import pricing
import datetime
from movie import Movie


class Rental:
   """
   A rental of a movie by customer.
   From Fowler's refactoring example.

   A realistic Rental would have fields for the dates
   that the movie was rented and returned, from which the
   rental period is calculated.
   For simplicity of this application only days_rented is recorded.
   """

   def __init__(self, movie, days_rented):
      """Initialize a new movie rental object for
      a movie with known rental period (daysRented).
      """
      self.movie = movie
      self.days_rented = days_rented
      self.price_code = self.get_price_for_movie(movie)

   def get_movie(self):
      return self.movie

   def get_days_rented(self):
      return self.days_rented

   def get_price_code(self):
      return self.price_code

   def get_price(self) -> float:
      """Get the rental price for this rental."""
      return self.price_code.get_price(self.get_days_rented())

   def get_rental_points(self) -> int:
      """Get the rental points earned from this rental."""
      return self.price_code.get_rental_points(self.get_days_rented())

   @classmethod
   def get_price_for_movie(cls, movie: Movie):
      """Get the price code of the movie."""
      current_year = datetime.datetime.today().year
      if movie.year == current_year:
         return pricing.NEW_RELEASE
      if movie.is_genre("Children") or movie.is_genre("Childrens"):
         return pricing.CHILDREN
      return pricing.REGULAR