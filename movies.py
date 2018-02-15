'''
Jasper Cheung & Naotaka Kinoshita
SoftDev2 pd7
K05 -- Import/Export Bank
2018-02-15

Dataset: American Movies Scraped from Wikipedia
https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json
We took the json file directly from the download link using urllib2, and then imported
the entire json response to lisa.
'''

from pymongo import MongoClient
import urllib2
import json

c = MongoClient('lisa.stuy.edu')

db = c['mfDOOM']
coll = db['movies']

#coll.insert_one({'test':'test'})

def get_movies(url):
    resp = urllib2.urlopen(url)
    jason = resp.read()
    d = json.loads(jason)
    return d

def add_movies(json):
    coll.insert_many(json)

def search_title(title):
    pass

def after_year(year):
    pass

def director(director):
    pass

def year(year):
    pass

def before_year(year):
    pass

def genre_year(genre, year):
    pass

movies = get_movies('https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json')
add_movies(movies)
