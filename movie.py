from typing import Collection
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    title: str
    year: int
    genre: Collection[str]

    def __str__(self):
        """Return the title and year of the movie."""
        return f"{self.title} ({self.year})"

    def is_genre(self, string: str):
        """Return true if the movie belongs to the inputted genre."""
        return string.capitalize() in self.genre
