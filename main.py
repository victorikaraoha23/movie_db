# test_movie.py
# Tests for the Movie class

from movie import Movie
import sys

def print_header(label):
    print(f"\n{'='*50}\n{label}\n{'='*50}")

def test_creation_and_getters():
    print_header("TEST 1: Creation and Getters")
    m = Movie("The Matrix", 1999, 8.7, "Lana Wachowski", "Action")
    print(f"Movie created: {m}")
    print(f"Title: {m.title}")
    print(f"Year: {m.year}")
    print(f"Rating: {m.rating}")
    print(f"Director: {m.director}")
    print(f"Genre: {m.genre}")
    print(f"Poster URL: {m.poster_url}")

def test_validation():
    print_header("TEST 2: Validation (should raise errors)")
    tests = [
        ("", 2000, 5.0, "Director"),          # Empty title
        ("   ", 2000, 5.0, "Director"),       # Whitespace title
        ("Valid", 1800, 5.0, "Director"),     # Year < 1888
        ("Valid", "not_int", 5.0, "Director"), # Year non-int
        ("Valid", 2000, 15.0, "Director"),    # Rating > 10
        ("Valid", 2000, -1.0, "Director"),    # Rating < 0
        ("Valid", 2000, "not_float", "Director"), # Rating non-float
    ]
    for idx, (title, year, rating, director) in enumerate(tests, 1):
        try:
            m = Movie(title, year, rating, director)
            print(f"❌ Test {idx} FAILED: Should have raised error, but got {m}")
        except Exception as e:
            print(f"✅ Test {idx} PASSED: Caught {type(e).__name__}: {e}")

def test_to_dict():
    print_header("TEST 3: to_dict()")
    m = Movie("Inception", 2010, 8.8, "Christopher Nolan", "Sci-Fi", "http://example.com/poster.jpg")
    data = m.to_dict()
    print(f"to_dict() output: {data}")
    # Check keys
    expected_keys = {"title", "year", "rating", "director", "genre", "poster_url"}
    assert expected_keys == set(data.keys()), "Missing keys in to_dict()"
    print("✅ to_dict() contains all expected keys")

def test_from_dict():
    print_header("TEST 4: from_dict()")
    data = {
        "title": "Interstellar",
        "year": 2014,
        "rating": 8.6,
        "director": "Christopher Nolan",
        "genre": "Sci-Fi",
        "poster_url": None
    }
    m = Movie.from_dict(data)
    print(f"from_dict() created: {m}")
    assert m.title == "Interstellar"
    assert m.year == 2014
    assert m.rating == 8.6
    assert m.director == "Christopher Nolan"
    assert m.genre == "Sci-Fi"
    assert m.poster_url is None
    print("✅ from_dict() works with complete data")

def test_from_dict_missing_fields():
    print_header("TEST 5: from_dict() with missing required fields (should crash)")
    # This tests the current bug in your implementation
    incomplete_data = {
        "title": "Gladiator",
        # missing "year" and "rating"
    }
    try:
        m = Movie.from_dict(incomplete_data)
        print(f"❌ Should have crashed, but got: {m}")
    except Exception as e:
        print(f"✅ Correctly crashed with: {type(e).__name__}: {e}")

def test_from_dict_extra_fields():
    print_header("TEST 6: from_dict() with extra fields")
    data = {
        "title": "Goodfellas",
        "year": 1990,
        "rating": 8.7,
        "director": "Martin Scorsese",
        "genre": "Crime",
        "poster_url": None,
        "extra_field": "should be ignored"
    }
    m = Movie.from_dict(data)
    print(f"Created: {m}")
    assert m.title == "Goodfellas"
    assert m.year == 1990
    assert m.rating == 8.7
    assert m.director == "Martin Scorsese"
    assert m.genre == "Crime"
    print("✅ Extra fields ignored (if no error)")

def test_round_trip():
    print_header("TEST 7: Round trip (Movie → dict → Movie)")
    original = Movie("The Dark Knight", 2008, 9.0, "Christopher Nolan", "Action")
    data = original.to_dict()
    restored = Movie.from_dict(data)
    print(f"Original: {original}")
    print(f"Restored: {restored}")
    assert original.title == restored.title
    assert original.year == restored.year
    assert original.rating == restored.rating
    assert original.director == restored.director
    assert original.genre == restored.genre
    assert original.poster_url == restored.poster_url
    print("✅ Round trip successful")

def test_optional_fields():
    print_header("TEST 8: Optional fields (genre, poster_url)")
    m1 = Movie("Fight Club", 1999, 8.8, "David Fincher")  # no genre, no poster
    print(f"Without optional: {m1}")
    assert m1.genre is None
    assert m1.poster_url is None

    m2 = Movie("Pulp Fiction", 1994, 8.9, "Quentin Tarantino", genre="Crime")
    print(f"With genre only: {m2}")
    assert m2.genre == "Crime"
    assert m2.poster_url is None
    print("✅ Optional fields work")

def test_str():
    print_header("TEST 9: __str__()")
    m = Movie("The Godfather", 1972, 9.2, "Francis Ford Coppola")
    s = str(m)
    print(f"__str__() output: {s}")
    # Just ensure it prints without crashing
    print("✅ __str__() executed")

if __name__ == "__main__":
    test_creation_and_getters()
    test_validation()
    test_to_dict()
    test_from_dict()
    test_from_dict_missing_fields()
    test_from_dict_extra_fields()
    test_round_trip()
    test_optional_fields()
    test_str()
    print("\n🎉 All tests completed.")