import numpy as np
import pandas as pd
import ast
import nltk

movies = pd.read_csv('./static/dataset/tmdb_5000_movies.csv')
credits = pd.read_csv('./static/dataset/tmdb_5000_credits.csv') 

movies = movies.merge(credits,on='title')
movies = movies[['movie_id','title','overview','genres','keywords','cast']]

# print(movies['genres'][0])


# appending genres(Action,Fantasy...) and keywords(Future wars,space...) after converting in list
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L 
movies.dropna(inplace=True)

movies['keywords'] = movies['keywords'].apply(convert)
movies['genres'] = movies['genres'].apply(convert)

# print(movies)

# Appending top 5 actor name from cast
def convert3(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        else :
            break
        counter+=1
    return L 

movies['cast'] = movies['cast'].apply(convert)

# print(movies.head())

# Removing spaces

def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1

movies['cast'] = movies['cast'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)

movies_tags = movies ## ###

movies_tags['overview'] = movies_tags['overview'].apply(lambda x:x.split())
# print(movies_tags['overview'])

movies_tags['tags'] = movies_tags['overview'] + movies_tags['genres'] + movies_tags['keywords'] + movies_tags['cast']


movies_tags = movies.drop(columns=['overview','genres','keywords','cast'])

movies_tags['tags'] = movies_tags['tags'].apply(lambda x: " ".join(x))

# function for stemming__________________
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

movies_tags['tags'] = movies_tags['tags'].apply(stem)

# end _____________________


# print(movies_tags)

# converting movies to vector form


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')

vector = cv.fit_transform(movies_tags['tags']).toarray()

# vector.shape



from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vector)

# print(similarity)