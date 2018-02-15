from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu')

db = c.test
border = db.restaurants

def borough(boro):
    result = border.find({'borough': boro})
    print("All restaurants in borough " + boro)
    for item in result:
        print(item)

def zipcode(code):
    result = border.find({'address.zipcode': code})
    print("All restaurants in zipcode " + code)
    for item in result:
        print (item)

def zipgrade(code, grade):
    result = border.find({'$and' : [{'address.zipcode': code}, {'grades.grade':grade}]})
    print("All restaurants in zipcode " + code + " with grade " + grade)
    for item in result:
        print (item)

def zipbelow(code, score):
    result = border.find({'$and' : [{'address.zipcode': code}, {'grades.score': {'$lt':score}}]})
    print("All restaurants in zipcode " + code + " with score below " + str(score))
    for item in result:
        print (item)

def clever(cuisine, boro):
    result = border.find({'$and' : [{'cuisine': cuisine}, {'borough': boro}]})
    print("All " + cuisine + " restaurants in borough " + boro)
    for item in result:
        print (item)


borough('Queens')
zipcode('11368')
zipgrade('11368', 'B')
zipbelow('11368', 6)
clever('Japanese', 'Manhattan')
