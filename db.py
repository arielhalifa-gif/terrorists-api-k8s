from pymongo import MongoClient

class Connection:

    def get_connection():
        client = MongoClient(
                            host='localhost',
                            port=27017,
                            username='admin',
                            password='secretpass',
                            authSource='admin')
        db = client["threat_db"]
        return db
    
    def insert_to_db(data):
        db = Connection.get_connection()
        collection = db["top_threats"]
        result = collection.insert_many(data)
        return result
