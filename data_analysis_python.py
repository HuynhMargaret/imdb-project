
# coding: utf-8
import pandas as pd, numpy as np

# Read recipe inputs
df_ratings = pd.read_csv('titleratings.tsv', sep='\t')

df_basics = pd.read_csv('titlebasics.tsv', sep='\t')

df_principals = pd.read_csv('titlepincipals.tsv', sep='\t')

df_namebasics = pd.read_csv('namebasics.tsv', sep='\t')


#bayes mean for movies' rating (Oscars' rule - yearly, no differentiation in genres)
df_1 = pd.merge(df_ratings, df_basics, on="tconst")

df_1 = df_1[(df_1['titleType']=='movie')&(df_1['startYear']!='\N')&(df_1['genres'].str.contains('Documentary')==False)&(df_1['genres']!='\N')]
df_1['startYear'] = df_1['startYear'].astype(str).astype(int)

df_1['numVotes_annual'] = df_1.groupby(df_1['startYear'])['numVotes'].transform('mean')

df_1['w'] = df_1['numVotes']/(df_1['numVotes'] + df_1['numVotes_annual'])

df_1['annual_avgrating'] = df_1.groupby(df_1['startYear'])['averageRating'].transform('mean')
df_1['avg_bayes_rating'] = df_1['w']*df_1['averageRating'] + (1 - df_1['w'])*df_1['annual_avgrating']
df_1.head()


#Favorite director: Find the titles of all movies directed by Steven Spielberg
df_director = df_principals[df_principals['category']=='director']
df_directorname = pd.merge(df_director, df_namebasics, on="nconst")
df_2 = pd.merge(df_1, df_directorname, on="tconst")
df_favdirector = df_2[df_2['primaryName']=='Steven Spielberg']
df_favdirector.head()


#What were some good years for movies? Find all years that have a movie that received a rating of 9 and above, and sort them in increasing order.
df_3 = df_1[df_1['avg_bayes_rating']>=9.0]
print(df_3)
good_years = sorted(df_3.startYear.unique().tolist())
print(good_years)
len(good_years)


#Busy directors: Some directors directed more than one movie. For all such directors, return the titles of all movies directed by them, as well as the director name. Sort by director name, then movie title.
avgmoviedirect = df_2['primaryName'].value_counts().mean()
df_4 = df_2
df_4['movieDirected'] = df_4.primaryName.groupby(df_4.primaryName).transform('count')
df_4 = df_4[df_4['movieDirected']>avgmoviedirect]
df_4.head()


#Are older movies better-rated? Find the difference between the average rating of movies released before 1980 and the average rating of movies released after 1980
df_1_before1980 = df_1[df_1['startYear']<1980]
df_1_after1980 = df_1[df_1['startYear']>=1980]
avgrating_bef1980 = np.mean(df_1_before1980['avg_bayes_rating'])
print(avgrating_bef1980)
avgrating_aft1980 = np.mean(df_1_after1980['avg_bayes_rating'])
print(avgrating_aft1980)

