from collection import MovieCollection
from movie import Movie


def _sample_collection():
    col = MovieCollection()
    col.add_movie(Movie("Inception", 2010, 8.8, "Christopher Nolan", "Sci-Fi"))
    col.add_movie(Movie("The Matrix", 1999, 8.7, "Lana Wachowski", "Action"))
    col.add_movie(Movie("Interstellar", 2014, 8.6, "Christopher Nolan", "Sci-Fi"))
    return col


def test_find_is_case_insensitive():
    print("=== Testing find_by_title() ===\n")
    col = _sample_collection()
    assert col.find_by_title("inception").title == "Inception"
    assert col.find_by_title("  THE MATRIX  ".strip()).title == "The Matrix"
    assert col.find_by_title("Nope") is None
    print("find_by_title passed\n")


def test_search_by_title_and_year():
    print("=== Testing search() ===\n")
    col = _sample_collection()
    assert len(col.search("stellar")) == 1
    assert len(col.search("2010")) == 1
    assert len(col.search("in")) == 2  # Inception, Interstellar
    assert col.search("zzz") == []
    print("search passed\n")


def test_remove_all_movies():
    print("=== Testing remove() ===\n")
    col = _sample_collection()
    # Removing every movie catches the skip caused by mutating while looping.
    for title in ["inception", "the matrix", "interstellar"]:
        assert col.remove(title) is not None
    assert col.count() == 0
    assert col.remove("inception") is None
    print("remove passed\n")


if __name__ == "__main__":
    test_find_is_case_insensitive()
    test_search_by_title_and_year()
    test_remove_all_movies()
    print("\nAll collection tests completed!")
