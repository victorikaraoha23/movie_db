import json
from movie import Movie 
from collection import MovieCollection 


def save_collection(collection,filename):
    with open(filename,"w") as f:
        for movie in collection.list_all():
            json.dump(movie.to_dict(),f)
            f.write("\n")
        
    


def load_collections(file_name):
    with open(file_name,):
        collection_list=json.load(file_name)
        return collection_list