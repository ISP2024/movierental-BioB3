from typing import Collection
from dataclasses import dataclass
import csv
import logging


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
        return string.lower() in [genre.lower() for genre in self.genre]


class MovieCatalog:
    """
    A factory class to create Movie from a CSV file.
    """

    _instance = None

    def __init__(self) -> None:
        self._movies: list[Movie] = []
        self._generator = self.load_movie_data()
        self._logger = logging.getLogger()

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    def load_movie_data(self):
        """Get a movie generator from movies.csv"""
        with open("movies.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if not row or row[0].startswith("#"):
                    continue
                try:
                    yield Movie(row[1], int(row[2]), row[3].split("|"))
                except (IndexError, ValueError):
                    self._logger.error(
                        f'Line {csv_reader.line_num}: Unrecognized format "{(",".join(row))}"'
                    )

    def get_movie(self, title: str, year: int = -1):
        """Return a movie with matching title and optional year."""

        def find_movie(movies):
            for movie in movies:
                if (movie.title == title) and (year == -1 or movie.year == year):
                    return movie
            return None

        found = find_movie(self._movies)
        if found is None:
            for movie in self._generator:
                self._movies.append(movie)
                found = find_movie([movie])
                if found is not None:
                    break
        return found
