def show_info():
    print(
        "============================================ MOVIE MENU :) ======================================"
    )
    print("1.Add a movie")
    print("2.View all movie")
    print("3.Delete a movie")
    print("4.Delete a movie")
    print("5.Export collections")
    print("6.Save & Exit")


show_info()


def prompt_title():
    active = True
    while active:
        display = input("emter movie title: ")
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
            if not display:
                print("please enter a release year")
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
            if not display or display > 10.0:
                print("please enter a valid rating frrom 0.0 - 10.0")
            else:
                active = False
                return display
        except ValueError:
            print("input the correct datatype")


def prompt_director():
    active = True
    while active:
        display = input("enter director(press enter to skip): ")
        active = False
        return display.strip()


def prompt_genre():
    active = True
    while active:
        display = input("enter genre(press enter to skip): ")
        active = False
        return display.strip()


def prompt_filename():
    active = True
    while active:
        display = input("emter filename(press enter for '{default}'): ")
        if not display:
            print("please enter a filename")
        else:
            active = False
            return display.strip()


def confirm_action():
    pass


def display_movies():
    pass


def display_movie_details():
    pass


def display_message():
    pass


def display_error():
    pass


def display_success():
    pass


def show_export_menu():
    pass


print(prompt_filename())
