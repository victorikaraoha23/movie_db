import json

from collection import MovieCollection
from movie import Movie


def save_collection(collection, filename):
    with open(filename, "w") as f:
        collection_list = []
        for movie in collection.list_all():
            collection_list.append(movie.to_dict())
        json.dump(collection_list, f, indent=4)


def load_collection(file_name):
    try:
        with open(file_name) as f:
            collection_list = json.load(f)
            collection = MovieCollection()
            for movie_dict in collection_list:
                movie_object = Movie.from_dict(movie_dict)
                collection.add_movie(movie_object)
            return collection
    except FileNotFoundError:
        return MovieCollection()
