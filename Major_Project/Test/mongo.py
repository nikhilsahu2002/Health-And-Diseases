import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['HealthAndDisease']
collection = db['Project']


def get_data():
    data = []
    for item in collection.find():
        data.append(item)
    return data
