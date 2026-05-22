# test_file_handler.py
# Tests for file_handler module (save_collection and load_collection)
import json
import os
import tempfile

from collection import MovieCollection
from file_handler import load_collection, save_collection
from movie import Movie


def test_save_and_load():
    print("=== Testing save_collection() and load_collection() ===\n")

    # --- Create a collection with test movies ---
    col = MovieCollection()
    m1 = Movie("Inception", 2010, 8.8, "Christopher Nolan", "Sci-Fi")
    m2 = Movie("The Matrix", 1999, 8.7, "Lana Wachowski", "Action")
    m3 = Movie("Interstellar", 2014, 8.6, "Christopher Nolan", "Sci-Fi")
    col.add_movie(m1)
    col.add_movie(m2)
    col.add_movie(m3)

    # --- Save to a temporary file ---
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
        tmp_filename = tmp.name
    print(f"1. Saving collection to {tmp_filename}")
    save_collection(col, tmp_filename)

    # --- Verify file exists and has content ---
    assert os.path.exists(tmp_filename)
    with open(tmp_filename) as f:
        data = json.load(f)
    print(f"   File contains {len(data)} movies")
    assert len(data) == 3

    # --- Load back from the file ---
    print("2. Loading collection from the same file")
    loaded_col = load_collection(tmp_filename)
    print(f"   Loaded collection has {loaded_col.count()} movies")
    assert loaded_col.count() == 3

    # --- Compare original and loaded collections by title ---
    original_titles = {m.title for m in col.list_all()}
    loaded_titles = {m.title for m in loaded_col.list_all()}
    assert original_titles == loaded_titles
    print("   ✅ Titles match")

    # --- Clean up ---
    os.remove(tmp_filename)
    print("3. Temporary file deleted")
    print("✅ Save and load test passed!\n")


def test_missing_file():
    print("=== Testing missing file ===\n")
    non_existent = "this_file_does_not_exist.json"
    print(f"1. Loading from {non_existent}")
    col = load_collection(non_existent)
    print(f"   Returned collection count: {col.count()}")
    assert col.count() == 0
    assert col.list_all() == []
    print("✅ Missing file returns empty collection\n")


def test_corrupted_file():
    print("=== Testing corrupted file ===\n")
    # Create a corrupt JSON file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
        tmp.write("this is not valid json")
        tmp_filename = tmp.name
    print(f"1. Created corrupt file: {tmp_filename}")

    # Try to load it — your load_collection should handle this gracefully
    try:
        col = load_collection(tmp_filename)
        print(f"   Loaded collection count: {col.count()}")
        # If it handled corruption, it should return
        # an empty collection or create a backup
        assert col.count() == 0
        print("   ✅ Corrupted file handled (returned empty collection)")
    except Exception as e:
        print(f"   ❌ load_collection raised exception: {e}")
        print("   (Your file_handler should handle corrupted files gracefully)")

    # Clean up
    os.remove(tmp_filename)
    print("2. Corrupted file deleted\n")


def test_round_trip_with_empty_collection():
    print("=== Testing empty collection round trip ===\n")
    empty_col = MovieCollection()
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
        tmp_filename = tmp.name
    print(f"1. Saving empty collection to {tmp_filename}")
    save_collection(empty_col, tmp_filename)

    print("2. Loading empty collection")
    loaded_col = load_collection(tmp_filename)
    print(f"   Loaded collection count: {loaded_col.count()}")
    assert loaded_col.count() == 0
    assert loaded_col.list_all() == []
    print("✅ Empty collection round trip passed\n")

    os.remove(tmp_filename)


if __name__ == "__main__":
    test_save_and_load()
    test_missing_file()
    test_corrupted_file()
    test_round_trip_with_empty_collection()
    print("\n🎉 All file handler tests completed!")
