from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""

    _instance = None

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass

    def __new__(cls):
        """Make each child class a Singleton."""
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_price(self, days: int) -> float:
        """Regular movie rentals cost $2 for 2 days, additional days for $1.50 per day."""
        amount = 2.0
        if days > 2:
            amount += 1.5*(days-2)
        return amount

    def get_rental_points(self, days: int) -> int:
        """Regular movie rentals earn 1 point regardless of the number of days rented."""
        return 1


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_price(self, days: int) -> float:
        """New Release movie rentals cost $3 per day."""
        return 3 * days

    def get_rental_points(self, days: int) -> int:
        """New Release movie rentals earn 1 point for each day rented."""
        return days


class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children movies."""

    def get_price(self, days: int) -> float:
        """Children movie rentals cost $1.50 for 3 days, additional days for $1.50 per day."""
        amount = 1.5
        if days > 3:
           amount += 1.5*(days-3)
        return amount

    def get_rental_points(self, days: int) -> int:
        """Children movie rentals earn 1 point regardless of the number of days rented."""
        return 1


NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()
