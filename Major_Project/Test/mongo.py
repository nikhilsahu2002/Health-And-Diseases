import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['your_collection_name']


def get_data():
    data = []
    for item in collection.find():
        data.append(item)
    return data
