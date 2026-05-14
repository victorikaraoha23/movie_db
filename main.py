# test_collection.py
# Test file for MovieCollection class

from movie import Movie
from collection import MovieCollection

def run_collection_tests():
    print("=== Testing MovieCollection ===\n")

    # --- Setup ---
    col = MovieCollection()
    
    # Create movie objects
    m1 = Movie("Inception", 2010, 8.8, "Christopher Nolan", "Sci-Fi")
    m2 = Movie("The Matrix", 1999, 8.7, "Lana Wachowski", "Action")
    m3 = Movie("Interstellar", 2014, 8.6, "Christopher Nolan", "Sci-Fi")
    m4 = Movie("Fight Club", 1999, 8.8, "David Fincher", "Drama")

    # --- Test 1: Add and Count ---
    print("1. Testing add_movie() and count()")
    col.add_movie(m1)
    col.add_movie(m2)
    col.add_movie(m3)
    col.add_movie(m4)
    print(f"   Count = {col.count()} (expected 4)")
    assert col.count() == 4
    print("   ✅ Passed")

    # --- Test 2: List All ---
    print("\n2. Testing list_all()")
    all_movies = col.list_all()
    print(f"   List has {len(all_movies)} movies")
    for movie in all_movies:
        print(f"     {movie}")
    assert len(all_movies) == 4
    print("   ✅ Passed")

    # --- Test 3: Find by Title ---
    print("\n3. Testing find_by_title()")
    found = col.find_by_title("Inception")
    print(f"   Found 'Inception': {found}")
    # Compare by title instead of object identity
    print(f"Collection count after adding: {col.count()}")
    print(f"Movies in collection: {[m.title for m in col.list_all()]}")
    found = col.find_by_title("Inception")
    print(f"Found object: {found}")
    assert found.title == "Inception"
    assert found.title == "Inception"
    assert found.year == 2010

    not_found = col.find_by_title("Avatar")
    print(f"   Looking for 'Avatar': {not_found}")
    assert not_found is None
    print("   ✅ Passed")

    # --- Test 4: Find by Year ---
    print("\n4. Testing find_by_year()")
    movies_1999 = col.find_by_year(1999)
    print(f"   Movies from 1999: {[str(m) for m in movies_1999]}")
    assert len(movies_1999) == 2
    # Check titles instead of objects
    titles_1999 = [m.title for m in movies_1999]
    assert "The Matrix" in titles_1999
    assert "Fight Club" in titles_1999

    movies_2010 = col.find_by_year(2010)
    print(f"   Movies from 2010: {[str(m) for m in movies_2010]}")
    assert len(movies_2010) == 1
    assert movies_2010[0].title == "Inception"

    movies_2020 = col.find_by_year(2020)
    print(f"   Movies from 2020: {movies_2020}")
    assert isinstance(movies_2020, list)
    assert len(movies_2020) == 0
    print("   ✅ Passed")

    # --- Test 5: Remove ---
    print("\n5. Testing remove()")
    removed = col.remove("The Matrix")
    print(f"   Removed: {removed}")
    assert removed.title == "The Matrix"
    assert col.count() == 3
    assert col.find_by_title("The Matrix") is None

    not_removed = col.remove("Avatar")
    print(f"   Attempt to remove 'Avatar': {not_removed}")
    assert not_removed is None
    print("   ✅ Passed")

    # --- Test 6: Sort by Rating ---
    print("\n6. Testing sort_by_rating()")
    col.sort_by_rating()
    sorted_list = col.list_all()
    print("   Sorted by rating (descending):")
    for movie in sorted_list:
        print(f"     {movie}")
    # Check that rating order is correct
    for i in range(len(sorted_list) - 1):
        assert sorted_list[i].rating >= sorted_list[i+1].rating
    print("   ✅ Passed")

    # --- Test 7: Edge Cases ---
    print("\n7. Testing edge cases")
    empty_col = MovieCollection()
    assert empty_col.count() == 0
    assert empty_col.list_all() == []
    assert empty_col.find_by_title("Anything") is None
    assert empty_col.find_by_year(2000) == []
    assert empty_col.remove("Anything") is None
    print("   ✅ Passed")

    print("\n=== All tests passed! ===")

if __name__ == "__main__":
    run_collection_tests()