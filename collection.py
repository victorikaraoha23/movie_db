class MovieCollection:
    def __init__(self):
        self.movies = []

    def add(self,data):
        self.movies.append(data.to_dict())


    def remove(self,title):
        if title.lower

    def find_by_title(self):
        pass

    def find_by_year(self):
        pass

    def list_all(self):
        pass

    def count(self):
        return f"there are {len(self.movies)} movies in the collection"
        

    def sort_by_rating(self):
        sort() 