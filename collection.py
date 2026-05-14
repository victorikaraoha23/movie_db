class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self,data):
        self.movies.append(data)


    def remove(self,title):
        for element in self.movies:
            if element.title == title:
                self.movies.remove(element)
                return element
        return None

    def find_by_title(self,title):
        for element in self.movies:
            if element.title == title:
                return element
        return None

    def find_by_year(self,year):
        new_list=[]
        for element in self.movies:
             if element.year == year:
                new_list.append(element)
        return new_list
        

        

    def list_all(self):
        return self.movies.copy()
        
    def count(self):
        return len(self.movies)

    def sort_by_rating(self):
        self.movies.sort(key=lambda x: x.rating, reverse=True)