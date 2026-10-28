import csv

from file_handler import save_collection

FIELDS = ["title", "year", "rating", "director", "genre", "poster_url"]


def export_csv(collection, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for movie in collection.list_all():
            writer.writerow(movie.to_dict())


def export_json(collection, filename):
    # Same format as the collection file, so an export can be loaded back in.
    save_collection(collection, filename)


def export_txt(collection, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for movie in collection.list_all():
            f.write(f"{movie}\n")
            if movie.genre:
                f.write(f"    Genre: {movie.genre}\n")
            if movie.poster_url:
                f.write(f"    Poster: {movie.poster_url}\n")
            f.write("\n")
