def get_menu_choice():
    print(
        "============================================ MOVIE MENU :) ======================================"  # noqa: E501
    )
    print("1.Add a movie")
    print("2.View all movies")
    print("3.Search for a movie")
    print("4.Delete a movie")
    print("5.Export collections")
    print("6.Save & Exit")
    active = True
    while active:
        try:
            display = int(input("enter your choice (1-6): "))
            if display < 1 or display > 6:
                print("please enter a valid choice from 1 - 6")
            else:
                active = False
                return display
        except ValueError:
            print("input the correct datatype")


def prompt_title():
    active = True
    while active:
        display = input("enter movie title: ")
        if not display:
            print("please enter a title")
        else:
            active = False
            return display.strip()


def prompt_year():
    active = True
    while active:
        try:
            display = int(input("enter release year: "))
            if display < 1888:
                print("please enter a valid release year")
            else:
                active = False
                return display
        except ValueError:
            print("input the correct datatype")


def prompt_rating():
    active = True
    while active:
        try:
            display = float(input("enter rating (0.0-10.0): "))
            if display < 0.0 or display > 10.0:
                print("please enter a valid rating frrom 0.0 - 10.0")
            else:
                active = False
                return display
        except ValueError:
            print("input the correct datatype")


def prompt_director():
    display = input("enter director(press enter to skip): ")
    value = display.strip()
    if not value:
        return None
    else:
        return value


def prompt_genre():
    display = input("enter genre(press enter to skip): ")
    value = display.strip()
    if not value:
        return None
    else:
        return value


def prompt_filename(default):
    display = input(f"enter filename(press enter for '{default}'): ")
    if not display:
        return default
    else:
        return display.strip()


def confirm_action(message):
    active = True
    while active:
        display = input(f"{message} (y/n): ")
        if display.lower() == "n":
            active = False
            return False
        elif display.lower() == "y":
            active = False
            return True
        else:
            print("please input either y or n")


def display_movies(movies):
    counter = 1
    if not movies:
        print("no movies in collection")
    else:
        for items in movies:
            print(f"{counter}. {str(items)}")
            counter += 1


def display_movie_details(movie):
    movies = movie.to_dict()
    for key, values in movies.items():
        if values is None:
            pass
        else:
            print(f"{key.replace('_', ' ').title()}: {values}")


def display_message(message):
    print(message)


def display_error(message):
    print(f"error: {message}")


def display_success(message):
    print(f"success: {message}")


def show_export_menu():
    print("export options:")
    print("1. Export to CSV")
    print("2. Export to JSON")
    print("3. Export to TXT")
    print("4. Back to main menu")
    active = True
    while active:
        try:
            display = int(input("enter your choice (1-4): "))
            if display < 1 or display > 4:
                print("please enter a valid choice from 1 - 4")
            else:
                active = False
                return display
        except ValueError:
            print("input the correct datatype")
