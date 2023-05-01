import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['HealthAndDisease']
collection = db['persion']


def get_data():
    data = []
    for item in collection.find({"Symptom_1":" headache"}):
        data.append(item)
    return data
