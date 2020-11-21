from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

user = db.movies.find_one({'title': '월-E'})
print(user['star'])

same_stars = list(db.movies.find({'star': 9.41}))
print(same_stars['title'])