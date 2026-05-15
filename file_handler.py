import json
from movie import Movie 
from collection import MovieCollection 


def save_collection(collection,filename):
    try:
     with open(filename,"w") as f:
        for movie in collection.list_all():
            json.dump(movie.to_dict(),f)
            f.write("\n")
    except FileNotFoundError:
        pass
        
        
    


def load_collections(file_name):
    try:
     with open(file_name,):
          collection_list=json.load(file_name)
          for movies in collection_list:
            loaded_movies=movies.from_dict()
         return loaded_movies
    except FileNotFoundError:
            pass