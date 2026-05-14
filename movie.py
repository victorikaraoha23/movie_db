class Movie:
    def __init__(self, title, year, rating, director, genre=None, poster_url=None):
        self.title = title
        self.year = year
        self.rating = rating
        self.director = director
        self.genre = genre
        self.poster_url = poster_url

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value or not value.strip():
            raise ValueError("Title cannot be empty.")
        else:
            self._title = value.strip()


    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        year_int = int(value)  # Ensure it's a number
        if year_int < 1888:
            raise ValueError("Year must be a number greater than or equal to 1888.")
        else:
            self._year = year_int

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        value_float = float(value)  # Ensure it's a number
        if not (0.0 <= value_float <= 10.0):
            raise ValueError("Rating must be a number between 0.0 and 10.0.")
        else:
            self._rating = value_float
    
    def __str__(self):
        return f"{self.title} ({self.year}) - Directed by {self.director}, Rating: {self.rating}/10"

    def __repr__(self):
        return f"{self.title} ({self.year}) - Directed by {self.director}, Rating: {self.rating}/10"
    
    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "rating": self.rating,
            "director": self.director,
            "genre": self.genre,
            "poster_url": self.poster_url
        }
    @classmethod
    def from_dict(cls, data):
        return Movie(
            title=data["title"],
            year=data["year"],
            rating=data["rating"],
            director=data["director"],
            genre=data["genre"],
            poster_url=data["poster_url"]
        )
       


