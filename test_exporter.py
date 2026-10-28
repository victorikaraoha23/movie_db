import csv
import os
import tempfile

from collection import MovieCollection
from exporter import export_csv, export_json, export_txt
from file_handler import load_collection
from movie import Movie


def _sample_collection():
    col = MovieCollection()
    col.add_movie(Movie("Inception", 2010, 8.8, "Christopher Nolan", "Sci-Fi"))
    col.add_movie(Movie("The Matrix", 1999, 8.7, "Lana Wachowski", "Action"))
    return col


def test_export_csv():
    print("=== Testing export_csv() ===\n")
    col = _sample_collection()
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
        filename = tmp.name
    export_csv(col, filename)
    with open(filename, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 2
    assert rows[0]["title"] == "Inception"
    assert rows[0]["director"] == "Christopher Nolan"
    os.remove(filename)
    print("CSV export passed\n")


def test_export_json_round_trip():
    print("=== Testing export_json() ===\n")
    col = _sample_collection()
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        filename = tmp.name
    export_json(col, filename)
    loaded = load_collection(filename)
    assert [m.title for m in loaded.list_all()] == ["Inception", "The Matrix"]
    os.remove(filename)
    print("JSON export passed\n")


def test_export_txt():
    print("=== Testing export_txt() ===\n")
    col = _sample_collection()
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
        filename = tmp.name
    export_txt(col, filename)
    with open(filename, encoding="utf-8") as f:
        text = f.read()
    assert "Inception (2010)" in text
    assert "Genre: Sci-Fi" in text
    os.remove(filename)
    print("TXT export passed\n")


def test_export_empty_collection():
    print("=== Testing export of an empty collection ===\n")
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
        filename = tmp.name
    export_csv(MovieCollection(), filename)
    with open(filename, encoding="utf-8") as f:
        assert f.read().strip() == "title,year,rating,director,genre,poster_url"
    os.remove(filename)
    print("Empty collection export passed\n")


if __name__ == "__main__":
    test_export_csv()
    test_export_json_round_trip()
    test_export_txt()
    test_export_empty_collection()
    print("\nAll exporter tests completed!")
