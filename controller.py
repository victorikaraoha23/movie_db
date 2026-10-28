from api_client import APIError, fetch_movie
from cli import (
    confirm_action,
    display_error,
    display_message,
    display_movie_details,
    display_movies,
    display_success,
    get_menu_choice,
    prompt_director,
    prompt_filename,
    prompt_genre,
    prompt_rating,
    prompt_title,
    prompt_year,
    show_export_menu,
)
from exporter import export_csv, export_json, export_txt
from file_handler import load_collection, save_collection
from movie import Movie

DEFAULT_FILENAME = "movies.json"

EXPORTERS = {
    1: ("csv", export_csv),
    2: ("json", export_json),
    3: ("txt", export_txt),
}


class Controller:
    def __init__(self, filename=DEFAULT_FILENAME) -> None:
        self.filename = filename
        self.collection = load_collection(filename)

    def run(self):
        display_message(
            f"Loaded {self.collection.count()} movie(s) from {self.filename}."
        )
        try:
            while True:
                choice = get_menu_choice()
                if choice == 1:
                    self.add_movie()
                elif choice == 2:
                    self.view_movies()
                elif choice == 3:
                    self.search_movies()
                elif choice == 4:
                    self.delete_movie()
                elif choice == 5:
                    self.export_collection()
                elif choice == 6:
                    self.save()
                    display_message("Goodbye!")
                    return
        except KeyboardInterrupt:
            print()
            display_message("Interrupted - saving your collection.")
            self.save()

    def add_movie(self):
        if confirm_action("Look the movie up on OMDb?"):
            try:
                movie = self._lookup_movie()
            except (APIError, ValueError) as error:
                display_error(error)
                display_message("Falling back to manual entry.")
                movie = self._prompt_new_movie()
        else:
            movie = self._prompt_new_movie()

        if movie is None:
            return

        existing = self.collection.find_by_title(movie.title)
        if existing and not confirm_action(
            f"'{existing.title}' is already in the collection. Add it anyway?"
        ):
            display_message("Movie not added.")
            return

        self.collection.add_movie(movie)
        display_success(f"'{movie.title}' added.")

    def view_movies(self):
        movies = self.collection.list_all()
        display_movies(movies)
        if movies:
            display_message(f"Total: {len(movies)} movie(s).")

    def search_movies(self):
        query = input("enter a title or year to search for: ").strip()
        if not query:
            display_error("the search cannot be empty.")
            return
        display_movies(self.collection.search(query))

    def delete_movie(self):
        title = prompt_title()
        movie = self.collection.find_by_title(title)
        if movie is None:
            display_error(f"no movie titled '{title}' was found.")
            return
        if not confirm_action(f"Delete '{movie.title}' ({movie.year})?"):
            display_message("Nothing deleted.")
            return
        self.collection.remove(movie.title)
        display_success(f"'{movie.title}' deleted.")

    def export_collection(self):
        choice = show_export_menu()
        if choice == 4:
            return

        extension, exporter = EXPORTERS[choice]
        filename = prompt_filename(f"movies_export.{extension}")
        if not filename.lower().endswith(f".{extension}"):
            filename += f".{extension}"

        try:
            exporter(self.collection, filename)
        except OSError as error:
            display_error(f"could not write {filename} ({error}).")
            return
        display_success(f"exported {self.collection.count()} movie(s) to {filename}.")

    def save(self):
        try:
            save_collection(self.collection, self.filename)
        except OSError as error:
            display_error(f"could not save to {self.filename} ({error}).")
            return
        display_success(f"saved {self.collection.count()} movie(s) to {self.filename}.")

    def _lookup_movie(self):
        """Return the found movie, or None if the user declines to add it."""
        title = prompt_title()
        movie = Movie(**fetch_movie(title))
        display_message("Found:")
        display_movie_details(movie)
        if confirm_action("Add this movie?"):
            return movie
        display_message("Movie not added.")
        return None

    def _prompt_new_movie(self):
        title = prompt_title()
        year = prompt_year()
        rating = prompt_rating()
        director = prompt_director()
        genre = prompt_genre()
        try:
            return Movie(title, year, rating, director, genre)
        except ValueError as error:
            display_error(error)
            return None
