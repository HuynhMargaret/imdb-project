"""
@author: HuynhMargaret
"""
from imdb import IMDb
import xml.etree.ElementTree as ET
import pandas as pd


#define function to parse movie information from IMDbPY and turn it to a dictionary
def read_movie_dict(x):
    movie_dict = {}
    for item in x:
        if item.text != None or len(item) == 0:
            movie_dict[item.tag] = item.text
        else:
            movie_dict[item.tag] = []
            for i in item:
                cast_dict = {}
                if i.text != None:
                    cast_dict[i.tag] = i.text
                else:
                    for j in i:
                        if j.text != None or len(j) == 0:
                            cast_dict[j.tag] = j.text
                        else:
                            cast_dict[j.tag] = {}
                            for k in j:
                                if k.text != None or len(k) == 0:
                                    cast_dict[j.tag][k.tag] = k.text
                                else:
                                    cast_dict[j.tag][k.tag] = k[0].text
                movie_dict[item.tag].append(cast_dict)
    return movie_dict


# create an instance of the IMDb class
ia = IMDb()

#input - ID of top movies every year, based on Bayesian Average Rating
dataset = pd.read_excel(r'C:\Users\quynh\Downloads\title_top_annual.xlsx')

#get data from IMDbPY
movie_data_list = []
movie_skipped = []
for i in dataset.tconst.unique().tolist():
    # get a movie
    id_movie = i[2:]
    
    try:
        movie = ia.get_movie(str(id_movie))
    except:
        movie_skipped.append(id_movie)
        print("We skipped: ",id_movie)
        continue
    else:
        movie_str = ET.fromstring(movie.asXML())
        movie_dict = read_movie_dict(movie_str)
        movie_data_list.append(movie_dict)
        print("We finished: ",id_movie)

#export output     
df = pd.DataFrame(movie_data_list)
    



