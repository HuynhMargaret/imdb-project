"""
@author: HuynhMargaret
"""

from imdb import IMDb
import pandas as pd

ia = IMDb()

def read_person_dict(x):
    person_dict = {}
    person_dict['name_id'] = x
    name_id = x[2:]
    person = ia.get_person(name_id)
    for i in person.items():
        person_dict[i[0]] = i[1]
    return person_dict

dataset = pd.read_excel(r'C:\Users\quynh\Downloads\imdb_name.xlsx')

name_list = dataset.nconst.unique().tolist()

person_data_list = []
person_skipped = []

for i in name_list:
   
    try:
        person_dict = read_person_dict(i)
    except:
        person_skipped.append(i)
        print("We skipped: ",i)
        continue
    else:
        person_data_list.append(person_dict)
        print("We finished: ",i)
     
df = pd.DataFrame(person_data_list)

