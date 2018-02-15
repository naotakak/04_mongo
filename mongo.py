from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu') #connection start

db = c.test #database object
border = db.restaurants #Border Colliection

#prints all resturants in a given borough
def borough(boro):
    result = border.find({'borough': boro}) 
    print("All restaurants in borough " + boro)
    #find() returns a iterator, loop
    for item in result:
        print(item)

#prints all resturants in zipcode 
def zipcode(code):
    result = border.find({'address.zipcode': code})
    print("All restaurants in zipcode " + code)
    for item in result:
        print (item)

#prints all resturants in a zipcode with a certain grade
def zipgrade(code, grade):
    result = border.find({'$and' : [{'address.zipcode': code}, {'grades.grade':grade}]}) #AND OPERATOR
    print("All restaurants in zipcode " + code + " with grade " + grade)
    for item in result:
        print (item)

#prints all resturants in a zipcode within a certain score
def zipbelow(code, score):
    result = border.find({'$and' : [{'address.zipcode': code}, {'grades.score': {'$lt':score}}]})
    print("All restaurants in zipcode " + code + " with score below " + str(score))
    for item in result:
        print (item)
        
#look at the paramaters 
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
