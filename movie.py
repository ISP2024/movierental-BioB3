import pricing


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, price_code : pricing.PriceStrategy):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self) -> str:
        return self.title

    def __str__(self):
        return self.title
