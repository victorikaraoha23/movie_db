import json
import os

from collection import MovieCollection
from movie import Movie


def save_collection(collection, filename):
    with open(filename, "w", encoding="utf-8") as f:
        collection_list = []
        for movie in collection.list_all():
            collection_list.append(movie.to_dict())
        json.dump(collection_list, f, indent=4)


def load_collection(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            collection_list = json.load(f)
    except FileNotFoundError:
        return MovieCollection()
    except json.JSONDecodeError:
        # Keep the broken file around instead of silently overwriting it.
        os.replace(file_name, f"{file_name}.corrupt")
        return MovieCollection()

    collection = MovieCollection()
    for movie_dict in collection_list:
        try:
            collection.add_movie(Movie.from_dict(movie_dict))
        except (KeyError, TypeError, ValueError):
            # Skip entries that were hand-edited into something unusable.
            continue
    return collection
